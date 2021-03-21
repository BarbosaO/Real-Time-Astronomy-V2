import React from 'react';
import classes from './PlanetCardInfoList.module.css';
import PlanetCardInfo from '../PlanetCardInfo/PlanetCardInfo';

const PlanetCardInfoList = (props) => (
    <div className={classes.PlanetCardInfoList}>
        <PlanetCardInfo data={props.data.data.text[0] + " " + props.data.data.text[1]} unitsData={props.data.data.unitsData}/>
        <PlanetCardInfo data={props.data.data.text[2]}/>
        <PlanetCardInfo data={props.data.data.text[3]}/>
        <PlanetCardInfo data={props.data.data.text[4]}/>
    </div>
);

export default PlanetCardInfoList;