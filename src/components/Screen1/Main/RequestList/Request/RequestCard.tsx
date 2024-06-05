import classes from './RequestCard.module.scss'

const getRandomColor = () => {

    const red = Math.floor(Math.random() * 256);
    const green = Math.floor(Math.random() * 256);
    const blue = Math.floor(Math.random() * 256);

    return `rgb(${red}, ${green}, ${blue})`;
};


const RequestCard = (props: { name: string, number: string, work: string, course: string, date: string, deadline?: boolean, onClick: () => void }) => {

    const randomColor = getRandomColor();

    return <>
        <div className={classes.container} style={{ backgroundColor: props.deadline ? '#FFCFBA' : '#E9EAFF' }} onClick={props.onClick}>
            <div className={classes.elements}>
                <div className = {classes.infoStudent}>
                <div className={classes.icon}>
                    <div className={classes.circleWrap}>
                        <div className={classes.iconTypography} style={{ color: randomColor }}>{props.name.split(" ")[0].charAt(0)}</div>
                    </div>
                </div>
                <div className={classes.info1}>
                    <div className={classes.name}>{props.name}</div>
                    <div className={classes.work}>Лабораторная работа №{props.work}</div>
                </div>
                <div className={classes.info2}>{props.number.slice(0, -1)}
                    <span className={classes.highlight}>{props.number.slice(-1)}</span>
                </div>
                </div>
                <div className={classes.info3}>
                    <div className={classes.course}>{props.course}</div>
                    <div className={classes.requestData}>
                        <div className={classes.text}>дата отправки:</div>
                        <div className={classes.data}>{props.date}</div>
                    </div>
                </div>
            </div>

        </div>
        

    </>

};

export default RequestCard;