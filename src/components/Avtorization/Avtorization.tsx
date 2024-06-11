import React, { useState } from "react";
import css from './Avtorization.module.scss'

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
    <form >
      <label>Имя пользователя:</label>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />

      <label>Пароль:</label>
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />

      <input type="submit" value="Войти" />
      {error && <p style={{ color: "red" }}>{error}</p>}
    </form>
    </div>
  );
};

export default LoginForm;