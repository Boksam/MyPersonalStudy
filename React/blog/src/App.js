import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {

  let [title, setTitle] = useState(['남자 코트 추천', '강남 우동맛집', '파이썬독학']);
  let [like, setLike] = useState([0, 0, 0]);
  let [modal, setModal] = useState(false);
  let [curTitle, setCurTitle] = useState(0);
  const clickFunc = (i) => {
    let copy = [...like];
    copy[i]++;
    setLike(copy);
  };
  
  function changeTitle(){
    let copy = [...title];
    copy[0] = "여자 코트 추천";
    setTitle(copy);
  };
  
  function sortTitle(){
    let copy = [...title];
    copy.sort();
    setTitle(copy);
  };

  function setModalTrue(){
    if (modal == false) {
      setModal(true);
    }
  };


  return (
    <div className="App">
      <div className="black-nav">
        <h4>준우의 블로그</h4>
      </div>

      <button onClick={changeTitle}>누르면 첫 글 제목 바뀜</button>
      <button onClick={sortTitle}>누르면 가나다 순으로 정렬</button>

      {
        title.map((t, i) => {
          return (
            <div className="list">
            <h4 onClick={() => {setModalTrue(); setCurTitle(i)}}>{i} : {t} <span onClick = {() => {clickFunc(i)}}> 👍🏻 </span> {like[i]} </h4>
            <p>2월 17일 발행</p>
            </div>
          )
        })
      }

      {
        modal == true ? <Modal curTitle={curTitle} changeTitle={changeTitle} title={title}/> : null
      }
      
    </div>
  );
}



let Modal = (props) => {
  return (
    <div className="modal">
      <h4>{props.title[props.curTitle]}</h4>
      <p>날짜</p>
      <p>상세내용</p>
      <button onClick={props.changeTitle}>첫번째 제목 바꾸기</button>
    </div>
  )
}

export default App;
