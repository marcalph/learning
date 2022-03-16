import React from "react";

class InfoComponent extends React.Component {
    constructor(props) {
        super(props)
        console.log(props)
        this.state = {
            counter:-17,
            title: "Hello"
        }
    }

    buttonPressed() {
        this.setState({counter: this.state.counter+1})
    }


    render() {
        return (
        <div>
        <p> Count: {this.state.counter}</p>
        <button onClick={() => this.buttonPressed()}>ClickMe!</button>
        </div>
        )
    }
}

export default InfoComponent