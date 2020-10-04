import React from 'react';
import classes from './PlanetCardList.module.css';
import PlanetCard from '../PlanetCard/PlanetCard';

const PlanetCardList = (props) => (
    <div className={classes.PlanetCardList}>
        <PlanetCard />
        <PlanetCard />
        <PlanetCard />
        <PlanetCard />
        <PlanetCard />
        <PlanetCard />
        <PlanetCard />
        <PlanetCard />
    </div>
);

export default PlanetCardList;