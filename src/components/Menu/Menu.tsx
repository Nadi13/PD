import css from './Menu.module.scss';
import strings from '../../myTools/strings.tsx';
import { Calendar } from 'primereact/calendar';

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
            <div className = {css.customCalendar}>
                <Calendar v-model="date"/>
            </div>
        </div>
    </>
}

export default Menu;