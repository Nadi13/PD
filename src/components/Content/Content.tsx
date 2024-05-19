import css from './Content.module.scss'
import strings from '../../myTools/strings.tsx';
import Menu from '../Menu/Menu.tsx'

const Content = () => {
    return <>
        <div className = {css.content}>
            <Menu/>
        </div>
    </>
}

export default Content;