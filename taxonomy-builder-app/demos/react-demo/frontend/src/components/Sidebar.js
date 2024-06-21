import React from "react";
import "../css/Sidebar.css";
import { IoIosCreate } from "react-icons/io";
import { TbHierarchy3 } from "react-icons/tb";
import { FaPeoplePulling, FaCircleNodes } from "react-icons/fa6";
import { Box, Link, Flex } from "@chakra-ui/react";
import { Link as RouterLink } from "react-router-dom";
import "../css/SidebarItems.css";
import { FaHome } from "react-icons/fa";

const Sidebar = ({ isOpen, toggle }) => {
  const sidebarItems = [
    {
      icon: <FaHome size={25} color="white" />,
      text: "Home Page",
      link: "/home",
    },
    {
      icon: <TbHierarchy3 size={25} color="white" />,
      text: "View Some Taxonomies",
      link: "/view",
    },
    {
      icon: <IoIosCreate size={25} color="white" />,
      text: "Create a Taxonomy",
      link: "/create",
    },
    {
      icon: <FaPeoplePulling size={25} color="white" />,
      text: "Meet the Team",
      link: "/team",
    },
    {
      icon: <FaCircleNodes size={25} color="white" />,
      text: "React Flow Test",
      link: "/flow",
    },
  ];

  return (
    <div className={`sidebar ${isOpen ? "open" : ""}`}>
      {/* Add your sidebar content here */}
      {!isOpen && (
        <Flex className="flexContainer">
          {sidebarItems.map((item, index) => (
            <Link
              to={item.link || null}
              as={RouterLink}
              className="tooltipLink"
            >
              {item.icon}
              <Box className="tooltipBox">{item.text}</Box>
            </Link>
          ))}
        </Flex>
      )}
    </div>
  );
};

export default Sidebar;
