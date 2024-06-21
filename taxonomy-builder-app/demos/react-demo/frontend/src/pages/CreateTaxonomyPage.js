import React, { useCallback, useRef, useMemo } from 'react';
import ReactFlow, {
  applyEdgeChanges,
  applyNodeChanges,
  useReactFlow,
  ReactFlowProvider
} from 'reactflow';
import CustomNode from '../components/CustomNode.js'; 
import { useNodeEdgeContext } from '../context/NodeEdgeContext.js'; 
import styles from '../css/CreateTaxonomyPage.module.css';

const rfStyle = {
  backgroundColor: '#120136',
};

const Flow = () => {
  const reactFlowWrapper = useRef(null);
  const { state, dispatch } = useNodeEdgeContext(useNodeEdgeContext); 
  const { screenToFlowPosition } = useReactFlow();


  const nodeTypes = useMemo(() => ({
    textUpdater: CustomNode, 
  }), []);

  const onNodesChange = useCallback((changes) => {
    dispatch({ type: 'UPDATE_NODES', payload: applyNodeChanges(changes, state.nodes) });
  }, [state.nodes, dispatch]);

  const onEdgesChange = useCallback((changes) => {
    dispatch({ type: 'UPDATE_EDGES', payload: applyEdgeChanges(changes, state.edges) });
  }, [state.edges, dispatch]);

  const onConnect = useCallback((connection) => {
    dispatch({ type: 'ADD_EDGE', payload: { ...connection, id: `e${connection.source}-${connection.target}` } });
  }, [dispatch]);

  const onDoubleClick = useCallback((event) => {
    if (!event.target.closest('.react-flow__node')) {
      const flowPos = screenToFlowPosition({ x: event.clientX, y: event.clientY });
      dispatch({
        type: 'ADD_NODE',
        payload: {
          id: `node-${state.nodes.length + 1}`,
          type: 'textUpdater',
          position: flowPos,
          data: { label: 'New Node' },
        },
      });
    }
  }, [dispatch, screenToFlowPosition, state.nodes.length]);
  const initialNodeLabel = state.nodes[0]?.data?.label || "No initial value";

  return (
    <div className={styles.createTaxonomyPage}>
      <h2 className={styles.title}>{`${initialNodeLabel} Taxonomy`}</h2>
      <div style={{ width: '100vw', height: '100vh', position: 'relative' }} ref={reactFlowWrapper}>
        <ReactFlow
          nodes={state.nodes}
          edges={state.edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onConnect={onConnect}
          onDoubleClickCapture={onDoubleClick}
          nodeTypes={nodeTypes}
          fitView
          style={rfStyle}
        >
         
        </ReactFlow>
      </div>
    </div>
  );
};

const CreateTaxonomyPage = () => (
  <ReactFlowProvider>
    <Flow />
  </ReactFlowProvider>
);

export default CreateTaxonomyPage;

