import Subject from './Subject/Subject';
import PanelCardList from './PanelCardList/PanelCardList';
import classes from './RequestPanel.module.scss'

const subjectName: string = "ООАиП"

const RequestPanel = () => {
    return <>

        <div className={classes.wrap}>
            <Subject name={subjectName}/>
            <PanelCardList/>
        </div>
    </>
}

export default RequestPanel;