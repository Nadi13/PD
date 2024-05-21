import css from './Header.module.scss'
import strings from '../../myTools/strings.tsx';

const Header = () => {
    return <>
        <header className = {css.header}>
            <nav className = {css.nav}> 
                <ul className = {css.ul}>
                <li><a href="" className = {css.selected}>{strings.Upload}</a></li>
                <li><a href="" className = {css.a}>{strings.Statements}</a></li>
                <li><a href="" className = {css.a}>{strings.Memo}</a></li>
                <li><a href="" className = {css.a}>{strings.LaboratoryWorks}</a></li>
                </ul>
            </nav>
            <div className = {css.profile_block}>
                <img className={css.img} src='src/assets/notification.png'></img>
                <div className={css.circle}>{strings.C}</div>
            </div>
        </header>
    </>
}

export default Header;