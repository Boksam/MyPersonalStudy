// import logo from './logo.svg';
// import './App.css';
// import { useState } from 'react';

// function App() {

//   let [title, setTitle] = useState(['남자 코트 추천', '강남 우동맛집', '파이썬독학']);
//   let [like, setLike] = useState([0, 0, 0]);
//   let [modal, setModal] = useState(false);
//   let [curTitle, setCurTitle] = useState(0);
//   let [input_value, set_input_value] = useState('');
//   const clickFunc = (i) => {
//     let copy = [...like];
//     copy[i]++;
//     setLike(copy);
//   };
  
//   function changeTitle(){
//     let copy = [...title];
//     copy[0] = "여자 코트 추천";
//     setTitle(copy);
//   };
  
//   function sortTitle(){
//     let copy = [...title];
//     copy.sort();
//     setTitle(copy);
//   };

//   function setModalTrue(){
//     if (modal == false) {
//       setModal(true);
//     }
//   };

//   const addPost = () => {
//     let title_copy = [...title, input_value];
//     let like_copy = [...like, 0];
//     setTitle(title_copy);
//     setLike(like_copy);
//   };

//   const deletePost = (targetTitle) => {
//     setTitle(title.filter(title => title != targetTitle));
//   }


//   return (
//     <div className="App">
//       <div className="black-nav">
//         <h4>준우의 블로그</h4>
//       </div>

//       <button onClick={changeTitle}>누르면 첫 글 제목 바뀜</button>
//       <button onClick={sortTitle}>누르면 가나다 순으로 정렬</button>

//       {
//         title.map((t, i) => {
//           return (
//             <div className="list">
//               <h4 onClick={() => {setModalTrue(); setCurTitle(i)}}>{t} 
//               <span onClick = {(e) => {e.stopPropagation(); clickFunc(i)}}> 👍🏻 </span> {like[i]}
//               <button onClick={() => {deletePost(t)}}>삭제하기</button>
//               </h4>
//               <p>2월 17일 발행</p>
//             </div>
//           )
//         })
//       }
//       <div>
//       <input type="text" onChange={(e) => set_input_value(e.target.value)}/>
//       <button onClick={() => {addPost();}}/>
//       </div>
//       {
//         modal == true ? <Modal curTitle={curTitle} changeTitle={changeTitle} title={title}/> : null
//       }
      
//     </div>
//   );
// }



// let Modal = (props) => {
//   return (
//     <div className="modal">
//       <h4>{props.title[props.curTitle]}</h4>
//       <p>날짜</p>
//       <p>상세내용</p>
//       <button onClick={() => {props.changeTitle()}}>첫번째 제목 바꾸기</button>
//     </div>
//   )
// }

// export default App;


import { useState, useRef, useEffect } from 'react';

function App() {
  const [myState, setMyState] = useState(false);
  const DropMenu = () => {
    return (<>
      <h2>hello</h2>
      <p>hihihi</p>
    </>)
  }

  return (
    <>
      <button onClick={() => {setMyState((prev) => !prev)}}>press this</button>
      {myState ? <DropMenu/> : null}
    </>
  )
}

export default App;