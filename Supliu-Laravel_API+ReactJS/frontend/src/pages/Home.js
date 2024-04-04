import Navbar from './layout/Navbar.js';
import SlideHome from './layout/SlideHome.js';
import CollapseHome from './layout/CollapseHome.js';
import React from 'react';



function Home(){


    return (

        <>
            <Navbar />
            <SlideHome />
            <CollapseHome />
        </>

    );

}

export default Home;