import { useState } from 'react'
import './App.scss'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './pages/home/Home'
import Login from './pages/login/Login'
import Dashboard from './pages/dashboard/Dashboard'
import AddStudent from './pages/addStudent/AddStudent'
import DinningApplication from './pages/dinningApplication/DinningApplication'
import Feedbacks from './pages/feedbacks/Feedbacks'
import StudentList from './pages/studentList/StudentList'
import Profile from './pages/profile/Profile'

function App() {
  // const [count, setCount] = useState(0)

  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/login' element={<Login />} />
          <Route path='/dashboard' element={<Dashboard />} />
          <Route path='/add-student' element={<AddStudent />} />
          <Route path='/dinning-applications' element={<DinningApplication />} />
          <Route path='/feedbacks' element={<Feedbacks />} />
          <Route path='/student-list' element={<StudentList />} />
          <Route path='/profile' element={<Profile />} />
        </Routes>

      </Router>
    </div>
  )
}

export default App
