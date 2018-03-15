import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

import DjangoCSRFToken from 'django-react-csrftoken';
import { ApolloProvider } from 'react-apollo'
import { ApolloClient, HttpLink, InMemoryCache } from 'apollo-client-preset'

const cache = new InMemoryCache();

const httplink = new HttpLink({
	uri: 'http://127.0.0.1:8000/graphql/',
	credentials: 'include',
	headers: {
		// authorization: 'bearer token',
		// 'X-CSRF-Token': DjangoCSRFToken
	}
});

const client = new ApolloClient({
	cache,
	link: httplink
});

// const ApolloApp = AppComponent => (
// 	<ApolloProvider client={client}>
// 		<AppComponent />
// 	</ApolloProvider>
// );

ReactDOM.render(
	<ApolloProvider client={client}>
		<App />
	</ApolloProvider>,
	document.getElementById('root')
);
registerServiceWorker();
