import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Menu from './components/ui/Menu';
import MainPage from './components/ui/MainPage';
import Projects from './components/ui/Projects';
import Tennis from './components/ui/Tennis';
import About from './components/ui/About';
import GenerateText from './components/GenerateText';
import TrainModel from './components/TrainModel';
import TherapyChat from './components/TherapyChat';

const App = () => (
  <Router>
    <div className="font-sans">
      <Menu />
      <main className="container mx-auto mt-10">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/projects" element={<Projects />} />
          <Route path="/tennis" element={<Tennis />} />
          <Route path="/about" element={<About />} />
          <Route path="/generate" element={<GenerateText />} />
          <Route path="/train" element={<TrainModel />} />
          <Route path="/therapy" element={<TherapyChat />} />
        </Routes>
      </main>
    </div>
  </Router>
);

export default App;