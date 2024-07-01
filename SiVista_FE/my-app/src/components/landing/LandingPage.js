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
          <button> Promotional banners</button>
        </div>
        <div className="sub-container-2">
          <button>Lists of running jobs</button>
        </div>
        <div className="sub-container-3">
          <button>Create projects</button>
        </div>
        <div className="sub-container-4">
          <button>View projects/jobs</button>
        </div>
      </div>
    </div>
  );
};
export default LandingPage;