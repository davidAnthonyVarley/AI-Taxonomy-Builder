import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import json
from chatgpt_api import send_prompt

st.set_page_config(page_title="Taxonomy Visualization",
                   page_icon="📊", layout="wide")

st.sidebar.success(
    "Feel free to explore the options above. Actual functionality will be added soon."
)


# Nodes and edges setup
def create_nodes_and_edges(data):
    nodes = []
    edges = []
    nodes.append(Node(id=1, label=next(iter(data)), size=25, shape="circle"))
    id_counter = 2

    def process_category(category, parent_id=1):
        nonlocal id_counter

        current_id = id_counter
        id_counter += 1

        nodes.append(
            Node(id=current_id,
                 label=category["category"], size=25, shape="circle")
        )

        if parent_id is not None:
            edges.append(
                Edge(source=parent_id,
                     label=category["category"], target=current_id)
            )

        for subcategory in category["subcategories"]:
            process_category(subcategory, current_id)

    for law_category in data[next(iter(data))]:
        process_category(law_category)

    return nodes, edges


# nodes, edges = create_nodes_and_edges(testdata)

# Config setup
config = Config(width=2000, height=600, directed=True,
                physics=False, hierarchical=True)

# Display the graph
# agraph(nodes=nodes, edges=edges, config=config)


def get_session_state(resource_path):
    state = st.session_state

    # Initialize user state if session doesn't exist
    if not state.get("INIT", False):
        state["my_input"] = ""

    state["INIT"] = True
    return state


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input the user prompt here",
                         st.session_state["my_input"])
st.session_state["my_input"] = my_input

submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    print("submit button hit")
    st.write("The user prompt entered is: ", my_input)

    taxonomy_as_text = send_prompt(my_input)
    # print("*")
    # print("*")
    # print("*")
    # print(taxonomy_as_text)
    # print("*")
    # print("*")
    # print("*")

    taxonomy_successfully_generated_as_json = False
    attempts = 0  # if it trys more than 10 times then stop trying

    # tests for demo:
    # types of corporate fraud
    # types of chocolate bar
    # feudal system

    # it doesn't always work the first time, so brute-force it until it works
    while (not taxonomy_successfully_generated_as_json) and (attempts < 10):
        try:
            output = json.loads(taxonomy_as_text)
            nodes, edges = create_nodes_and_edges(output)
            agraph(nodes=nodes, edges=edges, config=config)

            taxonomy_successfully_generated_as_json = True

        except Exception as e:
            print("Error in generating taxonomy: ", e)
            print("regenerating taxonomy, attempt number ", attempts)
            attempts += 1
            taxonomy_as_text = send_prompt(my_input)
            # keep on looping until success


def render_sidebar():
    taxonomy_options = ["Technology"]
    selected_taxonomy = st.sidebar.radio("Select a Taxonomy", taxonomy_options)
    st.sidebar.write(f"You selected: {selected_taxonomy}")
    return selected_taxonomy


selected_taxonomy = render_sidebar()

# # TODO


# def render_main(session_state):
#     my_input = st.text_input("Input the user prompt here", session_state["my_input"])
#     submit = st.button("Submit")
#     if submit:
#         session_state["my_input"] = my_input
#         st.write("The user prompt entered is: ", my_input)


# if __name__ == '__main__':
#     state = get_session_state()
#     render_main(state)
#     render_sidebar(state)
