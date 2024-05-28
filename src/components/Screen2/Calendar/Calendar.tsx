import React, { useState } from 'react';
import css from './Calendar.module.scss'

const Calendar = () => {
  const [isCalendarOpen, setIsCalendarOpen] = useState(false);
  const [selectedDate, setSelectedDate] = useState(new Date());

  const toggleCalendar = () => {
    setIsCalendarOpen(!isCalendarOpen);
  };

  const prevDay = () => {
    setSelectedDate(new Date(selectedDate.setDate(selectedDate.getDate() - 1)));
  };

  const nextDay = () => {
    setSelectedDate(new Date(selectedDate.setDate(selectedDate.getDate() + 1)));
  };

  const getDaysInMonth = () => {
    return new Date(selectedDate.getFullYear(), selectedDate.getMonth() + 1, 0).getDate();
  };

  const createCalendar = () => {
    const calendar = [];
  
    for (let i = 1; i <= getDaysInMonth(); i++) {
      calendar.push(<div key={i} className={css.day}>{i}</div>);
    }
  
    return calendar;
  };

  return (
    <div>
      <div className={css.header}>
        <div className={css.prevMonth} onClick={prevDay}>
            <img className={css.img1} src='src/assets/arrow_left.png'></img>
        </div>
        <button className = {css.button} onClick={toggleCalendar}>
        </button>
        <div className={css.date}>
          {selectedDate.toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' })}
        </div>
        <div className={css.nextMonth} onClick={nextDay}>
            <img className={css.img1} src='src/assets/arrow_right.png'></img>
        </div>
      </div>
      {isCalendarOpen && (
        <div className={css.calendaerContent}>
          {createCalendar()}
        </div>
      )}
    </div>
  );
};

export default Calendar;
