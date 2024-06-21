import React, { useState } from 'react';
import './App.css';
import logo from './logo.svg';

function App() {
  const [darkMode, setDarkMode] = useState(false);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  return (
    <div className={`App ${darkMode ? 'dark' : ''}`}>
      <header className="App-header">
        <h1>React Dark Mode Test</h1>
      </header>
      <main>
        <button onClick={toggleDarkMode}>
          Switch to {darkMode ? 'Day' : 'Night'} Mode
        </button>
        <div className="logo-container">
          <img src={logo} alt="Logo" className="logo" /> {}
        </div>
      </main>
      <footer className="App-footer">
        <p>© Thank you for your consideration</p>
      </footer>
    </div>
  );
}

export default App;
