import React, { Component } from 'react'
import { View, Text, TouchableOpacity, TextInput, StyleSheet } from 'react-native'

class Inputs extends Component {
    constructor(props) {
        super(props);
        this.state = {
            origin: "",
            destination: "",
            response: null
        }
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
    populate = (origin, destination) => {
        some = {"origin" : "5021 Linda Place Longmont, Colorado", "destination" : "4223 San Marco Drive Longmont, Colorado"}
        fetch('http://127.0.0.1:5000//processed_requests', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
            origin: origin,
            destination: destination,
            })
        })
        fetch('http://127.0.0.1:5000//processed_requests', {
        method: 'GET'
        //Request Type
        })
        .then((response) => response.json())
        //If response is in json then in success
        .then((responseJson) => {
        //Success
        this.state.response = responseJson[responseJson.length - 1]
        this.state.response.forEach(element => {
            
        });
        })
        //If response is not in json then in error
        .catch((error) => {
        //Error
        console.error(error);
        });
    }
    loop = (responseJson) => {
        //const first = responseJson[0][0]
        //console.log('\n' + first)
        /*responseJson.forEach(element => {
            
        });
        */
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
                    ref = {button => {this.button = button}}
                    style = {styles.enterButton}
                    onPress = {
                        () => { this.populate(this.state.origin, this.state.destination) }
                    }>
                <Text style = {styles.enterButtonText}> LET'S GO! </Text>
                </TouchableOpacity>
                <Text style = {styles.enterButton}>
                    Route 1
                </Text>
                <Text style = {styles.enterButton}>
                    Route 2
                </Text>
                <Text style = {styles.enterButton}>
                    Route 3
                </Text>
            </View>
        )
     }
  }
  export default Inputs
  
  const styles = StyleSheet.create({
    container: {
        paddingTop: 12,
        marginTop: 10,
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
    },
    routes: {
        backgroundColor: '#9a73ef',
    }
})