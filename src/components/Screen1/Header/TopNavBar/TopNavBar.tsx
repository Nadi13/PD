import classes from './TopNavBar.module.scss'

const TopNavBar = () => {
    return <>
        <nav className={classes.container}>
            <span className={`${classes.elem} ${classes.selected}`}>
                <div className={classes.selectedTypography}>Запросы на проверку</div>
            </span>
            <span className={classes.elem}>Ведомости по лабораторным</span>
            <span className={classes.elem}>Памятка студентам</span>
            <span className={classes.elem}>Лабораторные работы</span>
        </nav>
    </>
}

export default TopNavBar;