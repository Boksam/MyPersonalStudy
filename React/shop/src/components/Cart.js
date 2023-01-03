import { Table } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import '../css/cart.css';
import { plusCount } from "../store/store";
import { changeAge } from "../store/userSlice";

const Cart = () => {

    let user = useSelector((state)=>{return state.user});
    let cart = useSelector((state)=>{return state.cart});
    let dispatch = useDispatch();

    return (
        <div>
            <h4>{user.name}({user.age})'s basket</h4>
            <button onClick={()=>{dispatch(changeAge())}}>Age</button>
            <Table className="main-table">
                <thead>
                    <tr className="table-head">
                    <th>#</th>
                    <th>ID</th>
                    <th>상품명</th>
                    <th>수량</th>
                    <th>추가하기</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        cart.map((shoe, i) =>{
                            return(
                                <tr key={i}>
                                    <td>{i + 1}</td>
                                    <td>{shoe.id}</td>
                                    <td>{shoe.name}</td>
                                    <td>{shoe.count}</td>
                                    <td><button onClick={()=>{dispatch(plusCount({id : shoe.id, addCount : 1}))}}>+</button></td>
                                </tr>
                            )}
                        )
                    }
                </tbody>
            </Table> 
        </div>
    )
}

export default Cart;