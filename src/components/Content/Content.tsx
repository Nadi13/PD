import css from './Content.module.scss'
import strings from '../../myTools/strings.tsx';
import Labor from '../Labor/Labor.tsx'
import Tasks from '../Tasks/Tasks.tsx'

const Content = () => {
    return <>
        <div className = {css.content}>
            <Labor/>
            <Tasks/>
        </div>
    </>
}

export default Content;