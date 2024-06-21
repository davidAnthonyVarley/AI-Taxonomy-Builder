# easy access to chatgpt 3.5 api
import openai
from json import loads, dump
import sys

from dotenv import load_dotenv
import os

# Load environment variables from .env file in the same directory
load_dotenv()
# import requests

openai_key = os.getenv("API_KEY")


# if frontend wants to use chatgpt API, use this text_presentation = 0, with
# text_presentation = 0   meaning that you will get a human-readable response from chatgpt
# text_presentation = 1   meaning that you will get the data in the form of a python dictionary


def message_chatGPT(
    label=None,
    return_data_as_json_string=False,
    existing_nodes=None,
    existing_edges=None,
    current_node_id=None,
):

    existing_messages = []
    structure = ""
    # if == False, no need to change anything
    if return_data_as_json_string == True:

        # ' dont add any notes ' means dont add a concluding statement, as AI usually do.

        # structure = 'You are a taxonomy builder. Your job is to take a prompt from the user and to generate a classification tree based on it. The tree must be generated SPECIFICALLY in the following JSON format:```{"*user prompt*": [{"category": "your catgeory name here", "subcategories": [{"category": "your catgeory name here", "subcategories": [...]}...]}...]}}```You must ensure you always generate data in this exact format. You must always generate some form of taxonomy. PLEASE DO NOT GENERATE DATA IN ANY OTHER FORMAT. With this in mind, please generate a taxonomy for the following prompt: '

        # NEW STRUCTURE PROVIDED BY ROSS
        structure = (
            '''
        You are a taxonomy builder. Your directive is to take an existing taxonomy (or classification tree) as well as an existing node from that taxonomy and produce several new nodes and edges in the taxononmy. The taxonomy takes the following format: 
            ```json
            {
            nodes: [
            {
            "id": str,
            "type": "textUpdater",
            "data": {
            "value": str
            },
            "position": {
            "x": int,
            "y": int
            },
            "width": int,
            "height": int,
            "dragging": False,
            "selected": False
            },
            ...
            ],
            "edges": [
            {
            "id": str,
            "source": str,
            "target": str
            },
            ...
            ]
            ```
        You must generate a JSON object of the same form containing only the nodes to be added to the existing taxonomy. You must create at least 3 new nodes, with edges, each of which having a source at the source node provided, and a target at one of the new nodes. You MUST ensure to generate both nodes and edges. The "label" of each new node must be some subcategory of the label of the parent node.  Data must be generated in this format. DO NOT GENERATE DATA IN ANY OTHER FORMAT. Where 3 relevant nodes cannot be generated, only generate as many nodes as contain relevant subcategories. 

        With this in mind, generate new nodes based off of the prompt "'''
            + label
            + '''", with a source node id of "'''
            + current_node_id
            + """" and the following existing taxonomy: 
            ```"""
            + str({"nodes": existing_nodes, "edges": existing_edges})
            + """```"""
        )

    # store the response
    existing_messages.append({"role": "user", "content": structure})

    # Set API key
    openai.api_key = openai_key

    # Make the request to OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=existing_messages
    )

    # strip away padding we dont need
    content = response.choices[0].message.content
    content_json = loads(content)
    return content_json


# message_chatGPT() end


# this will return a dictionary with attributes. the frontend should not be calling this
def store_json_as_python_dictionary(content):
    # store data into d3 tree node, ie, nested dicts
    # initialise node
    py_dict = loads(content)
    return py_dict


# store_as_py_dict() end


def json_to_string(filepath):

    with open(filepath, "r") as file:
        return file.read()


def write_to_json(filepath, data):

    with open(filepath, "w") as file:
        dump(data, file)


# used to store chatgpt response
def store_content_as_dataset(content):

    # open the test dataseet file and write the chatgpt response into it
    with open("test_query_dataset.txt", "w") as file:
        file.write(content)


# store_content_as_dataset() end


# print("cmd line prompt ", prompt )
