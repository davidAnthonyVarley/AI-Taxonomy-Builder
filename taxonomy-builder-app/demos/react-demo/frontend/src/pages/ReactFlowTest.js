import { useCallback, useRef, useMemo } from "react";
import ReactFlow, {
  ReactFlowProvider,
  Background,
  BackgroundVariant,
  applyEdgeChanges,
  applyNodeChanges,
  useReactFlow,
} from "reactflow";
import "reactflow/dist/style.css";
import TextUpdaterNode from "../components/TextUpdaterNode.js";
import "../css/text-updater-node.css";
import { useNodeEdgeContext } from "../context/NodeEdgeContext.js";

const rfStyle = {
  backgroundColor: "#B8CEFF",
};

const Flow = () => {
  const { state, dispatch } = useNodeEdgeContext();
  const { nodes, edges } = state;
  const reactFlowWrapper = useRef(null);
  const { screenToFlowPosition } = useReactFlow();

  const nodeTypes = useMemo(
    () => ({
      textUpdater: TextUpdaterNode,
    }),
    [],
  );

  const onNodesChange = useCallback(
    (changes) => {
      const updatedNodes = applyNodeChanges(changes, state.nodes);
      dispatch({ type: "UPDATE_NODES", payload: updatedNodes });
    },
    [state.nodes, dispatch],
  );

  const onEdgesChange = useCallback(
    (changes) => {
      const updatedEdges = applyEdgeChanges(changes, state.edges);
      dispatch({ type: "UPDATE_EDGES", payload: updatedEdges });
    },
    [state.edges, dispatch],
  );

  const onConnect = useCallback(
    (connection) => {
      const newEdge = {
        id: `edge-${connection.source}-${connection.target}`,
        source: connection.source,
        target: connection.target,
      };
      dispatch({ type: "ADD_EDGE", payload: newEdge });
    },
    [dispatch],
  );

  const onDoubleClick = useCallback(
    (event) => {
      // Check if the click target is not a node
      if (
        !event.target.closest(".react-flow__node") ||
        event.target.closest(".react-flow__node") === null
      ) {
        const newNode = {
          id: `node-${state.nodes.length + 1}`,
          type: "textUpdater",
          position: screenToFlowPosition({
            x: event.clientX - 70,
            y: event.clientY - 50,
          }),
          data: { label: "Enter Initial Value" },
          width: 70,
          height: 49,
          selected: false,
          dragging: false,
        };
        dispatch({ type: "ADD_NODE", payload: newNode });
      }
    },
    [state, dispatch, screenToFlowPosition],
  );

  return (
    <div
      style={{ width: "100vw", height: "100vh", position: "relative" }}
      ref={reactFlowWrapper}
    >
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        onDoubleClickCapture={onDoubleClick} // Add the onDoubleClick event handler
        nodeTypes={nodeTypes}
        fitView
        style={rfStyle}
      >
        <Background variant={BackgroundVariant.Dots} />
      </ReactFlow>
    </div>
  );
};

const ReactFlowTest = () => (
  <ReactFlowProvider>
    <Flow />
  </ReactFlowProvider>
);

export default ReactFlowTest;
