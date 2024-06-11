import css from './PanelCard.module.scss'
import strings from '../../../../../myTools/strings.tsx';
import cards from '../../RequestList/RequestList.tsx'
import { useState } from "react";

const PanelCard = () => {
    const [selectedStatus, setSelectedStatus] = useState("Pending");

    const handleStatusChange = (newStatus: string) => {
        setSelectedStatus(newStatus);
    };
    
    return <>
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
                <button className={`${css.button} ${css.button3}`} onClick={() => handleStatusChange("Rejected")}>{strings.Rejected}</button>
            </div>
            </div>
    </>
}
export default PanelCard;

