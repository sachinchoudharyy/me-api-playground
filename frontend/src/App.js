import React from "react";
import Profile from "./components/Profile";
import Projects from "./components/Projects";
import Search from "./components/Search";

function App() {
  return (
    <div style={{ margin: "20px", fontFamily: "Arial" }}>
      <h1>Me-API Playground</h1>
      <Profile />
      <hr />
      <Projects />
      <hr />
      <Search />
    </div>
  );
}

export default App;
