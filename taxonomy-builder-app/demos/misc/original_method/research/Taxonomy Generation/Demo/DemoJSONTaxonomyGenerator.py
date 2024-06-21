from openai import OpenAI
from diagrams import Diagram, Cluster, Edge

taxonomy = input("Taxonomy to be generated: ")

client = OpenAI(api_key="sk-")
inputPrompt = (
    """
    "You are a taxonomy builder. Your job is to take a prompt from the user and to generate a taxonomy based on it. The taxonomy must be generate SPECIFICALLY in the following JSON format:

    {
    "taxonomy title": [
    {
    "category": "your catgeory name here", 
    "subcategories": [
    {
    "category": "your catgeory name here", 
    "subcategories": [
    ...
    ]
    }
    ...
    ]
    }
    ...
    ]
    }
    
You must ensure you always generate data in this exact format. If there is any concern about generation based on the data provided by the user prompt, please inform the user and tell them how they can modify their prompt to assist. 

PLEASE DO NOT GENERATE DATA IN ANY OTHER FORMAT"
DO NOT GENERATE ANYTHING OTHER THAN THE JSON

"""
    + "The user input prompt is "
    + taxonomy
    + " , with many different subcategories"
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a json taxonomy builder"},
        {"role": "user", "content": inputPrompt},
    ],
    max_tokens=500,
)

generated_code = response.choices[0].message.content
output_file_path = "generatedJSON.json"
with open(output_file_path, "w") as output_file:
    output_file.write(generated_code)
