import React from 'react';
import { Link } from 'react-router-dom';
import './Menu.css';

const Menu = () => (
  <nav className="menu">
    <ul>
      <li><Link to="/">Home</Link></li>
      <li><Link to="/projects">Projects</Link></li>
      <li><Link to="/tennis">Tennis</Link></li>
      <li><Link to="/about">About</Link></li>
    </ul>
  </nav>
);

export default Menu;