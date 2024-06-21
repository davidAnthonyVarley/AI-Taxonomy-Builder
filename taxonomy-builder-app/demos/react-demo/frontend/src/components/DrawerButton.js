import React, { useState } from "react";
import "../css/DrawerButton.css";

const DrawerButton = ({ onClick }) => {
  const [isOpen, setIsOpen] = useState(false);

  const handleClick = () => {
    setIsOpen(!isOpen);
    onClick(); // If you want to propagate the click event, you can call onClick here
  };

  return (
    <button onClick={handleClick} className="button">
      <div className={`nav-toggle ${isOpen ? "open" : ""}`}>
        <span className="bar"></span>
        <span className="bar"></span>
        <span className="bar"></span>
      </div>
    </button>
  );
};

export default DrawerButton;
