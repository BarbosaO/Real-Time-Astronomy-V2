import React, { useContext } from 'react';
import classes from './PlanetCardList.module.css';
import PlanetCard from '../PlanetCard/PlanetCard';

const PlanetCardList = (props) => {
    return(
        <div className={classes.PlanetCardList}>
            <PlanetCard data = {props} planetData={props.planetData.mercury}/>
            <PlanetCard data = {props} planetData={props.planetData.venus}/>
            <PlanetCard data = {props} planetData={props.planetData.mars}/>
            <PlanetCard data = {props} planetData={props.planetData.jupiter}/>
            <PlanetCard data = {props} planetData={props.planetData.saturn}/>
            <PlanetCard data = {props} planetData={props.planetData.uranus}/>
            <PlanetCard data = {props} planetData={props.planetData.neptune}/>
        </div>
    );
}

export default PlanetCardList;