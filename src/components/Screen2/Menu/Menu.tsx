import css from './Menu.module.scss';
import strings from '../../../myTools/strings.tsx';

import Calendar from '../Calendar/Calendar.tsx';

const Menu = () => {
    return <>
        <div className = {css.menu}>
            <form className = {css.form}>
                <img className={css.img} src='src/assets/search.png'></img>
                <input className = {css.input} type = "text"/>
            </form>
            <select className = {css.selectGroup} name = "group" id = "group-select">
                <option value = "">{strings.Group}</option>
                <option value = "">{strings.Mo211}</option>
            </select>
            <Calendar/>
            <select className = {css.selectWorks} name = "works" id = "work-select">
                <option value = "">{strings.Labs}</option>
            </select>
        </div>
    </>
}

export default Menu;