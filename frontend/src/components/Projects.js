import React, { useEffect, useState } from "react";
import { getProjects } from "../api";

function Projects() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    getProjects().then((res) => setProjects(res.data));
  }, []);

  return (
    <div>
      <h2>Projects</h2>
      <ul>
        {projects.map((p, i) => (
          <li key={i}>
            <strong>{p.title}</strong> - {p.description}
            {p.link && (
              <>
                {" "} <a href={p.link} target="_blank" rel="noreferrer">View</a>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Projects;
