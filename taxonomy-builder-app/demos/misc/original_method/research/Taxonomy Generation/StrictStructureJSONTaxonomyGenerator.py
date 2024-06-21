from openai import OpenAI
import instructor
from pydantic import BaseModel, Field, model_validator, FieldValidationInfo
from typing import List, Optional


taxonomy = input("Taxonomy to be generated: ")

client = instructor.patch(OpenAI(api_key="sk-"))
# inputPrompt = "Create a json file that will show a detailed "+ taxonomy +" taxonomy. Each layer of the hierarchy should be called a category and have a category name, description and hierarchy level "


class TaxonomyNode(BaseModel):
    name: str = Field(..., description="The subcategory name.")


class Validation(BaseModel):
    is_valid: bool
    error_message: str = Field(
        description="If this node isn't a valid subcategory, explain why."
    )


class Taxonomy(TaxonomyNode):
    parent_node: str
    child_nodes: Optional[List[TaxonomyNode]]

    def expand_node(self, expand_on_node: str):
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Create a list of subcategories from the parent node: {expand_on_node}?",
                },
            ],
            response_model=Taxonomy,
        )
        return resp

    json_data = read_json(file_path)
    current_state = Taxonomy(**json_data)

    @model_validator(mode="after")
    def validate_sources(self, info: FieldValidationInfo):
        # text_chunks = info.context.get("text_chunk", None)
        for node in self.child_nodes:
            resp = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": f"Is the node {node} actually a subcategory of: {self.parent_node}?",
                    },
                ],
                response_model=Validation,
            )

            if resp.is_valid:
                pass
            else:
                raise ValueError(
                    f"The child node {node} is not a valid subcategory of parent node {self.parent_node}"
                )

        return self


inputPrompt = "Generate a ontology about chocolate, where all child nodes are a subcategory of the parent node."
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_model=Taxonomy,
    messages=[
        {"role": "system", "content": "You are a json data generator"},
        {"role": "user", "content": inputPrompt},
    ],
    max_tokens=500,
)
response.expand_node()

assert isinstance(response, Taxonomy)
generated_code = response.json()
output_file_path = "generatedJSON.json"
with open(output_file_path, "w") as output_file:
    output_file.write(generated_code)
