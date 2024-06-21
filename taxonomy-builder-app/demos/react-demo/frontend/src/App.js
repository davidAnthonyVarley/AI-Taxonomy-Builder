import React, { useState } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import Sidebar from "./components/Sidebar";
import Header from "./components/Header";
import CreateTaxonomyPage from "./pages/CreateTaxonomyPage";
import PreexistingTaxonomyPage from "./pages/PreexistingTaxonomyPage";
import MeetTeamPage from "./pages/MeetTeamPage";
import ReactFlowTest from "./pages/ReactFlowTest";
import HomePage from "./pages/HomePage";
import "./css/App.css";
import { NodeEdgeProvider } from "./context/NodeEdgeContext";

const App = () => {
  const [isOpen, setIsOpen] = useState(true);

  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  return (
    <NodeEdgeProvider>
      <Router>
        <div className="App">
          <Header onSidebarToggle={toggleSidebar} />
          <div className="sidebar-and-main-content-area">
            <Sidebar isOpen={isOpen} toggle={toggleSidebar} />
            <div className="main-content">
              <Routes>
                {/* add pages here */}
                <Route path="/" element={<Navigate replace to="/home" />} />
                <Route path="/home" element={<HomePage />} />
                <Route path="/view" element={<PreexistingTaxonomyPage />} />
                <Route path="/create" element={<CreateTaxonomyPage />} />
                <Route path="/team" element={<MeetTeamPage />} />
                <Route path="/flow" element={<ReactFlowTest />} />
              </Routes>
            </div>
          </div>
        </div>
      </Router>
    </NodeEdgeProvider>
  );
};

export default App;
