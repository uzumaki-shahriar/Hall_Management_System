import React from 'react'
import './DiningManagement.scss'
import Sidebar from '../../components/sidebar/Sidebar'

export default function DiningManagement() {
  return (
    <div className='page'>
      <Sidebar />
      <div className="main">
        <header className="header">Dining Management</header>
      </div>
    </div>
  )
}
