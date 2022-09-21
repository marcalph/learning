const ChildComponent = () => {
    return (
      <div>
        <p>I am the child</p>
      </div>
    );
  };

class ParentComponent extends React.Component {
constructor(props) {
    super(props);
}
render() {
    return (
    <div>
        <h1>I am the parent</h1>
        { /* Change code below this line */ }
        <ChildComponent />

        { /* Change code above this line */ }
    </div>
    );
}
}
// ReactDOM.render(<ParentComponent/>, document.getElementById('challenge-node'))



class Counter extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        count: 0
      };
    this.increment = this.increment.bind(this);
    this.decrement = this.decrement.bind(this);
    this.reset = this.reset.bind(this);
   }
    reset() {
      this.setState({
        count: 0
      });
    }
    increment() {
      this.setState(state => ({
        count: state.count + 1
      }));
    }
    decrement() {
      this.setState(state => ({
        count: state.count - 1
      }));
    }
    render() {
      return (
        <div>
          <button className='inc' onClick={this.increment}>Increment!</button>
          <button className='dec' onClick={this.decrement}>Decrement!</button>
          <button className='reset' onClick={this.reset}>Reset</button>
          <h1>Current Count: {this.state.count}</h1>
        </div>
      );
    }
  };






  class ControlledInput extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        input: ''
      };
      // Change code below this line
      this.handleChange = this.handleChange.bind(this)
      // Change code above this line
    }
    // Change code below this line
  handleChange(event) {
    this.setState(({
        input: event.target.value
      })
    )
  }
    // Change code above this line
    render() {
      return (
        <div>
          { /* Change code below this line */}
          <input value={this.state.input} onChange={this.handleChange} />
          { /* Change code above this line */}
          <h4>Controlled Input:</h4>
          <p>{this.state.input}</p>
        </div>
      );
    }
  };








  class Results extends React.Component {
    constructor(props) {
      super(props);
    }
    render() {
      return <h1>{this.props.fiftyFifty? "You Lose!" : "You Win!"}</h1>;
    }
  }

  class GameOfChance extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        counter: 1
      };
      this.handleClick = this.handleClick.bind(this);
    }
    handleClick() {
      this.setState(prevState => {
        return {
          counter: prevState.counter+1
        }
      });
    }
    render() {
      const expression = Math.random() >=.5?true:false;
      return (
        <div>
          <button onClick={this.handleClick}>Play Again</button>
          <Results fiftyFifty={expression} />
          <p>{'Turn: ' + this.state.counter}</p>
        </div>
      );
    }
  }








  class GateKeeper extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        input: ''
      };
      this.handleChange = this.handleChange.bind(this);
    }
    handleChange(event) {
      this.setState({ input: event.target.value })
    }
    render() {
      let inputStyle = {
        border: '1px solid black'
      };
      if (this.state.input.length>15){inputStyle={border: "3px solid red"}
      }
      return (
        <div>
          <h3>Don't Type Too Much:</h3>
          <input
            type="text"
            style={inputStyle}
            value={this.state.input}
            onChange={this.handleChange} />
        </div>
      );
    }
  };