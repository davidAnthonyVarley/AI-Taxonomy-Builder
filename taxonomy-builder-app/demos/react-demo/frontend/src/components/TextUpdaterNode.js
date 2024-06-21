import React, { useState, useCallback } from "react";
import { Handle, Position } from "reactflow";
import { FaCircleXmark, FaCirclePlus } from "react-icons/fa6";
import { useNodeEdgeContext } from "../context/NodeEdgeContext";
import { API_ENDPOINTS } from "../config/config";

function TextUpdaterNode(props) {
  const [isEditing, setIsEditing] = useState(false);
  const [editedValue, setEditedValue] = useState(props.data.label);
  const [isLoading, setIsLoading] = useState(false); // New state for loading

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
    <div className="text-updater-node">
      <Handle
        type="target"
        position={Position.Top}
        isConnectable={props.isConnectable}
      />
      <div className="label-container">
        {isEditing ? (
          <input
            value={editedValue}
            onChange={onTitleChange}
            onBlur={onTitleBlur}
            className="nodrag"
          />
        ) : (
          <label htmlFor="text" onClick={onTitleClick}>
            {editedValue}
          </label>
        )}
      </div>
      <Handle
        type="source"
        position={Position.Bottom}
        id="b"
        isConnectable={props.isConnectable}
      />
      <div className="button-container">
        <button className="buttons" onClick={onDeleteButtonClick}>
          <FaCircleXmark color="red" />
        </button>
        <button className="buttons" onClick={onStepButtonClick}>
          {isLoading ? (
            <div className="loading-circle" />
          ) : (
            <FaCirclePlus color="green" />
          )}
        </button>
      </div>
    </div>
  );
}

export default TextUpdaterNode;
