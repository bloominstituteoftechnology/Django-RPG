import React, { Component } from 'react';
import { graphql } from 'react-apollo'
import gql from 'graphql-tag'

import Characters from './Characters';
// import '../styles/CharactersList.css';

class CharactersList extends Component {
  render() {
    // 1
    if (this.props.feedQuery && this.props.feedQuery.loading) {
      return <div>Loading</div>
    };
  
    // 2
    if (this.props.feedQuery && this.props.feedQuery.error) {
      return <div>Error</div>
    };
  
    // 3
    const charactersToRender = this.props.feedQuery.allCharacters.edges;
  
    return (
      <div>{charactersToRender.map(data => <Characters key={data.id} data={data} />)}</div>
    )
  }
}

const FEED_QUERY = gql`
  # 2
  query FeedQuery {
    allCharacters{
      edges{
        node{
          name
          level
          hp
        }
      }
    }
  }
`

export default graphql(FEED_QUERY, { name: 'feedQuery' }) (CharactersList);

