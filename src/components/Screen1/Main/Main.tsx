import Header from "../../Screen2/Header/Header";
import Body from "./Body/Body";
import css from "./Main.module.scss"
import { useLocation } from "react-router-dom";

const Main = () => {
    const location = useLocation();
    const user = location.state?.user;
    console.log(user.sessionKey)
    return <>
    <div className = {css.main}>
        <div className = {css.body}>
            <Header/>
            <Body key1 = {user.sessionKey}/>
        </div>
        </div>  
    </>
}

export default Main;