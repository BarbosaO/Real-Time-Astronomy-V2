import React, { useContext } from 'react';
import classes from './PlanetCardList.module.css';
import PlanetCard from '../PlanetCard/PlanetCard';

const PlanetCardList = (props) => {
    return(
        <div className={classes.PlanetCardList}>
            <PlanetCard data = {props} planetData={props.planetData.mercury} distanceData={props.distanceData.mercury_heliocentric_distance}/>
            <PlanetCard data = {props} planetData={props.planetData.venus} distanceData={props.distanceData.venus_heliocentric_distance}/>
            <PlanetCard data = {props} planetData={props.planetData.mars} distanceData={props.distanceData.mars_heliocentric_distance}/>
            <PlanetCard data = {props} planetData={props.planetData.jupiter} distanceData={props.distanceData.jupiter_heliocentric_distance}/>
            <PlanetCard data = {props} planetData={props.planetData.saturn} distanceData={props.distanceData.saturn_heliocentric_distance}/>
            <PlanetCard data = {props} planetData={props.planetData.uranus} distanceData={props.distanceData.uranus_heliocentric_distance}/>
            <PlanetCard data = {props} planetData={props.planetData.neptune} distanceData={props.distanceData.neptune_heliocentric_distance}/>
        </div>
    );
}

export default PlanetCardList;