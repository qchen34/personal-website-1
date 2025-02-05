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

    // 加载 Twitter widget
    const script = document.createElement("script");
    script.src = "https://platform.twitter.com/widgets.js";
    script.async = true;
    document.body.appendChild(script);

    return () => {
      window.removeEventListener('scroll', handleScroll);
      document.body.removeChild(script);
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
      <section className="twitter-section">
        <h2>Latest Tweets</h2>
        <div className="twitter-timeline-container">
          <a 
            className="twitter-timeline" 
            data-height="600"
            data-theme="light"
            href="https://twitter.com/CxrisChen34">
            Loading Tweets...
          </a>
        </div>
      </section>
      <footer className="main-footer">
        <div className="footer-content">
          <p>© 2024 Your Name. All rights reserved.</p>
          <div className="social-links">
            <a href="https://twitter.com/CxrisChen34" target="_blank" rel="noopener noreferrer">Twitter</a>
            <a href="https://linkedin.com/in/YOUR_LINKEDIN" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            <a href="https://github.com/YOUR_GITHUB" target="_blank" rel="noopener noreferrer">GitHub</a>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default MainPage;