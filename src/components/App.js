import React, { Component } from 'react';
// import Logos from './Logos';
import CharactersList from './CharactersList';
import '../styles/App.css';

class App extends Component {
  render() {
    return (
      // <Logos />
      <div>
        Hello!<br />
        Django / GraphQL Backend with React Front-end!<br /><br />
        <CharactersList />
      </div>
    );
  }
}

export default App;
