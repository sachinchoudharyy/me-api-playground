import React, { useState } from "react";
import { getProjects } from "../api";

function Search() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = () => {
    getProjects(query).then((res) => setResults(res.data));
  };

  return (
    <div>
      <h2>Search Projects by Skill</h2>
      <input
        type="text"
        placeholder="Enter skill (e.g., Python)"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>

      <ul>
        {results.map((p, i) => (
          <li key={i}>
            <strong>{p.title}</strong> - {p.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Search;
