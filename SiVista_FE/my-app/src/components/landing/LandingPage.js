import React from "react";
import User from "../../Assets/Images/user.png";
import Bell from "../../Assets/Images/bell.png";
import Logo from "../../Assets/Images/Logo.svg";
import "./LandingPage.css";
const LandingPage = () => {
  return (
    <div>
      <nav>
        <div className="logo">
          <img src={Logo} alt="logo" />
        </div>
        <div className="userId">
          <img src={Bell} alt="bell" />
          <img src={User} alt="user" />
        </div>
      </nav>
      <div className="container">
        <div className="sub-container-1">
          <h1>Promotional Banner</h1>
        </div>
        <div className="sub-container-2">
          <h1>Lists of running jobs</h1>
        </div>
        <div className="sub-container-3">
          <h1>Create projects</h1>
        </div>
        <div className="sub-container-4">
          <h1>View projects/jobs</h1>
        </div>
      </div>
    </div>
  );
};
export default LandingPage;