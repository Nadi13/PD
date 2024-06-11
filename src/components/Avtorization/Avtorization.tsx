import React, { useState } from "react";
import css from './Avtorization.module.scss'
import strings from '../../myTools/strings.tsx';
import { useEffect} from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';

const LoginForm = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e:React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    const response = await fetch('http://127.0.0.1:8000/api/user/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });

    const data = await response.json();

    if (response.status === 200) {
      navigate('/Main', { state: { user: data } });
    } else {
      setError("Incorrect username or password");
    }
};

  return (
        <div className = {css.container}>
            <form className = {css.form}>
                <div className = {css.textBlock}>
                    <div className = {css.title}>{strings.Avtorization}</div>
                    <div className = {css.subtitle}>{strings.Subtitle}</div>
                </div>
                <div className = {css.block}>
                <input type = "text" value={username} onChange={(e) => setUsername(e.target.value)} className = {css.login} placeholder={strings.Login}/>
                <input type = "password" value={password} onChange={(e) => setPassword(e.target.value)} className = {css.login} placeholder={strings.Password} />
                </div>
                {error && <div className={css.error}>{error}</div>}
                <div className = {css.choice}>
                    <div className={css.reg}>{strings.Registration}</div>
                    <button className={css.logIn} onClick={handleLogin}>{strings.Into}</button>
                </div>
            </form>
        </div>
  );
};

export default LoginForm;