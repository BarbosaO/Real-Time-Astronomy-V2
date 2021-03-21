import React , {Component} from 'react';
import PlanetCardList from '../components/PlanetCardList/PlanetCardList';
import classes from './Home.module.css';
import CalculationsService from '../api/CalculationsService.js';

const title = "Real Time Astronomy";
const aboutText = "An astronomy engine to calculate heliocentric and geocentric distances, and additional orbital data of planets from the solar system in real time. This is an upgraded version."

class Home extends Component{

    state = {
        textArray : ["Distance in", "MI", "x-coordinate (Hx)", "y-coordinate (Hy)", "z-coordinate (Hz)"],
        seconds : 0
    }

    switchToKmHandler = () =>{
        this.setState({
            textArray : ["Distance in", "KM", "x-coordinate (Hx)", "y-coordinate (Hy)", "z-coordinate (Hz)"]
        })
    }

    switchToMIHandler = () =>{
        this.setState({
            textArray : ["Distance in", "MI", "x-coordinate (Hx)", "y-coordinate (Hy)", "z-coordinate (Hz)"]
        })
    }

    switchToAUHandler = () =>{
        this.setState({
            textArray : ["Distance in", "AU", "x-coordinate (Hx)", "y-coordinate (Hy)", "z-coordinate (Hz)"]
        })
    }

    retrieveMercuryCalculations(){

      CalculationsService.retrieveMercuryCalculations()
      .then(response => this.handleSuccessfulResponse(response))
      .catch(error => this.handleError(error))
    }

    handleSuccessfulResponse(response){
        console.log("Response: " + response.data[0][0]);
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

        this.setState({seconds : errorMessage});
    }

    tick() {

        this.retrieveMercuryCalculations();
        this.setState(state => ({
            seconds: state.seconds + 1
        }));
    }

    componentDidMount() {
        this.interval = setInterval(() => this.tick(), 1000);
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
                    <PlanetCardList text={this.state.textArray} unitsData={this.state.seconds}/>
                </section>
        
            </div>
        );
    }
}

export default Home;