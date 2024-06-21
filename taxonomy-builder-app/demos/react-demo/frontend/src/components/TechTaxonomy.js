import React, { useCallback } from 'react';
import ReactFlow, {
  ReactFlowProvider,
  useNodesState,
  useEdgesState,
  addEdge,
  Background,
  BackgroundVariant,
  Controls
} from 'reactflow';
import 'reactflow/dist/style.css';
import TextUpdaterNode from "./TextUpdaterNode.js";
import techData from '../JSON/tech-short.json';
import '../css/CustomNode.css';

const rfStyle = {
  backgroundColor: "#0c0032",
};

const Flow = () => {
  const [nodes, setNodes, onNodesChange] = useNodesState(techData.nodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(techData.edges);
  const onConnect = useCallback((params) => setEdges((els) => addEdge(params, els)), []);

  return (
    <div style={{ width: "2000px", height: "750px", position: "relative" }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        fitView
        style={rfStyle}
        nodeTypes={{ textUpdater: TextUpdaterNode }}
      >
        <Background variant={BackgroundVariant.Dots} />
        <Controls />
      </ReactFlow>
    </div>
  );
};

const TechTaxonomy = () => {
  return (
    <ReactFlowProvider>
      <Flow />
    </ReactFlowProvider>
  );
}

export default TechTaxonomy;
