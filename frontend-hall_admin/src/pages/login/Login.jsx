import React, { useState } from 'react'
import './Login.scss'
import CustomDropdown from '../../components/customDropdown/CustomDropdown'
import { useNavigate } from 'react-router-dom'

export default function Login() {
  const halls = [
    { id: 1, name: 'Shahid Mohammad Shah Hall' },
    { id: 2, name: 'Sufia Kamal Hall' },
    { id: 3, name: 'Kabi Kazi Nazrul Islam Hall' },
    { id: 4, name: 'Shaheed Tareq Huda Hall' }
  ]

  const [selectedHall, setSelectedHall] = useState(null)

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
          <label>Email</label>
          <input type="email" placeholder="Enter your email" required />
        </div>

        <div className="field">
          <label>Select Hall</label>
          <CustomDropdown
            options={halls.map(h => h.name)}
            value={selectedHall}
            onChange={setSelectedHall}
            placeholder="Choose your hall"
          />
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
