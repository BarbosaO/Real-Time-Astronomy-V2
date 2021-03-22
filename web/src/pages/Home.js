import React , {Component} from 'react';
import PlanetCardList from '../components/PlanetCardList/PlanetCardList';
import classes from './Home.module.css';
import CalculationsService from '../api/CalculationsService.js';
import axios from 'axios';

const title = "Real Time Astronomy";
const aboutText = "An astronomy engine to calculate heliocentric and geocentric distances, and additional orbital data of planets from the solar system in real time. This is an upgraded version."

class Home extends Component{

    state = {
        textArray : ["Distance in", "MI", "x-coordinate (Hx)", "y-coordinate (Hy)", "z-coordinate (Hz)"],
        planetData : '',
        distanceData : '',
    }

    switchToKmHandler = () =>{
        this.retrieveDistances(CalculationsService.retrieveKmDistances, "KM");
        clearInterval(this.interval);
        this.interval = setInterval(() => this.retrieveDistances(CalculationsService.retrieveKmDistances, "KM"), 1000);
    }

    switchToMIHandler = () =>{
        this.retrieveDistances(CalculationsService.retrieveMiDistances, "MI");
        clearInterval(this.interval);
        this.interval = setInterval(() => this.retrieveDistances(CalculationsService.retrieveMiDistances, "MI"), 1000);
    }

    switchToAUHandler = () =>{
        this.retrieveDistances(CalculationsService.retrieveAuDistances, "AU");
        clearInterval(this.interval);
        this.interval = setInterval(() => this.retrieveDistances(CalculationsService.retrieveAuDistances, "AU"), 1000);
    }

    retrieveInitialCalculations(){

      const all_calculations_request = CalculationsService.retrieveAllCalculations();
      const initial_distances_request = CalculationsService.retrieveMiDistances();

      axios.all([all_calculations_request, initial_distances_request])
      .then(axios.spread((...responses) => {
          const all_calculations_response = responses[0]
          const initial_distances_response = responses[1]

          this.handleSuccessfulResponse(all_calculations_response, initial_distances_response)
      }))
      .catch(error => this.handleError(error))

    }

    retrieveDistances(func, units){
        func()
        .then(response => {
            this.setState({
                textArray : ["Distance in", units, "x-coordinate (Hx)", "y-coordinate (Hy)", "z-coordinate (Hz)"],
                distanceData : response.data,
            })
        })
    }

    handleSuccessfulResponse(responseOne, responseTwo){
        this.setState({
            planetData : responseOne.data,
            distanceData : responseTwo.data
        })
    }

    handleError(error){
        console.log(error);
        
        let errorMessage = '';
        
        if(error.message){
            errorMessage += error.message
        }

        if(error.message && error.response.data){
            errorMessage += error.response.data.message;
        }
    }

    /* tick() {

        this.setState(state => ({
            seconds: state.seconds + 1
        }));
    } */

    componentDidMount() {
        this.retrieveInitialCalculations();
        this.interval = setInterval(() => this.retrieveInitialCalculations(), 1000);
        
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }

    render(){
        return(
            <div className={classes.HomeContainer}>
                <section className={classes.LandingPageInfo}>
                    <div className={classes.landingTitle}>
                        <h1 className={classes.Title}>
                            {title}
                        </h1>
                    </div>
                    <div className={classes.AboutInfo}>
                        <p className={classes.AboutText}>
                            {aboutText}
                        </p>
                    </div>
                    <div className={classes.Buttons}>
                        <button onClick={this.switchToKmHandler}>KM</button>
                        <button onClick={this.switchToMIHandler}>MI</button>
                        <button onClick={this.switchToAUHandler}>AU</button>
                    </div>
                </section>
        
                <section>
                    <PlanetCardList text={this.state.textArray} planetData={this.state.planetData} distanceData={this.state.distanceData}/>
                </section>
            </div>
        );
    }
}

export default Home;