import React from "react";
import "../css/MeetTeamPage.css";
import group_photo from "../images/Group Photo.jpg";

const MeetTeamPage = () => {
  return (
    <div className="pageContainer">
      <div class="container-1">
        <img
          src={group_photo}
          class="image"
          height={700}
          width={1245}
          alt=""
        ></img>
        <div class="overlay">
          <div class="text">Our Lovely Team :D</div>
        </div>
      </div>
      <br></br>
      <h2>3rd Years</h2> <br></br> <br></br>
      <div class="container">
        <div
          className="box box-1"
          style={{ "--img": `url(${require("../images/Ross.jpg")})` }}
          data-text="Ross - Team Lead"
        ></div>
        <div
          className="box box-2"
          style={{ "--img": `url(${require("../images/Bill.jpg")})` }}
          data-text="Bill - Data Science Lead"
        ></div>
        <div
          className="box box-3"
          style={{ "--img": `url(${require("../images/Martha.jpg")})` }}
          data-text="Martha - Documentation"
        ></div>
        <div
          className="box box-4"
          style={{ "--img": `url(${require("../images/Xiyuan.jpg")})` }}
          data-text="Xiyuan - Frontend Lead"
        ></div>
        <div
          className="box box-5"
          style={{ "--img": `url(${require("../images/Cian.jpg")})` }}
          data-text="Cian - Backend Lead"
        ></div>
      </div>
      <br></br>
      <br></br>
      <h2>2nd Years</h2>
      <br></br>
      <br></br>
      <div class="container">
        <div
          className="box box-6"
          style={{ "--img": `url(${require("../images/Scott.png")})` }}
          data-text="Scott - Data Science Dev"
        ></div>
        <div
          className="box box-7"
          style={{ "--img": `url(${require("../images/Madalina.jpg")})` }}
          data-text="Madalina - Frontend Dev"
        ></div>
        <div
          className="box box-8"
          style={{ "--img": `url(${require("../images/Brian.jpg")})` }}
          data-text="Brian - Frontend Dev"
        ></div>
        <div
          className="box box-9"
          style={{ "--img": `url(${require("../images/David.jpg")})` }}
          data-text="David - Backend Dev"
        ></div>
        <div
          className="box box-10"
          style={{ "--img": `url(${require("../images/Norbert.jpg")})` }}
          data-text="Norbert - Backend Dev"
        ></div>
        <div
          className="box box-11"
          style={{ "--img": `url(${require("../images/Kyle.jpg")})` }}
          data-text="Kyle - Backend Dev"
        ></div>
      </div>
    </div>
  );
};

export default MeetTeamPage;
