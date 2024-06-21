import json
from pydantic import BaseModel, Field, model_validator, FieldValidationInfo
from typing import List, Optional
import instructor
from openai import OpenAI
MODEL = "gpt-3.5-turbo-0125"


client = instructor.patch(OpenAI(api_key="sk-"))


class Position(BaseModel):
    x: int = 0
    y: int = 0


class Data(BaseModel):
    name: str = Field(description="The name of the node generated")
    description: str = Field(
        description="A breif one sentence description of the node that was just generated"
    )


class Node(BaseModel):
    id: int = 0
    data: Data = Field(
        description="Data class containing the node's name and description"
    )
    position: Position = Position(x=0, y=0)


class Edge(BaseModel):
    id: int
    source: int
    target: int
    animated: bool = True


class Nodes(BaseModel):
    nodes: List["Node"] = []


class Taxonomy(BaseModel):
    nodes: List["Node"]
    edges: List["Edge"] = []
    currentNode: int

    def generate_step(self):
        expand_on = self.findNode(self.currentNode)
        child_nodes = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": f"""You are an iterative taxonomy builder.
                    You are given the current state of the taxonomy and a parent node on which to expand. 
                    You should create the next level of child nodes for the taxonomy from the given parent node. 
                    Do not procide any duplcates, and all child nodes must be a subcategory of the parent node.
                    return a list of the next children in the list nodes. You are to generate the name and description
                    field of the data field for each child node please.
                    """,
                },
                {
                    "role": "user",
                    "content": f"""Generate the child nodes for parent node {expand_on.data}""",
                },
                {
                    "role": "user",
                    "content": f"""Here is the current state of the taxonomy:
                    {self.model_dump_json(indent=2)}""",
                    # if cur_state is not None else expand_on.data
                },
            ],
            response_model=Nodes,
        )
        self.expand_nodeList(expand_on=expand_on, child_nodes=child_nodes)
        return child_nodes

    def expand_nodeList(self, expand_on: Node, child_nodes: Nodes):
        firstChildId = self.findMaxNodeId() + 1
        for enumeration, node in enumerate(child_nodes.nodes):
            node.id = firstChildId + enumeration
            newEdge = Edge(id=node.id, source=expand_on.id, target=node.id)
            self.edges.append(newEdge)
            self.nodes.append(node)

    def findMaxNodeId(self) -> int:
        maxId = 0
        for node in self.nodes:
            if node.id > maxId:
                maxId = node.id
        return maxId

    def findNode(self, id: int) -> Node:
        for node in self.nodes:
            if node.id == id:
                return node


def jsonInputHandler() -> Taxonomy:
    with open("sampleDataInput.json", "r") as read_file:
        data = read_file.read()
    inputTaxonomy = Taxonomy.model_validate_json(data)
    return inputTaxonomy


taxonomy = jsonInputHandler()
taxonomy.generate_step()
print(taxonomy.model_dump_json(indent=2))


# input_Parent = Node(id=4, data=Data(name="frogs", description="The species frogs")) #id is a string -> convert
# nodes : List['Node'] = []
# nodes.append(input_Parent)
# taxonomy = Taxonomy(nodes=nodes, currentNode=0)
# childNodes = taxonomy.generate_step(input_Parent, None)
# taxonomy.expand_nodeList(input_Parent, childNodes)
# print(taxonomy.model_dump_json(indent=2))
