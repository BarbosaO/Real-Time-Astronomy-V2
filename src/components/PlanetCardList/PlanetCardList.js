import React, { useContext } from 'react';
import classes from './PlanetCardList.module.css';
import PlanetCard from '../PlanetCard/PlanetCard';

const PlanetCardList = (props) => {
    return(
        <div className={classes.PlanetCardList}>
            <PlanetCard text={props}/>
            <PlanetCard text={props}/>
            <PlanetCard text={props}/>
            <PlanetCard text={props}/>
            <PlanetCard text={props}/>
            <PlanetCard text={props}/>
            <PlanetCard text={props}/>
            <PlanetCard text={props}/>
        </div>
    );
}

export default PlanetCardList;