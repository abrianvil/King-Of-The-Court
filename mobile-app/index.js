import React from 'react';
import { Provider } from 'react-redux';
import { AppRegistry } from 'react-native';
import configureStore from './src/store';
import App from './App';

const store= configureStore()


const MyApp= ()=>(
    <Provider store={store}>
        <App store={store}/>
    </Provider>
);



AppRegistry.registerComponent('MyApp', ()=>MyApp)


const mapStateToProps = (state) => {
  return {
    store: state,
  };
};

export const test= connect(mapStateToProps, { store })(App);
