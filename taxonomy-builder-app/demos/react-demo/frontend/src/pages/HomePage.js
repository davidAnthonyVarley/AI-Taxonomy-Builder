import React from "react";
import welcome_img from "../images/WelcomeImage2.png";
import "../css/HomePage.css";

const HomePage = () => {
  return (
    <div className="container-home">
      <div className="container-box">
      <div className="container-intro">
        <div className="container-intro-text">
          <h1 style={{ fontSize: "2rem", fontWeight: "bold" }}>
            Welcome <br></br>to our <br></br>Interactive <br></br>Taxonomy <br></br>Builder
          </h1>
        </div>
        <div class="container-image">
          <img
          src={welcome_img}
          className="image"
          alt="Welcome"
          />
        </div>
      </div>
      </div>
      
      <div class="container-flex">
        <div class="left-section">
          <h2 class="header1">Understanding Taxonomy </h2>
          <div className="container-def">
            <p>
              Taxonomy is the practice of systematically organising things into categories. 
              It is most commonly associated with biology, however it's also used
              by librarians to sort books, by search engines 
              to find information quickly, and by businesses to organize their products.
            </p>
          </div>
        </div>
        <div class="middle-section">
          <h2 class="header2">How Does it Work?</h2>
          <div className="container-how">
            We developed our Interactive Taxonomy <br></br>system through the use of Artifical
            Intelligence. <br></br>By using the OpenAI API, we are able to call <br></br>GPT4 to provide 
            the taxonomy that the <br></br>user requests.
          </div>
        </div>
        <div class="right-section">
          <h2 class="header3">Getting Started</h2>
          <div className="container-tutorial">
            Click on the "Create a Taxonomy" section. <br></br>
            Input your prompt into the Taxonomy Builder. <br></br>
            Explore your prompt in a graph format. <br></br>
            Click on categories to expand further and enjoy!
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
