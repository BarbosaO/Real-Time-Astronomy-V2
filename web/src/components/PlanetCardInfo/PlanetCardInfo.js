import React from 'react';
import classes from './PlanetCardInfo.module.css';

const PlanetCardInfo = (props) => (
    
    <div className={classes.PlanetCardInfo}>
        <div className={classes.Quantity}>{props.unitsData}</div>
        <div className={classes.Distance}>{props.data}</div>
    </div>
);

export default PlanetCardInfo;