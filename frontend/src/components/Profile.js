import React, { useEffect, useState } from "react";
import { getProfile } from "../api";

function Profile() {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    getProfile().then((res) => setProfile(res.data));
  }, []);

  if (!profile) return <p>Loading profile...</p>;

  return (
    <div>
      <h2>{profile.name}</h2>
      <p>Email: {profile.email}</p>
      <p>Education: {profile.education}</p>
      <p>
        <a href={profile.github} target="_blank" rel="noreferrer">GitHub</a> |{" "}
        <a href={profile.linkedin} target="_blank" rel="noreferrer">LinkedIn</a> |{" "}
        <a href={profile.portfolio} target="_blank" rel="noreferrer">Portfolio</a>
      </p>
    </div>
  );
}

export default Profile;
