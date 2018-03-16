import React, { Component } from 'react';
import '../styles/Characters.css';

class Characters extends Component {
    render() {
      return (
        <div>
            Name: {this.props.data.node.name} | HP: {this.props.data.node.hp} | Level: {this.props.data.node.level}
        </div>
      )
    }
}

export default Characters;

