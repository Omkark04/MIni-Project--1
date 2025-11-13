// Home.jsx
import React, { useState } from 'react';
import '../styles/home.css';
import Navbar from '../components/Navabar';

function Home() {
  const [activeAccordion, setActiveAccordion] = useState(null);


  const stats = [
    { icon: "🎯", value: "97%", label: "Prediction Accuracy" },
    { icon: "👥", value: "25+", label: "Job Categories" },
    { icon: "📈", value: "50+", label: "Countries Covered" },
    { icon: "🏆", value: "Real-time", label: "Job Listings" }
  ];

  const features = [
    {
      icon: "🧠",
      title: "AI-Powered Matching",
      description: "Advanced machine learning algorithms analyze your skills to predict the perfect job role with 97% accuracy."
    },
    {
      icon: "🔍",
      title: "Real-Time Job Listings",
      description: "Get live job opportunities from LinkedIn, Naukri.com, and other top platforms directly to your dashboard."
    },
    {
      icon: "🛡️",
      title: "Secure & Private",
      description: "Your data is protected with JWT authentication and secure encryption protocols."
    },
    {
      icon: "✨",
      title: "Smart Recommendations",
      description: "Receive personalized job suggestions based on your education, experience, and skill set."
    }
  ];

  const faqs = [
    {
      q: "How does the job role prediction work?",
      a: "Our system uses a K-Neighbor Classifier with TF-IDF vectorization to analyze your skills, education, and experience. It compares your profile against 25 distinct job categories with 97% accuracy to predict the most suitable role for you."
    },
    {
      q: "What job categories are supported?",
      a: "We support 25+ categories including Data Science, Python Developer, Java Developer, DevOps, Business Analyst, Web Design, Blockchain, Automation Testing, SAP, HR, and many more across IT and non-IT domains."
    },
    {
      q: "How are job listings gathered?",
      a: "We use web scraping technology with Selenium and BeautifulSoup to collect real-time job openings from platforms like LinkedIn, ensuring you get the latest opportunities matching your predicted role."
    },
    {
      q: "Is my data secure?",
      a: "Absolutely! We use JWT authentication for secure login, PostgreSQL for reliable data storage, and follow industry-standard security practices to protect your information."
    },
    {
      q: "Which countries are covered?",
      a: "Our system suggests job openings across 50+ countries including USA, UK, Germany, Canada, India, Australia, Singapore, UAE, and many more."
    },
    {
      q: "Can I use this if I'm not in IT?",
      a: "Yes! While we cover extensive IT roles, we also support non-IT categories like Advocate, Civil Engineer, Mechanical Engineer, HR, Sales, Health and Fitness, and more."
    }
  ];

  return (
    <div className="home-container">
      <Navbar/>
      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-content">
          <div className="hero-badge">
            <span className="badge-icon">✨</span>
            <span>97% Prediction Accuracy</span>
          </div>
          
          <h1 className="hero-title">
            Find Your Perfect
            <span className="hero-title-gradient">Career Match</span>
          </h1>
          
          <p className="hero-description">
            Let AI analyze your skills and guide you to the job role that truly fits your potential. 
            Stop applying randomly, start applying smartly.
          </p>
          
          <div className="hero-buttons">
            <button className="hero-primary-btn">
              <span>Predict My Role</span>
              <span className="btn-arrow">→</span>
            </button>
            <button className="hero-secondary-btn">Watch Demo</button>
          </div>
        </div>

        <div className="floating-element floating-1"></div>
        <div className="floating-element floating-2"></div>
      </section>

      {/* Stats Section */}
      <section className="stats-section">
        <div className="stats-grid">
          {stats.map((stat, i) => (
            <div key={i} className="stat-card">
              <div className="stat-icon">{stat.icon}</div>
              <div className="stat-value">{stat.value}</div>
              <div className="stat-label">{stat.label}</div>
            </div>
          ))}
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="features-section">
        <div className="section-header1">
          <h2 className="section-title">Why Choose CareerMatch AI?</h2>
          <p className="section-subtitle">
            Powered by cutting-edge technology to transform your job search experience
          </p>
        </div>

        <div className="features-grid">
          {features.map((feature, i) => (
            <div key={i} className="feature-card">
              <div className="feature-icon">{feature.icon}</div>
              <h3 className="feature-title">{feature.title}</h3>
              <p className="feature-description">{feature.description}</p>
            </div>
          ))}
        </div>
      </section>

      {/* About Us Section */}
      <section id="about" className="about-section">
        <div className="about-container">
          <div className="section-header1">
            <h2 className="section-title">About Our Mission</h2>
            <p className="section-subtitle">Bridging the gap between talent and opportunity</p>
          </div>

          <div className="about-content">
            <div className="about-text">
              <p className="about-paragraph">
                Freshers often possess diverse skill sets but struggle to identify which job role best suits their profile. 
                Many end up applying for less suitable positions despite having stronger qualifications for higher-value roles.
              </p>
              
              <p className="about-paragraph">
                CareerMatch AI was born from this challenge. We developed an intelligent system that analyzes your skills, 
                education, and experience using machine learning to recommend the most relevant and rewarding career opportunities.
              </p>

              <div className="about-features">
                <div className="about-feature-item">
                  <span className="check-icon">✓</span>
                  <span>Built with React, Django, and PostgreSQL for reliability</span>
                </div>
                <div className="about-feature-item">
                  <span className="check-icon">✓</span>
                  <span>97% accuracy using K-Neighbor Classifier algorithm</span>
                </div>
                <div className="about-feature-item">
                  <span className="check-icon">✓</span>
                  <span>Real-time job scraping from top platforms</span>
                </div>
                <div className="about-feature-item">
                  <span className="check-icon">✓</span>
                  <span>Covers 25+ job categories across 50+ countries</span>
                </div>
              </div>
            </div>

            <div className="about-visual">
              <div className="about-card">
                <div className="about-card-item">
                  <div className="about-card-icon about-icon-1">🧠</div>
                  <div className="about-card-content">
                    <div className="about-card-title">Smart Analysis</div>
                    <div className="about-card-subtitle">ML-powered insights</div>
                  </div>
                </div>
                
                <div className="about-card-item">
                  <div className="about-card-icon about-icon-2">🎯</div>
                  <div className="about-card-content">
                    <div className="about-card-title">Precise Matching</div>
                    <div className="about-card-subtitle">97% accuracy rate</div>
                  </div>
                </div>
                
                <div className="about-card-item">
                  <div className="about-card-icon about-icon-3">📈</div>
                  <div className="about-card-content">
                    <div className="about-card-title">Career Growth</div>
                    <div className="about-card-subtitle">Continuous opportunities</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section id="faq" className="faq-section">
        <div className="faq-container">
          <div className="section-header1">
            <h2 className="section-title">Frequently Asked Questions</h2>
            <p className="section-subtitle">Everything you need to know about CareerMatch AI</p>
          </div>

          <div className="faq-list">
            {faqs.map((faq, i) => (
              <div key={i} className="faq-item">
                <button
                  onClick={() => setActiveAccordion(activeAccordion === i ? null : i)}
                  className="faq-question"
                >
                  <span className="faq-question-text">{faq.q}</span>
                  <span className={`faq-arrow ${activeAccordion === i ? 'faq-arrow-open' : ''}`}>
                    ▼
                  </span>
                </button>
                
                <div className={`faq-answer ${activeAccordion === i ? 'faq-answer-open' : ''}`}>
                  <div className="faq-answer-text">{faq.a}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="cta-section">
        <div className="cta-content">
          <h2 className="cta-title">Ready to Find Your Perfect Role?</h2>
          <p className="cta-description">
            Join thousands of job seekers who've discovered their ideal career path with AI-powered precision
          </p>
          <button className="cta-button">
            <span>Start Your Journey</span>
            <span className="btn-arrow">→</span>
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="footer">
        <div className="footer-content">
          <div className="footer-brand">
            <span className="footer-icon">⚡</span>
            <span className="footer-brand-text">CareerMatch AI</span>
          </div>
          <p className="footer-text">
            Developed by Omkar Kangule & Ketan Dhembre<br />
            Chh. Shahu College of Engineering | Dept. of AI & Data Science
          </p>
          <p className="footer-copyright">
            © 2025 CareerMatch AI. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}

export default Home;