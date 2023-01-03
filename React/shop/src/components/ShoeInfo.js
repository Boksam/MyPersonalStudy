import { useNavigate } from "react-router-dom";

const ShoeInfo = (props) => {
    let navigate = useNavigate();
    return (
        <div onClick={()=>navigate('/detail/'+(props.i))}>
            <img src={'https://codingapple1.github.io/shop/shoes' + (props.i + 1) + ".jpg"}/>
            <h4>{props.shoe.title}</h4>
            <p>{props.shoe.content}</p>
        </div>
    )
}

export default ShoeInfo;