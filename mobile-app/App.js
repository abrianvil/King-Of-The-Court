import { StatusBar } from 'expo-status-bar';
import { Provider, connect } from 'react-redux';
import configureStore from './src/store';
import { StyleSheet, Text, View } from 'react-native';

const store = configureStore()

export default function App() {
  return (
    <Provider store={store}>
      <View style={styles.container}>
        <Text>Open up App.js to start working on your app!</Text>
        <Text>this is a test</Text>
        <StatusBar style="auto" />
      </View>
    </Provider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});


// const mapStateToProps = (state) => {
//   return {
//     store: state,
//   };
// };

// export const test= connect(mapStateToProps, { store })(App);
