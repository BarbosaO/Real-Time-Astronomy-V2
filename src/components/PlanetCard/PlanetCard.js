import React from 'react';
import classes from './PlanetCard.module.css';
import PlanetCardInfoList from '../PlanetCardInfoList/PlanetCardInfoList';

const PlanetCard = (props) => (
    <div className={classes.PlanetCard}>
        <div className={classes.Header}>Name</div>
        <div className={classes.HeaderLine}></div>
        <PlanetCardInfoList data={props}/>
    </div>
   
);

export default PlanetCard;