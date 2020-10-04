import React, {Component} from 'react';
import './App.css';
import PlanetCardList from './components/PlanetCardList/PlanetCardList';

class App extends Component {
  render(){
    return(
      <div>
        <PlanetCardList />
      </div>
    );
  }
}

export default App;
