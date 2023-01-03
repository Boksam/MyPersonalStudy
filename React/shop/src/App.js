import logo from './logo.svg';
import { useState } from 'react';
import { Routes, Route, useParams, Outlet } from 'react-router-dom';
import './App.css';
import data from './data.js';
import DetailPage from './components/DetailPage.js';
import HomePage from './components/HomePage.js';
import Navbar from './components/Navbar';
import Cart from './components/Cart';

function App() {
  let [shoes, set_shoes] = useState(data);
  
  return (
    <div className="App">
      <Navbar/>
      <Routes>
        <Route path='/' element={ <HomePage shoes={shoes} /> } />
        <Route path='/detail' element={<><h2>detail page</h2><Outlet/></>}>
          <Route path='/detail/:id' element={ <DetailPage shoes={shoes}/>} />
        </Route>
        <Route path='/cart' element={<Cart/>}/>
        <Route path='*' element={ <div>404 ERROR</div>} />
      </Routes>
    </div>
  );
}

export default App;