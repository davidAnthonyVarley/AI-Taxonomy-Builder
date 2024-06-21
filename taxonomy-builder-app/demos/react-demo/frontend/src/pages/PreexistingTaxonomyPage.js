import DragAndDropSidebar from "../components/DragAndDropSidebar";
import React, { useState } from "react";
import "../css/PreexistingTaxonomyPage.css";
import UniverseTaxonomy from "../components/UniverseTaxonomy"
import TechTaxonomy from "../components/TechTaxonomy"

const PreexistingTaxonomyPage = () => {
  const [taxonomyText, setTaxonomyText] = useState("");
  const [dragOver, setDragOver] = useState(false);
  const [showUniverseTaxonomy, setShowUniverseTaxonomy] = useState(false);
  const [showTechTaxonomy, setShowTechTaxonomy] = useState(false);

  const handleDrop = (event) => {
    event.preventDefault();
    const text = event.dataTransfer.getData("text");
    setTaxonomyText(`${text}`); // load bearing text display
    setDragOver(false);
    
    if (text === "Universe") { 
      setShowUniverseTaxonomy(true);
    }
    else if (text === "Technology") {
      setShowTechTaxonomy(true); // added functionality for technology tax
    }
  };

  const handleDragOver = (event) => {
    event.preventDefault();
    setDragOver(true);
  };

  const handleDragLeave = () => {
    setDragOver(false);
  };

  return (
    <div className="preexisting-taxonomy-page-container">
      <DragAndDropSidebar />
      <div
        className={`preexisting-taxonomy-page-content ${dragOver ? "drag-over" : ""}`}
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
      >
        {taxonomyText.includes("Universe") && <UniverseTaxonomy />}
        {taxonomyText.includes("Technology") && <TechTaxonomy />}
      </div>
    </div>
  );  
};

export default PreexistingTaxonomyPage;
