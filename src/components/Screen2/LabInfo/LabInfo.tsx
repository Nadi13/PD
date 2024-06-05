import css from './LabInfo.module.scss';
import strings from '../../../myTools/strings.tsx';
import { useLocation } from "react-router-dom";

const LabInfo = () => {
    const location = useLocation();
    const selectedRequest = location.state;
    return <>
        <div className = {css.container}>
            <div className = {css.info}>
                <div className = {css.student}>
                    <div className = {css.circle}>{selectedRequest.name.split(" ")[0].charAt(0)}</div>
                    <div className = {css.fio}>{selectedRequest.name}</div>
                    <div className = {css.group}>{selectedRequest.number}</div>
                    <div className = {css.course}>{selectedRequest.course}</div>
                </div>
                <div className = {css.work}>
                    <div className = {css.lab}>Лабораторная работа №{selectedRequest.work}</div>
                    <div className= {css.variant}>{strings.Variant}</div>
                </div>
                <div className = {css.description}>{strings.Description}</div>
                <div className = {css.content}>
                    {strings.Content}
                    <div className = {css.text}>
                        {strings.Data1}
                        <div className = {css.data}> {selectedRequest.date}</div>
                    </div>
                </div>
                <div className = {css.box}></div>
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