import classes from './RequestList.module.scss'
import RequestCard from './Request/RequestCard'

const requests = [
    { name: 'Имя Фамилия Отчество', number: 'ФИТ-211/2', work: '3', course: '3 курс, 1 сем', date: 'пт, 1 дек., 16:34', deadline: true},
    { name: 'Имя Фамилия Отчество', number: 'ФИТ-211/1', work: '2', course: '3 курс, 1 сем', date: 'пт, 3 дек., 13:40', deadline: true},
    { name: 'Имя Фамилия Отчество', number: 'ФИТ-212/2', work: '1', course: '3 курс, 1 сем', date: 'пт, 13 дек., 22:43' },
    { name: 'Имя Фамилия Отчество', number: 'ФИТ-211/1', work: '2', course: '3 курс, 1 сем', date: 'пт, 14 дек., 16:20' },
    { name: 'Имя Фамилия Отчество', number: 'МО-211/2', work: '1', course: '3 курс, 1 сем', date: 'пт, 14 дек., 19:14' },
]

const RequestList = () => {
    return <>

        <div className={classes.wrap}>
            {
                requests.map(
                    (item) =>
                        <RequestCard name={item.name} number={item.number} work={item.work} course={item.course} date={item.date} deadline={item.deadline}/>
                )
            }
        </div>
    </>
}

export default RequestList;