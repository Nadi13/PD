import Header from "../../Screen2/Header/Header";
import Body from "./Body/Body";
import css from "./Main.module.scss"

const Main = () => {
    return <>
    <div className = {css.main}>
        <div className = {css.body}>
            <Header/>
            <Body/>
        </div>
        </div>  
    </>
}

export default Main;