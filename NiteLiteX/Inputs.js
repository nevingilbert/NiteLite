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
                    underlineColorAndroid = "transparent"
                    placeholder = "Origin"
                    placeholderTextColor = "#9a73ef"
                    autoCapitalize = "none"
                    onChangeText = {this.handleOrigin}/>
                <TextInput style = {styles.input}
                    underlineColorAndroid = "transparent"
                    placeholder = "Destination"
                    placeholderTextColor = "#9a73ef"
                    autoCapitalize = "none"
                    onChangeText = {this.handleDestination}/>
                <TouchableOpacity
                    style = {styles.submitButton}
                    onPress = {
                        () => this.route(this.state.origin, this.state.destination)
                    }>
                <Text style = {styles.submitButtonText}> Submit </Text>
                </TouchableOpacity>
            </View>
        )
     }
  }
  export default Inputs
  
  const styles = StyleSheet.create({
     container: {
        paddingTop: 23
     },
     input: {
        margin: 15,
        height: 40,
        borderColor: '#7a42f4',
        borderWidth: 1,
        padding: 10
     },
     submitButton: {
        backgroundColor: '#7a42f4',
        padding: 10,
        margin: 15,
        height: 40,
     },
     submitButtonText:{
        color: 'white'
     }
  })