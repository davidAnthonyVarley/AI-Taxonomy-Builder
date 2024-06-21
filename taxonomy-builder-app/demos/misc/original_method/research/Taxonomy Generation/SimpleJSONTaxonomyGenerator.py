from openai import OpenAI
from diagrams import Diagram, Cluster, Edge

taxonomy = input("Taxonomy to be generated: ")

client = OpenAI(api_key="INSERTYOUROWNAPIKEY")
inputPrompt = "Create a json file that will a detailed " + taxonomy + " taxonomy "

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a json data generator"},
        {"role": "user", "content": inputPrompt},
    ],
    max_tokens=500,
)

generated_code = response.choices[0].message.content
output_file_path = "generatedJSON.json"
with open(output_file_path, "w") as output_file:
    output_file.write(generated_code)
