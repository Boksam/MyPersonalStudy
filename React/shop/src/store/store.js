import { configureStore, createSlice } from "@reduxjs/toolkit";
import user from './userSlice.js';

let stock = createSlice({
    name : 'stock',
    initialState : [10, 11, 12],
})

let cart = createSlice({
    name : 'cart',
    initialState : [
        {id : 0, name : 'White and Black', count : 2},
        {id : 2, name : 'Grey Yordan', count : 1}
    ],
    reducers : {
        plusCount(state, actions){
            console.log(actions.id);
            const id = actions.payload.id;
            const [target] = state.filter(shoe => shoe.id === id);
            target.count += actions.payload.addCount;
        }
    }
});
export let {plusCount} = cart.actions;

export default configureStore({
    reducer : {
        user : user.reducer,
        stock : stock.reducer,
        cart : cart.reducer,
    }
})