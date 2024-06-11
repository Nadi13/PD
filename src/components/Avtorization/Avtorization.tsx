import React, { useState } from "react";
import css from './Avtorization.module.scss'
import strings from '../../myTools/strings.tsx';

const LoginForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  //const submitForm = (e) => {
    //e.preventDefault();
    // Здесь вы можете отправить запрос на сервер для аутентификации.
    //if (username === "admin" && password === "password") {
      //alert("Успешная авторизация!");
    ///} else {
      //setError("Неверные учетные данные");
    //}
  //};

  return (
        <div className = {css.container}>
            <form className = {css.form}>
                <div className = {css.textBlock}>
                    <text className = {css.title}>{strings.Avtorization}</text>
                    <text className = {css.subtitle}>{strings.Subtitle}</text>
                </div>
                <div className = {css.block}>
                <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} className = {css.login} placeholder={strings.Login}/>
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className = {css.login} placeholder={strings.Password} />
                </div>
                <div className = {css.choice}>
                    <button className={css.reg}>{strings.Registration}</button>
                    <button className={css.logIn}>{strings.Into}</button>
                </div>
            </form>
        </div>
  );
};

export default LoginForm;