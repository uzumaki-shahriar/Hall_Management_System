import { useState } from 'react'
import './App.scss'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './pages/home/Home'
import Login from './pages/login/Login'
import Dashboard from './pages/dashboard/Dashboard'
import WriteFeedback from './pages/writeFeedback/WriteFeedback'
import Profile from './pages/profile/Profile'
import Payment from './pages/payment/Payment'
import DiningManagement from './pages/diningManagement/DiningManagement'

function App() {
  // const [count, setCount] = useState(0)

  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/login' element={<Login />} />
          <Route path='/dashboard' element={<Dashboard />} />
          <Route path='/write-feedback' element={<WriteFeedback />} />
          <Route path='/profile' element={<Profile />} />
          <Route path='/payment' element={<Payment />} />
          <Route path='/dining-mangement' element={<DiningManagement />} />
        </Routes>

      </Router>
    </div>
  )
}

export default App
