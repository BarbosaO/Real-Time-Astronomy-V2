import React from 'react';
import Auxiliary from '../../Auxiliary';
import classes from './PlanetCard.module.css';

const PlanetCard = (props) => (
    <Auxiliary>
        <div className={classes.PlanetCard}>
            <div className={classes.Header}>Name</div>
            <div className={classes.HeaderLine}></div>
        </div>
    </Auxiliary>
);

export default PlanetCard;