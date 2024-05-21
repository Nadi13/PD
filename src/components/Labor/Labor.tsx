import css from './Labor.module.scss';
import strings from '../../myTools/strings.tsx';

const Labor = () => {
    return <>
        <div className = {css.labor}>
            <div className = {css.title}>{strings.LaboratoryWork}</div>
            <select name = "laboratory" id = "laboratory-select">
                <option value = "">{}</option>
            </select>
            <div className = {css.title}>{strings.Variant}</div>
            <select name = "variant" id = "variant-select">
                <option value = "">{}</option>
            </select>
            <div className = {css.title}>{strings.Send}</div>
            <input className = {css.input} type = "text"/>
            <button className = {css.button}>{strings.Send}</button>
        </div>
    </>
}

export default Labor;