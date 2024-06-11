import RequestList from '../RequestList/RequestList';
import strings from '../../../../myTools/strings.tsx';
import css from '../RequestPanel/PanelCard/PanelCard.module.scss';
import classes from './Body.module.scss';
import Menu from '../../../Screen2/Menu/Menu.tsx';
import {useState, useEffect } from "react";

const Body = () => {
    const [selectedStatus, setSelectedStatus] = useState(localStorage.getItem("selectedStatus") || "Pending");
    const handleStatusChange = (newStatus: string) => {
        setSelectedStatus(newStatus);
        localStorage.setItem("selectedStatus", newStatus);
    };
    
    useEffect(() => {
        localStorage.setItem("selectedStatus", selectedStatus);
    }, [selectedStatus]);
    return <>
        <div className={classes.container}>
        <div className = {css.content}>
            <select name="pets" id="pet-select">
            <option value="">{strings.Subject}</option>
            </select>
            <div className = {css.textBlock}>
                <button className = {css.button} onClick={() => handleStatusChange("Pending")}>
                    {strings.Unverifid}
                    <div className = {css.count}>{}</div>
                </button>
                <button className = {css.button} onClick={() => handleStatusChange("Retake")}>
                    {strings.Retake}
                    <div className = {css.count}>{}</div>
                </button>
                <button className={`${css.button} ${css.button1}`} onClick={() => handleStatusChange("Postponed")}>{strings.Deferred}</button>
                <button className={`${css.button} ${css.button2}`} onClick={() => handleStatusChange("Accepted")}>{strings.Accepted}</button>
                <button className={`${css.button} ${css.button3}`} onClick={() => handleStatusChange("Declined")}>{strings.Rejected}</button>
            </div>
            </div>
            <div className = {classes.content}>
                    <Menu/>
                    <RequestList status={selectedStatus}/>
            </div>
        </div>
    </>
}

export default Body;