import logo from './logo.svg';
import './App.css';
import InfoComponent from './components/Info';
import {PropTypes} from "prop-types"
import {useState} from "react"

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
          <Info></Info>
        </p>
      </header>
      <body>
      </body>
    </div>
  );
}


function ButtonSate(){
  const [title, setTitle] = useState("")
  const [counter, setCounter] = useState(0)

  const updateCounterClicked =() => {
    setCounter(counter+1)
  }
  const updateTitleClicked =() => {
    setTitle("new title!")
  }

  return (
    <div>
    <p>Title: {title}</p>
    <p>Counter: {counter}</p>
    <button onClick={updateTitleClicked}>Update title</button>
    <button onClick={updateCounterClicked}>Update Counter</button>
    </div>
  )
}




function Data (props){
  return (
    <div>
      <p>Title: {props.title}</p>
    </div>
  )
}


const Info =  () => {
  return (
    <div>
      <InfoComponent title="jsx"/>
      <ButtonSate></ButtonSate>
      <h2>
        Inventory System
      </h2>
      <p> Manage your stuff.</p>
    </div>
  );
}

export default App;