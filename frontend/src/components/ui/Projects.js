import React from 'react';
import { Link } from 'react-router-dom';
import './Projects.css';

const Projects = () => {
  return (
    <div className="projects-page">
      <h1>Projects</h1>
      <div className="projects-grid">
        <div className="project-block">
          <Link to="/generate">
            <div className="project-content">
              <h2>Project 1: Generate Shakespeare text</h2>
              <p>Click to generate text</p>
            </div>
          </Link>
        </div>
        <div className="project-block">
          <div className="project-content">
            <h2>Project 2</h2>
            <p>Description of Project 2</p>
          </div>
        </div>
        <div className="project-block">
          <div className="project-content">
            <h2>Project 3</h2>
            <p>Description of Project 3</p>
          </div>
        </div>
        <div className="project-block">
          <div className="project-content">
            <h2>Project 4</h2>
            <p>Description of Project 4</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Projects;