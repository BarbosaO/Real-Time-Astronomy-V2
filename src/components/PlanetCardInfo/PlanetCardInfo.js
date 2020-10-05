import React , {Component} from 'react';
import classes from './PlanetCardInfo.module.css';

const PlanetCardInfo = (props) => (
    
    <div className={classes.PlanetCardInfo}>
        <div className={classes.Quantity}>100,000</div>
        <div className={classes.Distance}>{props.text}</div>
    </div>
);

export default PlanetCardInfo;