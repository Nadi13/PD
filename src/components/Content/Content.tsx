import css from './Content.module.scss'
import Menu from '../Menu/Menu.tsx';
import LabInfo from '../LabInfo/LabInfo.tsx';

const Content = () => {
    
    return <>
        <div className = {css.content}>
            <Menu/>
            <LabInfo/>
        </div>
    </>
}

export default Content;