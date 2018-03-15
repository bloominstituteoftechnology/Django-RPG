import React, { Component } from 'react';
import '../App.css';
// import logo from '../logo.svg';

import { gql } from 'apollo-boost';
import { Query } from 'react-apollo';

const GET_CHARCTERS = gql`
  query {
    characters {
      name
      hp
    }
  }
`

class Characters extends Component {
	render() {
		return (
			<div className="Characters">
				<header className="Characters-header">
					{/* <img src={logo} className="Characters-logo" alt="logo" /> */}
					<h1 className="Characters-title">Welcome to React Character Page</h1>
				</header>
				<p className="Characters-intro">Character Page!</p>
				<Query query={GET_CHARCTERS}>
					{({ loading, error, data }) => {
						if (loading) return <div>Loading...</div>;
						if (error) return <div>Error :(</div>;
						console.log('DATA', data);
						return <p>{data.characters.name} </p>;
					}}
				</Query>
			</div>
		);
	}
}

export default Characters;
