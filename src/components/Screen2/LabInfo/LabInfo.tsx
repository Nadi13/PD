import css from './LabInfo.module.scss';
import strings from '../../../myTools/strings.tsx';
import { useLocation } from "react-router-dom";
import { Link } from 'react-router-dom';

const LabInfo = () => {
    const location = useLocation();
    const selectedRequest = location.state;
    const course = Math.ceil(selectedRequest.lab.semester / 2);

    const date1 = new Date(selectedRequest.creationdate)
    const week = date1.toLocaleDateString("ru-RU", { weekday: "short" });
    const month = date1.toLocaleDateString("ru-RU", { day: "numeric", month: "short" });
    const timecreation = date1.toLocaleTimeString("ru-RU", { hour: "numeric", minute: "numeric" });
    const formattedDate = `${week}, ${month}, ${timecreation}`;

    const content = selectedRequest.content.split(' ');

    return <>
        <div className = {css.container}>
            <div className = {css.info}>
                <div className = {css.student}>
                    <div className = {css.circle}>{selectedRequest.student.surname.split(" ")[0].charAt(0)}</div>
                    <div className = {css.fio}>{`${selectedRequest.student.surname} ${selectedRequest.student.name} ${selectedRequest.student.patronymic}`}</div>
                    <div className = {css.group}>{selectedRequest.lab.qroupname}</div>
                    <div className = {css.course}>{course} {strings.Course}, {selectedRequest.lab.semester} {strings.Semestr}</div>
                </div>
                <div className = {css.work}>
                    <div className = {css.lab}>{selectedRequest.lab.name}</div>
                    <div className= {css.variant}>{strings.Variant} {selectedRequest.variant}</div>
                </div>
                <div className = {css.description}>{selectedRequest.lab.description}</div>
                <div className = {css.content}>
                    {strings.Content}
                    <div className = {css.text}>
                        {strings.Data1}
                        <div className = {css.data}> {formattedDate }</div>
                    </div>
                </div>
                <div className = {css.box}>
                <p>
                    {content.map((item: string, index: number) => {
                        if(item.includes('http')) {
                            return <Link key={index} to={item}>{item}</Link>;
                        } 
                        return <span key={index}>{item}</span>;
                    })}
                </p>
                </div>
                <div className = {css.git}>
                    <div className = {css.text1}>
                        {strings.Percent}
                        <div className = {css.percent}>100%</div>
                    </div>
                    <div className = {css.text1}>
                        {strings.Commits}
                        <div className = {css.commit}>12</div>
                    </div>
                </div>
                <div className = {css.content}>{strings.Comment}</div>
                <div className = {css.box}></div>
                <div className = {css.buttonBlock}>
                    <button className = {css.buttonCross}></button>
                    <button className = {css.buttonCheck}></button>
                    <button className = {css.button3}>{strings.Add}</button>
                </div>
            </div>
            <div className = {css.taskBlock}>
                <div className = {css.text}>{strings.Task}</div>
                <div className = {css.task}></div>
            </div>
        </div>
    </>
}

export default LabInfo;