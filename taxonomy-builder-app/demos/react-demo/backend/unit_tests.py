import unittest

import requests
from typing import List

# from chatgpt_api import message_chatGPT
from json import loads

# this is very frustrating
"""
from pydantic import BaseModel




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

"""


def contains_node_id(nodes, node_id):
    node_to_append = None
    for node in nodes:
        if node["id"] == node_id:
            print(node["id"], " === ", node_id)
            node_to_append = node

    # if contains id, return true
    if node_to_append is None:
        return False
    else:
        return True


# Function to be tested
def add(a, b):
    return a + b


# Test case class
class TestAddFunction(unittest.TestCase):

    # print("generating json")
    # generated_json = message_chatGPT(label="types of bread")
    # print(generated_json)
    # json = loads(generated_json)

    # nodes = json['nodes']
    print("about to test connection")

    def check_connection_to_fastapi_server(self):
        print("testing connection")
        url = "http://localhost:8000/unittesting_test_connection/"
        response = requests.get(url)
        data = response.read()
        print(data)
        self.assertEquals(
            data, "The unit test file connected to the fastapi server as expected"
        )

    print("tested connection")

    def test_contains_node(self):

        nodes = [
            {
                "id": "node1",
                "type": "textUpdater",
                "data": {"value": "Node 1"},
                "position": {"x": 100, "y": 100},
                "width": 100,
                "height": 50,
                "dragging": False,
                "selected": False,
            },
            {
                "id": "node2",
                "type": "textUpdater",
                "data": {"value": "Node 2"},
                "position": {"x": 200, "y": 200},
                "width": 100,
                "height": 50,
                "dragging": False,
                "selected": False,
            },
        ]
        edges = [{"id": "edge1", "source": "node1", "target": "node2"}]

        node_id = "node1"
        self.assertEqual(contains_node_id(nodes, node_id), True)

    def test_doesnt_contain_node(self):

        nodes = [
            {
                "id": "node1",
                "type": "textUpdater",
                "data": {"value": "Node 1"},
                "position": {"x": 100, "y": 100},
                "width": 100,
                "height": 50,
                "dragging": False,
                "selected": False,
            },
            {
                "id": "node2",
                "type": "textUpdater",
                "data": {"value": "Node 2"},
                "position": {"x": 200, "y": 200},
                "width": 100,
                "height": 50,
                "dragging": False,
                "selected": False,
            },
        ]
        edges = [{"id": "edge1", "source": "node1", "target": "node2"}]

        node_id = "nodeNOTinLIST"
        # print("checking for false id")
        self.assertEqual(contains_node_id(nodes, node_id), False)

    # the next three are just to test that the unittest library works
    # dont remove them bc when your other code isn't working, this tells you that it isn't the unitttest library

    # Test method to check addition of two positive numbers
    def test_positive_numbers(self):
        self.assertEqual(add(3, 9), 8)

    def temper(self):
        self.assertEqual(1, 1)

    # Test method to check addition of a positive and a negative number
    def test_positive_and_negative_numbers(self):
        self.assertEqual(add(-3, 5), 2)

    # Test method to check addition of two negative numbers
    def test_negative_numbers(self):
        self.assertEqual(add(-3, -5), -8)


# Run tests


unittest.main()
