import classes from './Subject.module.scss'

const Subject = ({ name }: { name: string }) => {
    return <>
        <div className={classes.wrap}>
            <div className={classes.text}>{name}</div>
            {/* <div className={classes.icon} style={{ width: '17px', height: '9px' }}>
                <img src="src/assets/arrow.png" />
            </div> */}
        </div>
    </>
}

export default Subject;