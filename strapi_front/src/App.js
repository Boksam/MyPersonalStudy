import React from "react";
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Homepage from "./pages/Homepage";
import Category from "./pages/Category";
import ReviewDetails from "./pages/ReviewDetails";
import SiteHeader from "./components/SiteHeader";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <SiteHeader/>
        <Routes>
          <Route path="/" element={<Homepage/>}/>
          <Route path="details/:id" element={<ReviewDetails/>}/>
          <Route path="/category/:id" element={<Category/>}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
