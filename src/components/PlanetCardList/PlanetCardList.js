import React, { useContext } from 'react';
import classes from './PlanetCardList.module.css';
import PlanetCard from '../PlanetCard/PlanetCard';

const PlanetCardList = (props) => {
    return(
        <div className={classes.PlanetCardList}>
            <PlanetCard data={props}/>
            <PlanetCard data={props}/>
            <PlanetCard data={props}/>
            <PlanetCard data={props}/>
            <PlanetCard data={props}/>
            <PlanetCard data={props}/>
            <PlanetCard data={props}/>
            <PlanetCard data={props}/>
        </div>
    );
}

export default PlanetCardList;