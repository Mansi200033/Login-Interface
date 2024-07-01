import React, { useState, useEffect } from 'react';
import "./LoginPage.css";
import Logo from '../../Assets/Images/Logo.svg';
import Axios from 'axios';
import { useNavigate } from 'react-router-dom';
const LoginPage = () => {
  const navigate = useNavigate();
  const [data, setData] = useState({
    Username: "",
    Password: ""
  });
  const [isButtonDisabled, setIsButtonDisabled] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  useEffect(() => {
    if (data.Username && data.Password) {
      setIsButtonDisabled(false);
    } else {
      setIsButtonDisabled(true);
    }
  }, [data]);
  function handle(e) {
    const newdata = { ...data };
    newdata[e.target.id] = e.target.value;
    setData(newdata);
    console.log(newdata);
  }
  const url = 'http://127.0.0.1:8000/api/login/';
  function submit(e) {
    e.preventDefault();
    setIsButtonDisabled(true);
    setIsLoading(true);
    Axios.post(url, data).then(res => {
      console.log(res.data);
      console.log(res.data.token);
      
      if (res.data.status === 200) {
        console.log("this is working");
        setData({
          Username: "",
          Password: ""
        });
        navigate("/home");
        localStorage.setItem("tokens", res.data.token.access)
      } else {
        alert(res.data.message);
        setIsButtonDisabled(false);
        setIsLoading(false);
        setData({
          Username: "",
          Password: ""
        });
      }
    }).catch(err => {
      console.log(err);
      setIsButtonDisabled(false);
      setIsLoading(false);
    });
  }
  return (
    <div className='login'>
      <div className="login-container">
        <div className="login-logo">
          <img src={Logo} alt="logo" width={400} />
        </div>
        <div className='login-form'>
          <form onSubmit={(e) => submit(e)}>
            <label htmlFor="Username">Username</label>
            <input
              type='text'
              placeholder='Username'
              id='Username'
              value={data.Username}
              onChange={(e) => handle(e)}
              disabled={isLoading}
            />
            <label htmlFor="Password">Password</label>
            <input
              type='password'
              placeholder='Password'
              id='Password'
              value={data.Password}
              onChange={(e) => handle(e)}
              disabled={isLoading}
            />
            <a href="/">Forgot password?</a>
            <button type='submit' disabled={isButtonDisabled || isLoading}>
             Login
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
export default LoginPage;