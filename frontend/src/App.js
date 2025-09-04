import React from "react";
import Profile from "./components/Profile";
import Projects from "./components/Projects";
import Search from "./components/Search";
import Skills from "./components/Skills";

function App() {
  return (
    <div style={{ fontFamily: "Arial, sans-serif", margin: "20px" }}>
      <header style={{ background: "#282c34", padding: "15px", color: "white" }}>
        <h1>Me-API Playground</h1>
        <nav>
          <a href="#profile" style={{ margin: "0 10px", color: "white" }}>Profile</a>
          <a href="#skills" style={{ margin: "0 10px", color: "white" }}>Skills</a>
          <a href="#projects" style={{ margin: "0 10px", color: "white" }}>Projects</a>
          <a href="#search" style={{ margin: "0 10px", color: "white" }}>Search</a>
        </nav>
      </header>

      <section id="profile"><Profile /></section>
      <hr />
      <section id="skills"><Skills /></section>
      <hr />
      <section id="projects"><Projects /></section>
      <hr />
      <section id="search"><Search /></section>
    </div>
  );
}



export default App;
