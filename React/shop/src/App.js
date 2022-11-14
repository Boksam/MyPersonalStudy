import logo from './logo.svg';
import { useState } from 'react';
import { Routes, Route, Link, useNavigate, Outlet } from 'react-router-dom';
import './App.css';
import data from './data.js';
import Detail_page from './routes/detail.js';

function App() {
  let [shoes, set_shoes] = useState(data);
  let navigate = useNavigate(); 
  
  return (
    <div className="App">
      <div className='navbar'>
        <h4>Junwoo's Shop</h4>
        <span className='space'></span>
        <button onClick={()=> {navigate('/') }}>Home</button>
        <button onClick={()=> {navigate('/detail') }}>Detail</button>
      </div>

      <Routes>
        <Route path='/' element={
          <>
            <div className='main-bg'></div><div className='shoes_list'>
              {
                shoes.map((shoe, i) => {
                  return <ShoesComponent shoe={shoe} i={i} />;
                })
              }
            </div>
          </>
        }/>
        <Route path='/detail' element={<Detail_page/>} />
        <Route path='/about' element={<About/>}>
          <Route path='member' element={<div>Ho</div>}/>
          <Route path='location' element={<div>Ho</div>}/>
        </Route>
        <Route path='*' element={<div>404 ERROR</div>} />
      </Routes>
    </div>
  );
}

let ShoesComponent = (props) => {
  return (<div>
    <img src={'https://codingapple1.github.io/shop/shoes' + (props.i + 1) + ".jpg"}/>
    <h4>{props.shoe.title}</h4>
    <p>{props.shoe.content}</p>
  </div>)
};

let About = () => {
  return (
    <div>
      <h4>회사정보</h4>
      <Outlet></Outlet>
    </div>
  )
}

export default App;