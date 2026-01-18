import React, { useState } from 'react'
import './Profile.scss'
import Sidebar from '../../components/sidebar/Sidebar'

export default function Profile() {
    // Dummy data objects
    // const hallData = {
    //     name: 'Kabi Kazi Nazrul Islam Hall',
    //     totalRooms: 120,
    //     university: 'Chittagong University of Engineering & Technology',
    //     totalStudents: 400
    // }

    const studentData = {
        id: 'STD-1023',
        name: 'Student Name',
        email: 'student@hall.edu',
        batch: '22',
        department: 'Computer Science & Engineering',
        homeAddress: 'Chattogram, Bangladesh',
        contactNumber: '017XXXXXXXX',
        roomNumber: 'B-214'
    }

    const [contactNumber, setContactNumber] = useState(studentData.contactNumber)
    const [homeAddress, setHomeAddress] = useState(studentData.homeAddress)

    const handleEditInfoSubmit = (e) => {
        e.preventDefault()
        if (!homeAddress.trim() || !contactNumber.trim()) {
            alert('Please fill in both fields!')
            return
        }
        console.log('Updated Info:', { contactNumber, homeAddress })
        alert('Contact information updated successfully!')
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

                    {/* Student Details Display */}
                    <section className='profile-section'>
                        <h2>Student Details</h2>
                        <div className='profile-display'>
                            <p><strong>ID:</strong> {studentData.id}</p>
                            <p><strong>Name:</strong> {studentData.name}</p>
                            <p><strong>Email:</strong> {studentData.email}</p>
                            <p><strong>Batch:</strong> {studentData.batch}</p>
                            <p><strong>Department:</strong> {studentData.department}</p>
                            <p><strong>Home Address:</strong> {studentData.homeAddress}</p>
                            <p><strong>Contact Number:</strong> {studentData.contactNumber}</p>
                            <p><strong>Room Number:</strong> {studentData.roomNumber}</p>
                        </div>
                    </section>

                    {/* Edit Info */}
                    <section className="profile-section">
                        <h2>Edit Contact Information</h2>
                        <form onSubmit={handleEditInfoSubmit} className="edit-contact-form">

                            <label>Home Address</label>
                            <input
                                type="text"
                                value={homeAddress}
                                onChange={e => setHomeAddress(e.target.value)}
                                required
                            />

                            <label>Contact Number</label>
                            <input
                                type="text"
                                value={contactNumber}
                                onChange={e => setContactNumber(e.target.value)}
                                required
                            />

                            <button type="submit" className='profile-btn btn'>Update Info</button>
                        </form>
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
