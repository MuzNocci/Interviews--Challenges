import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home.js";
import Login from "./pages/Login.js";



const AppRoutes = () => {


   return(
       <BrowserRouter>
            <Routes>
                <Route exact path="/" element={<Home />} />
                <Route exact path="/login" element={<Login />} />
            </Routes>
       </BrowserRouter>
   )
   
}

export default AppRoutes;