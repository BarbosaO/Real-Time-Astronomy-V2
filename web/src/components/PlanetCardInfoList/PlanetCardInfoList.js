import React from 'react';
import classes from './PlanetCardInfoList.module.css';
import PlanetCardInfo from '../PlanetCardInfo/PlanetCardInfo';

const PlanetCardInfoList = (props) => (
    <div className={classes.PlanetCardInfoList}>
        <PlanetCardInfo text={props.data.data.text[0] + " " + props.data.data.text[1]} planetData={props.data.data.planetData}/>
        <PlanetCardInfo text={props.data.data.text[2]} planetData={props.data.data.planetData}/>
        <PlanetCardInfo text={props.data.data.text[3]} planetData={props.data.data.planetData}/>
        <PlanetCardInfo text={props.data.data.text[4]} planetData={props.data.data.planetData}/>
    </div>
);

export default PlanetCardInfoList;