import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Navbar from "./components/Navbar";
import "./components/Navbar.css";
import Footer from "./components/Footer";
import "./components/Footer.css";
import "./App.css";

function App() {
  return (
    <div className="main-container">
      <Navbar />
      <div className="container inner-container">
        <h1>The Cyber Agent</h1>
        <h3>Play as a secret agent tasked with .... idk the story lol. </h3>
        <br></br>
        <div className="game-container">
          <iframe
            src={
              process.env.PUBLIC_URL +
              "/renpyGame/329Project-1.0-web/index.html"
            }
            name="The Cyber Agent"
            title="CyberAgent"
            width="100%"
            height="100%"
            frameborder="0"
            scrolling="no"
          >
            <p>There seems to have been an issue loading the game!</p>
          </iframe>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default App;
