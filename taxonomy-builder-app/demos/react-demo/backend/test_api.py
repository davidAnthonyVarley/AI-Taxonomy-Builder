from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import List

from chatgpt_api import message_chatGPT

app = FastAPI()

# this is a set of fake nodes, to test if our generate function successfully appends nodes to an existing taxonomy

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Node(BaseModel):
    id: str
    type: str
    position: dict
    data: dict
    width: int
    height: int
    selected: bool
    dragging: bool


class Edge(BaseModel):
    # Define Edge model if needed
    id: str
    source: str
    target: str


class InputData(BaseModel):
    nodes: List[Node]
    edges: List[Edge]
    current_node: str


def generate(nodes: List[Node], edges: List[Edge], current_node: str):
    # Implement your generate function here
    # Replace the following example with your actual implementation

    # new_nodes = [{"id": "new-node-1", "type": "textUpdater", "position": {"x": 0, "y": 100}, "data": {"value": 2}, "width": 70, "height": 49, "selected": False, "dragging": False}]
    # new_edges = [{"id": "new-edge-1", "source": "node-1", "target": "new-node-1"}]

    node_to_append = None
    for node in nodes:
        if node.id == current_node:
            node_to_append = node

    # may not need node to append if we tell chatgpt to just make edges for node with id xyz
    # returns all the nodes and edges, with the prompted new node with edges as well, as a json formatted string. Need to use jsonify to turn into a pydict
    result = message_chatGPT(
        label=node_to_append.data["label"],
        return_data_as_json_string=True,
        existing_nodes=str(nodes),
        existing_edges=str(edges),
        current_node_id=current_node,
    )
    # result.replace("\n", "") # remove new line chars that will cause to fail
    return result

    # return {"nodes": new_nodes, "edges": new_edges}


@app.get("/")
def greeting():
    return "the app is running"


@app.post("/generate")
# removed the input data and prompt parameters as i didn't know to post them
async def generate_endpoint(input_data: InputData):
    try:
        result = generate(input_data.nodes, input_data.edges,
                          input_data.current_node)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/test")
def read():
    return "test works"


@app.get("/unittesting_test_connection")
def reply():
    return "The unit test file connected to the fastapi server as expected"
