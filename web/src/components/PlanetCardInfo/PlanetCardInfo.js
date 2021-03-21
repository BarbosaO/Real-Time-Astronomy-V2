import React from 'react';
import classes from './PlanetCardInfo.module.css';

const PlanetCardInfo = (props) => (
    <div className={classes.PlanetCardInfo}>
        {props.planetData && <div className={classes.Quantity}>{props.planetData}</div>}
        <div className={classes.Distance}>{props.text}</div>
    </div>
);

export default PlanetCardInfo;