import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {

  let [title, setTitle] = useState(['남자 코트 추천', '강남 우동맛집', '파이썬독학']);
  let [like, setLike] = useState(0);
  let[modal, setModal] = useState(false);
  function clickFunc(){
    setLike(like+1);
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
    if (modal == true){
      setModal(false);
    }
    else{
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

      <div className="list">
        <h4 onClick={setModalTrue}>{title[0]} <span onClick={ clickFunc }>👍🏻</span> {like} </h4>
        <p>2월 17일 발행</p>
      </div>
      <div className="list">
        <h4>{title[1]}</h4>
        <p>2월 17일 발행</p>
      </div>
      <div className="list">
        <h4>{title[2]}</h4>
        <p>2월 17일 발행</p>
      </div>
      

      {
        modal == true ? <Modal/> : null
      }
      
    </div>
  );
}



function Modal(){
  return (
    <div className="modal">
      <h4>제목</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
}

export default App;
