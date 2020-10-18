import React, { Component } from 'react'
import { View, Text, TouchableOpacity, TextInput, StyleSheet } from 'react-native'

class Inputs extends Component {
    state = {
        origin: "",
        destination: ""
    }
    handleOrigin = (text) => {
        this.setState({ origin: text })
    }
    handleDestination = (text) => {
        this.setState({ destination: text })
    }
    route = (origin, destination) => {
        alert('origin: ' + origin + ' destination: ' + destination)
    }
    render() {
        return (
            <View style = {styles.container}>
                <TextInput style = {styles.input}
                    ref = {origin => { this.origin = origin }}
                    color = "white"
                    underlineColorAndroid = "transparent"
                    placeholder = "Origin"
                    placeholderTextColor = "#9a73ef"
                    autoCapitalize = "none"
                    onChangeText = {this.handleOrigin}
                    clearButtonMode="always"/>
                <TextInput style = {styles.input}
                    ref = {destination => { this.destination = destination }}
                    color = "white"
                    underlineColorAndroid = "transparent"
                    placeholder = "Destination"
                    placeholderTextColor = "#9a73ef"
                    autoCapitalize = "none"
                    onChangeText = {this.handleDestination}
                    clearButtonMode="always"/>
                <TouchableOpacity
                    style = {styles.enterButton}
                    onPress = {
                        () => { this.route(this.state.origin, this.state.destination); this.origin.clear(); this.destination.clear(); }
                    }>
                <Text style = {styles.enterButtonText}> LET'S GO! </Text>
                </TouchableOpacity>
            </View>
        )
     }
  }
  export default Inputs
  
  const styles = StyleSheet.create({
    container: {
        paddingTop: 20,
        marginTop: 15,
        margin: 39
    },
    input: {
        marginRight: 15,
        marginLeft: 15,
        marginTop: 15,
        height: 40,
        borderColor: '#7a42f4',
        borderWidth: 1,
        borderBottomLeftRadius: 10,
        borderBottomRightRadius: 10,
        borderTopLeftRadius: 10,
        borderTopRightRadius: 10,
        padding: 10
    },
    enterButton: {
        backgroundColor: '#7a42f4',
        borderBottomLeftRadius: 10,
        borderBottomRightRadius: 10,
        borderTopLeftRadius: 10,
        borderTopRightRadius: 10,
        paddingTop: 10,
        padding: 5,
        margin: 15,
        height: 40,
        width: 85
    },
    enterButtonText:{
        color: 'white'
    }
})