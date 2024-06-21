import { Link } from "react-router-dom";
import { IoIosPlanet } from "react-icons/io";
import { FaPaw } from "react-icons/fa";
import { FaComputer } from "react-icons/fa6";
import "../css/DragAndDropSidebar.css";

const sidebarItems = [
  {
    icon: <IoIosPlanet size={25} />,
    text: "Universe",
    link: "/universe",
  },
  {
    icon: <FaPaw size={25} />,
    text: "Animal Kingdom",
    link: "/animal",
  },
  {
    icon: <FaComputer size={25} />,
    text: "Technology",
    link: "/technology",
  },
];

const DragAndDropSidebar = () => {
  const handleDragStart = (event, text) => {
    event.dataTransfer.setData("text", text);
  };

  return (
    <div className="dragAndDropSidebar">
      {sidebarItems.map((item, index) => (
        <Link
          key={index}
          to={item.link}
          className="sidebar-item"
          draggable
          onDragStart={(event) => handleDragStart(event, item.text)}
        >
          {item.icon}
          <span className="sidebar-text">{item.text}</span>
        </Link>
      ))}
    </div>
  );
};

export default DragAndDropSidebar;
