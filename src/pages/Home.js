import React , {Component} from 'react';
import PlanetCardList from '../components/PlanetCardList/PlanetCardList';
import classes from './Home.module.css';

const title = "Real Time Astronomy";
const aboutText = "An astronomy engine to calculate heliocentric and geocentric distances, and additional orbital data of planets from the solar system in real time. This is an upgraded version."

class Home extends Component{

    state = {
        textArray : ["Distance in", "MI", "x-coordinate (Hx)", "y-coordinate (Hy)", "z-coordinate (Hz)"]
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
                    <PlanetCardList text={this.state.textArray}/>
                </section>
        
            </div>
        );
    }
}

export default Home;