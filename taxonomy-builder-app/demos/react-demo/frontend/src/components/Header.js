import React, { useState } from "react";
import "../css/Header.css";
import DrawerButton from "./DrawerButton";

const Header = ({ onSidebarToggle }) => {
  const [isDrawerOpen, setIsDrawerOpen] = useState(false);

  const handleDrawerToggle = () => {
    setIsDrawerOpen(!isDrawerOpen);
    onSidebarToggle();
  };

  return (
    <header>
      <DrawerButton onClick={handleDrawerToggle} />
      <h1>Interactive Taxonomy Builder</h1>
      {/* Add any other header content */}
    </header>
  );
};

export default Header;
