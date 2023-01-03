import { useNavigate } from "react-router-dom";

const Navbar = () => {
    const navigate = useNavigate();
    return (
        <div className='navbar'>
            <h4>Junwoo's Shop</h4>
            <span className='space'></span>
            <button onClick={()=> {navigate('/') }}>Home</button>
            <button onClick={()=> {navigate('/detail') }}>Detail</button>
        </div>)
}

export default Navbar;