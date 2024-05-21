import css from './Tasks.module.scss';
import strings from '../../myTools/strings.tsx';

const Tasks = () => {
    return <>
        <div className = {css.tasks}>
            <nav className = {css.nav}> 
                <ul className = {css.ul}>
                <li><a href="" className = {css.a1}>{strings.Lab1}</a></li>
                <li><a href="" className = {css.a}>{strings.Lab2}</a></li>
                <li><a href="" className = {css.a}>{strings.Lab3}</a></li>
                <li><a href="" className = {css.a}>{strings.Lab4}</a></li>
                <li><a href="" className = {css.a}>{strings.Lab5}</a></li>
                </ul>
            </nav>
        </div>
    </>
}

export default Tasks;
