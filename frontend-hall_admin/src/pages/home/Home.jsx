import React from 'react'
import './Home.scss'
import TypingEffect from '../../components/typingEffect/TypingEffect'
import { useNavigate } from 'react-router-dom'

export default function Home() {


  const navigate = useNavigate();

  const goToLogin = () => {
    navigate('/login');
  }

  return (
    <div className='home-container'>
      <div className="logo">HallMate</div>
      <TypingEffect
        text="Every Student's Companion."
        speed={100}
        cls="slogan"
      />
      <button className="btn goto-login-btn" onClick={goToLogin}>Login as an Admin</button>
    </div>
  )
}
