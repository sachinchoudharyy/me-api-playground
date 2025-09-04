import React, { useEffect, useState } from "react";
import { getSkills } from "../api";

function Skills() {
  const [skills, setSkills] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    getSkills()
      .then(res => {
        console.log("Skills API response:", res.data);
        setSkills(res.data || []);
      })
      .catch(err => {
        console.error("Skills fetch failed:", err);
        setError(err.message || "Failed to load skills");
      });
  }, []);

  if (error) return <p style={{ color: "red" }}>Skills error: {error}</p>;
  if (!skills.length) return <p>No skills found.</p>;

  return (
    <div>
      <h2>Skills</h2>
      <div style={{ display: "flex", flexWrap: "wrap", gap: 10 }}>
        {skills.map((s, i) => (
          <span key={i} style={{ padding: "8px 12px", background: "#eee", borderRadius: 8 }}>
            {s.name}{s.level ? ` (${s.level})` : ""}
          </span>
        ))}
      </div>
    </div>
  );
}

export default Skills;
