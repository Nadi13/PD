import css from './Menu.module.scss';
import strings from '../../myTools/strings.tsx';

const Menu = () => {
    return <>
        <div className = {css.menu}>
            <form className = {css.form}>
                <img className={css.img} src='src/assets/search.png'></img>
                <input className = {css.input} type = "text"/>
            </form>
            <select name = "group" id = "group-select">
                <option value = "">{strings.Group}</option>
                <option value = "">{strings.Mo211}</option>
            </select>
        </div>
    </>
}

export default Menu;