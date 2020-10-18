import React from 'react';
import {
  StyleSheet,
  View,
  Text
} from 'react-native';
import Inputs from './Inputs.js'


const App = () => {
  return (
		<View style={styles.main}>
			<Text style={styles.title}>
				NiteLite
			</Text>
    		<Inputs />
		</View>
	);
};

const styles = StyleSheet.create({
	main: {
		backgroundColor: "black",
		flex: 1
	},
	title: {
		color: '#7a42f4',
		shadowColor: '#9a73ef',
		fontSize: 50,
		marginTop: 250,
		marginLeft: 125,
		marginRight: 120,
		textAlignVertical: 'center'
	}
})

export default App;
