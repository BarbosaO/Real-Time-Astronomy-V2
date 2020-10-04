import React from 'react';
import classes from './PlanetCardInfoList.module.css';
import PlanetCardInfo from '../PlanetCardInfo/PlanetCardInfo';

const PlanetCardInfoList = (props) => (
    <div className={classes.PlanetCardInfoList}>
        <PlanetCardInfo />
        <PlanetCardInfo />
        <PlanetCardInfo />
        <PlanetCardInfo />
    </div>
);

export default PlanetCardInfoList;