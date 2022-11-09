import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {
  let [posts, set_posts] = useState(['post1', 'post2', 'post3']);
  let [likes, set_likes] = useState([0, 0, 0]);
  let [modal_state, set_modal_state] = useState(false);
  let [modal_title, set_modal_title] = useState(0);
  let [curr_input, set_curr_input] = useState('');

  let add_likes = (i) => {
    let copy = [...likes];
    copy[i]++;
    set_likes(copy);
  }
  
  let del_post = (i) => {
    let posts_copy = [...posts];
    posts_copy.splice(i, 1);
    set_posts(posts_copy);
    let likes_copy = [...likes];
    likes_copy.splice(i, 1);
    set_likes(likes_copy);
  }

  let add_post = () => {
    let posts_copy = [...posts, curr_input];
    set_posts(posts_copy);
    let likes_copy = [...likes, 0];
    set_likes(likes_copy);
  }

  return (
    <div className="App">
      <div class="nav_bar">
        <h4>Junwoo's Blog</h4>
      </div>

      <div className="post_list">
        {
          posts.map((it, i) => {
            return <div className="post">
              <h4 onClick={() => {set_modal_state(true); set_modal_title(i)}}>{it}
                <button onClick={(e) => {e.stopPropagation(); add_likes(i)}}>like</button>
                <span>{likes[i]}</span>
                <button className="del_btn" onClick={(e) => {e.stopPropagation(); del_post(i)}} >delete</button>
              </h4>
              <p>11월 9일 작성</p>
            </div>
          })
        }
      </div>
      
      {
        modal_state == true ? <Modal post_title={posts[modal_title]}/> : null
      }
      <div>
        <label>Enter new Post's title : </label>
        <input type="text" className='input_new_post' onChange={(e) => set_curr_input(e.target.value)}></input>
        <button onClick={() => {add_post()}}>Commit</button>
      </div>
    </div>
  );
}

let Modal = (props) => {
  return <div className="modal">
    <h3>{props.post_title}</h3>
    <p>paragraph</p>
    <p>date</p>
  </div>
}


export default App;


