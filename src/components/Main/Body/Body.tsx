import RequestList from '../RequestList/RequestList';
import RequestPanel from '../RequestPanel/RequestPanel';
import classes from './Body.module.scss'

const Body = () => {
    return <>

        <div className={classes.container}>
            <RequestPanel />
            <RequestList />
        </div>
    </>
}

export default Body;