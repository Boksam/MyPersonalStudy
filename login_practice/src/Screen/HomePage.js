import { useEffect, useState } from "react"
import '../CSS/HomePage.css';
import axios from "axios";
const HomePage = () => {
    const [id, setID] = useState("");
    const [pw, setPW] = useState("");


    const login = () => {
        console.log("try login");
        axios
            .post('localhost:1337/api/auth/local', {
                identifier: id,
                password: pw,
            })
            .then(response => {
                console.log("Login success");
            })
            .catch(error => {
                console.log("Error occured: ", error.response);
            });
    }

    return (
        <div className="main-home">
            <div>
                <form>
                    <label>ID : </label>
                    <input type="text" className="id-input" onChange={e => setID(e.target.value)} value={id}/>
                    <label>PW : </label>
                    <input type="text" className="pw-input" onChange={e => setPW(e.target.value)} value={pw}/>
                    <button className="input-btn" onClick={login}>login</button>
                </form>
            </div>
        </div>
    )
}

export default HomePage;