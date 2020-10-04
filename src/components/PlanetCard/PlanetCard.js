import React from 'react';
import Auxiliary from '../../Auxiliary';
import classes from './PlanetCard.module.css';
import PlanetCardInfoList from '../PlanetCardInfoList/PlanetCardInfoList';

const PlanetCard = (props) => (
    <Auxiliary>
        <div className={classes.PlanetCard}>
            <div className={classes.Header}>Name</div>
            <div className={classes.HeaderLine}></div>
            <PlanetCardInfoList/>
        </div>
    </Auxiliary>
);

export default PlanetCard;