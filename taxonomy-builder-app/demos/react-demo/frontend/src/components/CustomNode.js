import React, { useState, useCallback } from "react";
import { Handle, Position } from "reactflow";
import { FaPlus, FaTimes } from "react-icons/fa";
import { useNodeEdgeContext } from "../context/NodeEdgeContext";
import "../css/CustomNode.css"; 
import { API_ENDPOINTS } from "../config/config";


function CustomNode(props) {
  const [isEditing, setIsEditing] = useState(false);
  const [editedValue, setEditedValue] = useState(props.data.label);
  const [isHovered, setIsHovered] = useState(false); // Track hover state
  const [isLoading, setIsLoading] = useState(false); // Track loading state
  const { state, dispatch } = useNodeEdgeContext();

  const onTitleClick = useCallback(() => {
    setIsEditing(true);
  }, []);

  const onTitleChange = useCallback((event) => {
    setEditedValue(event.target.value);
  }, []);

  const onTitleBlur = useCallback(() => {
    setIsEditing(false);
    dispatch({
      type: "UPDATE_NODE_VALUE",
      payload: { id: props.id, label: editedValue },
    });
  }, [dispatch, editedValue, props.id]);

  const onDeleteButtonClick = useCallback(() => {
    dispatch({ type: "DELETE_NODE", payload: props.id });
  }, [dispatch, props.id]);

  const onStepButtonClick = useCallback(async () => {
    setIsLoading(true); // Set loading state to true before fetch request

    try {
      const payload = JSON.stringify({
        nodes: state.nodes,
        edges: state.edges,
        current_node: props.id,
      });

      const response = await fetch(API_ENDPOINTS.GENERATE, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: payload,
      });

      if (!response.ok) {
        throw new Error("Failed to fetch data from server");
      }

      const result = await response.json();

      const { nodes, edges } = result;

      for (const node of nodes) {
        dispatch({ type: "ADD_NODE", payload: node });
      }

      for (const edge of edges) {
        dispatch({ type: "ADD_EDGE", payload: edge });
      }
    } catch (error) {
      console.error("Error:", error.message);
    } finally {
      setIsLoading(false); // Set loading state back to false after fetch request completes
    }
  }, [props.id, state.edges, state.nodes, dispatch]);

  return (
    <div 
      className="custom-node" 
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      <Handle
        type="target"
        position={Position.Top}
        isConnectable={props.isConnectable}
      />
      <div className="node-content">
        {isEditing ? (
          <input
            value={editedValue}
            onChange={onTitleChange}
            onBlur={onTitleBlur}
            autoFocus // Focus the input field when it appears
          />
        ) : (
          <span onClick={onTitleClick}>{editedValue}</span> // Changed label to span for better click handling
        )}
      </div>
      {isHovered && (
        <div className="node-controls">
          <button className="delete-button" onClick={onDeleteButtonClick}>
            <FaTimes />
          </button>
          <button className="add-button" onClick={onStepButtonClick}>
            {isLoading ? <div className="loading-circle" /> : <FaPlus />}
          </button>
        </div>
      )}
      <Handle
        type="source"
        position={Position.Bottom}
        id="b"
        isConnectable={props.isConnectable}
      />
    </div>
  );
}

export default CustomNode;
