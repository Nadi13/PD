import classes from './Header.module.scss'
import TopNavBar from './TopNavBar/TopNavBar';


const Header = () => {
    return <>
        <header className={classes.header}>
            <div className={classes.elements}>
                <TopNavBar />
                <div className={classes.notification}>
                    <img src="src/assets/notification.png" alt="Уведомления" />
                </div>
                <div className={classes.icon}>
                    <div className={classes.circleWrap}>
                        <span className={classes.iconTypography}>K</span>
                    </div>
                </div>
            </div>
        </header>
    </>
}

export default Header;
