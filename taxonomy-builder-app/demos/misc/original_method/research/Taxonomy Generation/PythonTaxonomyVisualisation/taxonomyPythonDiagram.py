from openai import OpenAI
from diagrams import Diagram, Cluster, Edge

client = OpenAI(api_key="PUTINYOUROWNAPIKEY!")
inputPrompt = """
    Create a Python snyppit that will make the first three subcatogories as variables of a animal species taxonomy
    It will then print out those three variables
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a python code generator"},
        {"role": "user", "content": inputPrompt},
    ],
    max_tokens=500,
)

generated_code = response.choices[0].message.content
output_file_path = "generated_diagram_code.py"
with open(output_file_path, "w") as output_file:
    output_file.write(generated_code)
exec(open(output_file_path).read())
print(generated_code)
