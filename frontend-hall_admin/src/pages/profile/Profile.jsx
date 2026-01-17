import React, { useState } from 'react'
import './Profile.scss'
import Sidebar from '../../components/sidebar/Sidebar'

export default function Profile() {
    // Dummy data objects
    const hallData = {
        name: 'Kabi Kazi Nazrul Islam Hall',
        totalRooms: 120,
        university: 'Chittagong University of Engineering & Technology',
        totalStudents: 400
    }

    const adminData = {
        email: 'admin@hall.edu',
        contactNumber: '017XXXXXXXX'
    }

    const [currentPass, setCurrentPass] = useState('')
    const [newPass, setNewPass] = useState('')
    const [confirmPass, setConfirmPass] = useState('')

    const handleChangePassSubmit = (e) => {
        e.preventDefault()
        if (newPass !== confirmPass) {
            alert('New password and confirm password do not match!')
            return
        }
        console.log('Password changed:', { currentPass, newPass })
        setCurrentPass('')
        setNewPass('')
        setConfirmPass('')
    }

    return (
        <div className='page'>
            <Sidebar />
            <div className='main'>
                <header className='header'>
                    <h1>Profile</h1>
                </header>

                <div className='profile-sections'>

                    {/* Hall Details Display */}
                    <section className='profile-section'>
                        <h2>Hall Details</h2>
                        <div className='profile-display'>
                            <p><strong>Hall Name:</strong> {hallData.name}</p>
                            <p><strong>University:</strong> {hallData.university}</p>
                            <p><strong>Total Rooms:</strong> {hallData.totalRooms}</p>
                            <p><strong>Total Students:</strong> {hallData.totalStudents}</p>
                        </div>
                    </section>

                    {/* Admin Details Display */}
                    <section className='profile-section'>
                        <h2>Admin Details</h2>
                        <div className='profile-display'>
                            <p><strong>Email:</strong> {adminData.email}</p>
                            <p><strong>Contact Number:</strong> {adminData.contactNumber}</p>
                        </div>
                    </section>

                    {/* Change Admin Password */}
                    <section className='profile-section'>
                        <h2>Change Password</h2>
                        <form onSubmit={handleChangePassSubmit}>
                            <label>Current Password</label>
                            <input
                                type='password'
                                value={currentPass}
                                onChange={e => setCurrentPass(e.target.value)}
                                required
                            />

                            <label>New Password</label>
                            <input
                                type='password'
                                value={newPass}
                                onChange={e => setNewPass(e.target.value)}
                                required
                            />

                            <label>Confirm New Password</label>
                            <input
                                type='password'
                                value={confirmPass}
                                onChange={e => setConfirmPass(e.target.value)}
                                required
                            />

                            <button type='submit' className='profile-btn btn'>Change Password</button>
                        </form>
                    </section>

                </div>
            </div>
        </div>
    )
}
