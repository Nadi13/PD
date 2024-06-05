import classes from './RequestList.module.scss'
import RequestCard from './Request/RequestCard'
import { useNavigate } from "react-router-dom";


const requests = [
    { name: 'Юдинцева Надежда Ивановна', number: 'МО-211/2', work: '3', course: '3 курс, 2 сем', date: 'пт, 1 апр., 16:34', deadline: true},
    { name: 'Филякин Артем Дмитриевич', number: 'МО-211/2', work: '2', course: '3 курс, 2 сем', date: 'пт, 3 фев., 13:40', deadline: true},
    { name: 'Савченко София Дмитриевна', number: 'ФИТ-211/2', work: '1', course: '3 курс, 2 сем', date: 'пт, 13 фев., 22:43' },
    { name: 'Аникина Софья Дмитриевна', number: 'МО-211/1', work: '2', course: '3 курс, 2 сем', date: 'пт, 14 мая, 16:20' },
    { name: 'Бугаенко Иван Евгеньевич', number: 'ФИТ-212/1', work: '1', course: '3 курс, 2 сем', date: 'пт, 14 апр., 19:14' },
]


const RequestList = () => {
    const navigate = useNavigate();
    return <>
    <div className = {classes.container}>
        <div className={classes.wrap}>
            {requests.map((item) => 
                <RequestCard
                    name={item.name}
                    number={item.number}
                    work={item.work}
                    course={item.course}
                    date={item.date}
                    deadline={item.deadline}
                    onClick={() => navigate("/LabInfo", {state: item})}
                />
            )}
        </div>
        </div>
    </>
}

export default RequestList;