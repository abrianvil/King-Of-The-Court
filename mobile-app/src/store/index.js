// import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
// import thunk from 'redux-thunk';
// import sessionReducer from './session'

// const rootReducer = combineReducers({
//   session: sessionReducer,
// });
// let enhancer;

// if (process.env.NODE_ENV === 'production') {
//   enhancer = applyMiddleware(thunk);
// } else {
//   const logger = require('redux-logger').default;
//   const composeEnhancers =
//     window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
//   enhancer = composeEnhancers(applyMiddleware(thunk, logger));
// }

// const configureStore = (preloadedState) => {
//   return createStore(rootReducer, preloadedState, enhancer);
// };

// export default configureStore;

import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import { Platform } from 'react-native';
import sessionReducer from './session';

const rootReducer = combineReducers({
  session: sessionReducer,
});

const middleware = [thunk];

if (process.env.NODE_ENV !== 'production' && Platform.OS === 'ios') {
  const { logger } = require('redux-logger');
  middleware.push(logger);
}

const enhancer = compose(applyMiddleware(...middleware));

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
