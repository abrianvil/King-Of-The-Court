import { View, Text, StyleSheet, SafeAreaView, Button } from 'react-native'
import React from 'react'
import NavOptions from '../Components/NavOptions'
import { useNavigation } from '@react-navigation/native'

const HomeScreen = () => {

    const navigation = useNavigation()

    return (
        <SafeAreaView style={styles.container}>
            <Text>I am the HomeScreen</Text>
            <Button
                color="orange"
                title="Click Me"
                onPress={() => navigation.navigate('Navigation')}
                ></Button>
            {/* <NavOptions/> */}
        </SafeAreaView>
    )
}

export default HomeScreen;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
    },
})
