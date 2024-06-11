import classes from './RequestCard.module.scss'
import strings from '../../../../../myTools/strings.tsx';

const getRandomColor = () => {

    const red = Math.floor(Math.random() * 256);
    const green = Math.floor(Math.random() * 256);
    const blue = Math.floor(Math.random() * 256);

    return `rgb(${red}, ${green}, ${blue})`;
};


const RequestCard = (props: { name: string, number: string, work: string, semester: number, date: Date, deadline?: Date, onClick: () => void }) => {

    const randomColor = getRandomColor();

    const date1 = new Date(props.date)
    const week = date1.toLocaleDateString("ru-RU", { weekday: "short" });
    const month = date1.toLocaleDateString("ru-RU", { day: "numeric", month: "short" });
    const timecreation = date1.toLocaleTimeString("ru-RU", { hour: "numeric", minute: "numeric" });
    const course = Math.ceil(props.semester / 2);
    const formattedDate = `${week}, ${month}, ${timecreation}`;

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
                    <div className={classes.work}>{props.work}</div>
                </div>
                <div className={classes.info2}>{props.number}
                
                </div>
                </div>
                <div className={classes.info3}>
                    <div className={classes.course}> {course} {strings.Course}, {props.semester} {strings.Semestr}</div>
                    <div className={classes.requestData}>
                        <div className={classes.text}>{strings.Data1}</div>
                        <div className={classes.data}>{formattedDate}</div>
                    </div>
                </div>
            </div>

        </div>
        

    </>

};

export default RequestCard;