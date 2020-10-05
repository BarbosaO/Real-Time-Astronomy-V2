import React from 'react';
import classes from './PlanetCardInfoList.module.css';
import PlanetCardInfo from '../PlanetCardInfo/PlanetCardInfo';

const PlanetCardInfoList = (props) => (
    <div className={classes.PlanetCardInfoList}>
        <PlanetCardInfo text={props.text.text.text[0] + " " + props.text.text.text[1]}/>
        <PlanetCardInfo text={props.text.text.text[2]}/>
        <PlanetCardInfo text={props.text.text.text[3]}/>
        <PlanetCardInfo text={props.text.text.text[4]}/>
    </div>
);

export default PlanetCardInfoList;