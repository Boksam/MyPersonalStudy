import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";

let DetailPage = (props) => {
    const shoeID = useParams();
    const shoe = props.shoes.find(shoe => shoe.id == shoeID.id);
    const [count, setCount] = useState("");
    
    useEffect(() => {
        if (isNaN(count)){
            setCount("");
            alert('Number only');
        }
    }, [count]);


    const cart = useSelector((state) => state.cart);
    const addCart = () => {
        
    }

    return (
    <div className="container">
        <div className="row">
            <div className="col-md-6">
                <img src={"https://codingapple1.github.io/shop/shoes" + (shoe.id + 1) + ".jpg"} width="50%"/>
            </div>
            <div className="col-md-6">
                <h4 className="pt-5">{shoe.title}</h4>
                <p>{shoe.content}</p>
                <p>{shoe.price}원</p>
                <form>
                    <input type="text" onChange={e => setCount(e.target.value)} value={count}></input>
                    <button type="submit" className="btn btn-danger">주문하기</button>
                </form>
                
            </div>
        </div>
    </div>)
}

export default DetailPage;