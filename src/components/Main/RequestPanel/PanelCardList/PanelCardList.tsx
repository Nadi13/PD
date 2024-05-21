import PanelCard from '../PanelCard/PanelCard'
import classes from './PanelCardList.module.scss'

const elements = [
    { type: 'Непроверенные работы', number: '9', color: '#FFFFFF' },
    { type: 'Повторная сдача', number: '2', color: '#FFFFFF' },
    { type: 'Отложенные работы', color: '#FFF6DC' },
    { type: 'Принятые работы', color: '#F3FFEB' },
    { type: 'Отклоненные работы', color: '#FFCFCE' }
]

const PanelCardList = () => {
    return <>

        <div className={classes.wrap}>
            {
                elements.map((item) => <PanelCard type={item.type} number={item.number} color={item.color} />)
            }
        </div>
    </>
}

export default PanelCardList;