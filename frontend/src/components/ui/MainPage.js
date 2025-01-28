import React, { useEffect } from 'react';
import './MainPage.css';

const MainPage = () => {
  useEffect(() => {
    const handleScroll = () => {
      const timelineItems = document.querySelectorAll('.timeline-item');
      timelineItems.forEach(item => {
        const rect = item.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
          item.classList.add('visible');
        } else {
          item.classList.remove('visible');
        }
      });
    };

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Initial check

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <div className="main-page">
      <header className="main-header">
        <h1>Welcome to My Personal Website</h1>
        <p>Your one-stop destination for all things about me.</p>
      </header>
      <section className="career-path">
        <h2>Career Path</h2>
        <div className="timeline">
          <div className="timeline-item">
            <div className="timeline-content">
              <h3>Huawei Mexico</h3>
              <p>Optical Telecom Solution Architect</p>
              <p>2022 - 2024</p>
            </div>
          </div>
          <div className="timeline-item">
            <div className="timeline-content">
              <h3>HaiRobotics</h3>
              <p>Software Product Manager</p>
              <p>2021</p>
            </div>
          </div>
          <div className="timeline-item">
            <div className="timeline-content">
              <h3>University of Toronto</h3>
              <p>Human-Centered Data Science</p>
              <p>2019 - 2021</p>
            </div>
          </div>
          <div className="timeline-item">
            <div className="timeline-content">
              <h3>University at Buffalo</h3>
              <p>Geographic Information Science</p>
              <p>2014 - 2018</p>
            </div>
          </div>
        </div>
      </section>
      <section className="main-content">
        <div className="block">
          <h2>Latest Idea 1</h2>
          <p>Description of the latest idea 1.</p>
        </div>
        <div className="block">
          <h2>Latest Idea 2</h2>
          <p>Description of the latest idea 2.</p>
        </div>
        <div className="block">
          <h2>Latest Idea 3</h2>
          <p>Description of the latest idea 3.</p>
        </div>
      </section>
    </div>
  );
};

export default MainPage;