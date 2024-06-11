import RequestList from '../RequestList/RequestList';
import RequestPanel from '../RequestPanel/PanelCard/PanelCard.tsx';
import classes from './Body.module.scss'
import Menu from '../../../Screen2/Menu/Menu.tsx';


const Body = () => {
    return <>
        <div className={classes.container}>
            <RequestPanel />
            <div className = {classes.content}>
                <Menu/>
                <RequestList status={''} />
            </div>
        </div>
    </>
}

export default Body;