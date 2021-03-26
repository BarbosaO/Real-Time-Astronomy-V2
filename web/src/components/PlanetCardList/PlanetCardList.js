import React, { useContext } from 'react';
import classes from './PlanetCardList.module.css';
import PlanetCard from '../PlanetCard/PlanetCard';

const PlanetCardList = (props) => {
    return(
        
        <div className={classes.PlanetCardList}>
            <PlanetCard data = {props} planetData={props.planetData.mercury} distanceData={props.distanceData.mercury_distance}/>
            <PlanetCard data = {props} planetData={props.planetData.venus} distanceData={props.distanceData.venus_distance}/>
            <PlanetCard data = {props} planetData={props.planetData.mars} distanceData={props.distanceData.mars_distance}/>
            <PlanetCard data = {props} planetData={props.planetData.jupiter} distanceData={props.distanceData.jupiter_distance}/>
            <PlanetCard data = {props} planetData={props.planetData.saturn} distanceData={props.distanceData.saturn_distance}/>
            <PlanetCard data = {props} planetData={props.planetData.uranus} distanceData={props.distanceData.uranus_distance}/>
            <PlanetCard data = {props} planetData={props.planetData.neptune} distanceData={props.distanceData.neptune_distance}/>
        </div>
    );
}

export default PlanetCardList;