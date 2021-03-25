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

    switchToHelioHandler = () => {
        CalculationsService.retrieveHelioData()
        .then(response => {
            this.setState({
                planetData : response.data
            })
        })
        .catch(error => this.handleError(error))
    }

    switchToGeoHandler = () => {
        CalculationsService.retrieveGeoData()
        .then(response => {
            this.setState({
                planetData : response.data
            })
        })
        .catch(error => this.handleError(error))
    }

    switchToKmHandler = () =>{

        this.retrieveCalculations(CalculationsService.retrieveHelioData(), CalculationsService.retrieveKmDistances(), "KM");
        clearInterval(this.interval);
        this.interval = setInterval(() => this.retrieveCalculations(CalculationsService.retrieveHelioData(), CalculationsService.retrieveKmDistances(), "KM"), 1000);
    }

    switchToMIHandler = () =>{
        this.retrieveCalculations(CalculationsService.retrieveHelioData(), CalculationsService.retrieveMiDistances(), "MI");
        clearInterval(this.interval);
        this.interval = setInterval(() =>  this.retrieveCalculations(CalculationsService.retrieveHelioData(), CalculationsService.retrieveMiDistances(), "MI"), 1000);
    }

    switchToAUHandler = () =>{
        this.retrieveCalculations(CalculationsService.retrieveHelioData(), CalculationsService.retrieveAuDistances(), "AU");
        clearInterval(this.interval);
        this.interval = setInterval(() => this.retrieveCalculations(CalculationsService.retrieveHelioData(), CalculationsService.retrieveAuDistances(), "AU"), 1000);
    }

    retrieveCalculations(requestOne, requestTwo, units){
        
        const calculations_request = requestOne
        const distances_request = requestTwo

        axios.all([calculations_request, distances_request])
      .then(axios.spread((...responses) => {
          const calculations_response = responses[0]
          const distances_response = responses[1]

          this.setState({
            textArray : ["Distance in", units, "x-coordinate (Hx)", "y-coordinate (Hy)", "z-coordinate (Hz)"],
            planetData : calculations_response.data,
            distanceData : distances_response.data
        })
      }))
    }

    retrieveInitialCalculations(){

      const helio_calculations_request = CalculationsService.retrieveHelioData();
      const initial_distances_request = CalculationsService.retrieveMiDistances();

      axios.all([helio_calculations_request, initial_distances_request])
      .then(axios.spread((...responses) => {
          const helio_calculations_request = responses[0]
          const initial_distances_response = responses[1]

          this.handleSuccessfulResponse(helio_calculations_request, initial_distances_response)
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

    handleSuccessfulResponse(helio_calculations_res, initial_distances_res){
        this.setState({
            planetData : helio_calculations_res.data,
            distanceData : initial_distances_res.data
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

        return errorMessage
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
                        <button onClick={this.switchToGeoHandler}>GEO</button>
                        <button onClick={this.switchToHelioHandler}>HELIO</button>
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