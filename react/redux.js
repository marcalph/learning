const INCREMENT = "INCREMENT"; // Define a constant for increment action types
const DECREMENT = "DECREMENT"; // Define a constant for decrement action types

const counterReducer = (state=0, action) => {
  switch (action.type) {
    case INCREMENT:
      return state+1;
  case DECREMENT:
      return state-1;
  default:
    return state;

  }
}; // Define the counter reducer which will increment or decrement the state based on the action it receives

const incAction = ()=>{return {type:INCREMENT}}; // Define an action creator for incrementing

const decAction = ()=>{return {type:DECREMENT}}; // Define an action creator for decrementing

const store = Redux.createStore(counterReducer); // Define the Redux store here, passing in your reducers










const defaultState = {
    user: 'CamperBot',
    status: 'offline',
    friends: '732,982',
    community: 'freeCodeCamp'
  };
  
  const immutableReducer = (state = defaultState, action) => {
    switch(action.type) {
      case 'ONLINE':
        // Don't mutate state here or the tests will fail
        const newobj = Object.assign({}, state, {status: "online"})
        return newobj
      default:
        return state;
    }
  };
  
  const wakeUp = () => {
    return {
      type: 'ONLINE'
    }
  };
  
  const store = Redux.createStore(immutableReducer);