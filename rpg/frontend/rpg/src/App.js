import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Characters from './characters/characters';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to the Character Explorer powered by Django-GraphQL/REST-React</h1>
        </header>
        <p className="App-intro">
          Please enjoy...
        </p>
        <Characters />
      </div>
    );
  }
}

export default App;
