import React from 'react';
import PlanetCardList from '../components/PlanetCardList/PlanetCardList';
import classes from './Home.module.css';

const title = "Real Time Astronomy";
const aboutText = "An astronomy engine to calculate heliocentric and geocentric distances, and additional orbital data of planets from the solar system in real time. This is an upgraded version."

const Home = (props) => (
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
        </section>

        <section>
            <PlanetCardList />
        </section>


    </div>
)

export default Home;