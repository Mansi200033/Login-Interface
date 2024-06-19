import React from 'react'
import { useState } from 'react';
import "./LoginPage.css"
import Logo from '../../Assets/Images/Logo.svg'
import Axios from 'axios'
const LoginPage = () => {
  const [data, setData] = useState({
    Username:"",
    Password:""
  })
  
  
  function handle(e){
    const newdata = {...data}
    newdata[e.target.id] = e.target.value
    setData(newdata)
    console.log(newdata)
  }


  const url = 'http://127.0.0.1:8000/api/login/'
  function submit(e){
    e.preventDefault()
    Axios.post(url,data).then(res =>{
      console.log(res.data)
    }).catch(err=>{
      console.log(err)
    })
  }
  return (
    <>
    <div className='login'>
      <div className="login-container">
    <div className="login-logo">
        <img src={Logo} alt="logo"  width={400} />
    </div>
    <div className='login-form'>
  <form onSubmit={(e)=> submit(e)}>
    <label htmlFor="/">Username</label>
    <input type='Username' placeholder='Username' id='Username' value={data.Username} onChange={(e)=> handle(e)}/>
   <label htmlFor="/"> Password</label>
    <input type='Password' placeholder='Password' id='Password' value={data.Password} onChange={(e)=> handle(e)}/>
    <a href="/">Forgot password?</a>

    <button type='submit'>Login</button>
    
    
  </form>
  </div>
 </div>
  
    </div>
    </>
  )
}

export default LoginPage;
