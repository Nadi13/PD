import classes from './PanelCard.module.scss'

const PanelCard = (props: { type: string, number?: string, color: string }) => {
    return <>
        <div className={classes.container} style={{ backgroundColor: props.color }}>
            <div className={classes.text}>
                {props.type}
                {props.number && <span style={{ color: '#9E1D1A', fontSize: '13px', fontWeight: 'medium', marginLeft: '7px' }}> {props.number}</span>}
            </div>
        </div>
    </>
}
export default PanelCard;

