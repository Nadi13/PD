import css from './Subject.module.scss'
import strings from '../../myTools/strings.tsx';

const Subject = () => {
    return <>
        <div className = {css.container}>
            <div className = {css.content}>
            <select name="pets" id="pet-select">
            <option value="">{strings.Subject}</option>
            </select>
            <div className = {css.textBlock}>
                <div className = {css.title}>{strings.Statements}</div>
                <div className = {css.text}>{strings.LaboratoryWorks}</div>
            </div>
            </div>
        </div>
    </>
}

export default Subject;