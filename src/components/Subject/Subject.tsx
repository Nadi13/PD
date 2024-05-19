import css from './Subject.module.scss';
import strings from '../../myTools/strings.tsx';
import Content from "../Content/Content.tsx";

const Subject = () => {
    return <>
        <div className = {css.container}>
            <div className = {css.content}>
            <select name="pets" id="pet-select">
            <option value="">{strings.Subject}</option>
            </select>
            <div className = {css.textBlock}>
                <button className = {css.button}>
                    {strings.Unverifid}
                    <div className = {css.count}>9</div>
                </button>
                <button className = {css.button}>
                    {strings.Retake}
                    <div className = {css.count}>2</div>
                </button>
                <button className={`${css.button} ${css.button1}`}>{strings.Deferred}</button>
                <button className={`${css.button} ${css.button2}`}>{strings.Accepted}</button>
                <button className={`${css.button} ${css.button3}`}>{strings.Rejected}</button>
            </div>
            </div>
            <Content/>
        </div>
    </>
}

export default Subject;