import React, { useState } from 'react'
import './Login.scss'
import { useNavigate } from 'react-router-dom'

export default function Login() {

  const navigate = useNavigate()

  const handleSubmit = (e) => {
    e.preventDefault()
    // console.log("Selected Hall:", selectedHall)
    // send login data to backend here
    navigate('/dashboard')
  }

  return (
    <div className="login-container">
      <form className="login-form" onSubmit={handleSubmit}>
        <h2 className="login-title">Login</h2>

        <div className="field">
          <label>ID</label>
          <input type="text" placeholder="Enter your student id" required />
        </div>

        <div className="field">
          <label>Email</label>
          <input type="email" placeholder="Enter your email" required />
        </div>

        <div className="field">
          <label>Password</label>
          <input type="password" placeholder="Enter your password" required />
        </div>

        <button type="submit" className="btn login-btn">Login</button>
      </form>
    </div>
  )
}
