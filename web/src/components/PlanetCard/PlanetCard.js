import React from 'react';
import classes from './PlanetCard.module.css';
import PlanetCardInfoList from '../PlanetCardInfoList/PlanetCardInfoList';
import PlanetCardInfo from '../PlanetCardInfo/PlanetCardInfo.js';

function formatDistance(distance) {
    let nfDistance = new Intl.NumberFormat('en-US');
    return nfDistance.format(distance); 
}

const PlanetCard = (props) => (
    <div className={classes.PlanetCard}>
        {props.planetData && <div className={classes.Header}>{props.planetData.planet_name}</div>}
        <div className={classes.HeaderLine}></div>
        {props.planetData && <PlanetCardInfo text={props.data.text[0] + " " + props.data.text[1]} planetData={formatDistance(props.distanceData)}/>}
        {props.planetData && <PlanetCardInfo text={props.data.text[2]} planetData={props.planetData.heliocentric_x_coordinate}/>}
        {props.planetData && <PlanetCardInfo text={props.data.text[3]} planetData={props.planetData.heliocentric_y_coordinate}/>}
        {props.planetData && <PlanetCardInfo text={props.data.text[4]} planetData={props.planetData.heliocentric_z_coordinate}/>}
    </div>
   
);

export default PlanetCard;