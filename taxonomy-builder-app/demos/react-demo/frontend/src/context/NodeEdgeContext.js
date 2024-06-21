import React, { createContext, useReducer, useContext } from "react";

// Initial state
const initialState = {
  nodes: [
    {
      id: "node-1",
      type: "textUpdater",
      position: { x: 0, y: 0 },
      data: { label: "Enter Initial Value" },
    },
  ],
  edges: [],
};

// Reducer function
const reducer = (state, action) => {
  switch (action.type) {
    case "SET_STATE":
      return action.payload;
    case "ADD_NODE":
      return {
        ...state,
        nodes: [...state.nodes, action.payload],
      };
    case "ADD_EDGE":
      return {
        ...state,
        edges: [...state.edges, action.payload],
      };
    case "DELETE_NODE":
      return {
        ...state,
        nodes: state.nodes.filter((node) => node.id !== action.payload),
        edges: state.edges.filter(
          (edge) =>
            edge.source !== action.payload && edge.target !== action.payload,
        ),
      };

    case "UPDATE_NODES":
      return {
        ...state,
        nodes: action.payload,
      };

    case "UPDATE_EDGES":
      return {
        ...state,
        edges: action.payload,
      };

    case "UPDATE_NODE_VALUE":
      return {
        ...state,
        nodes: state.nodes.map((node) =>
          node.id === action.payload.id
            ? { ...node, data: { ...node.data, label: action.payload.label } }
            : node,
        ),
      };
    default:
      return state;
  }
};

// Create context
const NodeEdgeContext = createContext();

// Provider component
const NodeEdgeProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <NodeEdgeContext.Provider value={{ state, dispatch }}>
      {children}
    </NodeEdgeContext.Provider>
  );
};

// Custom hook to use the context
const useNodeEdgeContext = () => {
  const context = useContext(NodeEdgeContext);
  if (!context) {
    throw new Error("useNodeContext must be used within a NodeProvider");
  }
  return context;
};

export { NodeEdgeProvider, useNodeEdgeContext };
