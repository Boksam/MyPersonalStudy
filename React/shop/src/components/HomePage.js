import ShoeInfo from "./ShoeInfo";

const HomePage = (props) => {
    return (
        <>
            <div className='main-bg'></div><div className='shoes_list'>
                {
                props.shoes.map((shoe, i) => {
                    return <ShoeInfo shoe={shoe} i={i} />;
                })
                }
            </div>
        </>
    )
}

export default HomePage;