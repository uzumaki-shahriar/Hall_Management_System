import React from 'react'
import './AddStudent.scss'
import Sidebar from '../../components/sidebar/Sidebar'

export default function AddStudent() {
    return (
        <div className="page">
            <Sidebar />
            <div className="add-student-container main">
                <header className="header">
                    <h1>Add New Student</h1>
                </header>

                <div className="form-container">
                    <form className="add-student-form">
                        <div className="form-group">
                            <label>Student ID</label>
                            <input type="text" placeholder="Enter student ID" />
                        </div>

                        <div className="form-group">
                            <label>Student Name</label>
                            <input type="text" placeholder="Enter student name" />
                        </div>

                        <div className="form-group">
                            <label>Batch</label>
                            <input type="text" placeholder="Enter student's batch" />
                        </div>

                        <div className="form-group">
                            <label>Department</label>
                            <input type="text" placeholder="Enter student's department" />
                        </div>

                        <div className="form-group">
                            <label>Room No</label>
                            <input type="text" placeholder="Enter room number" />
                        </div>

                        <button type="submit" className='btn add-std-btn' style={{fontSize: '1.5rem'}}>Add Student</button>
                    </form>
                </div>
            </div>
        </div>
    )
}
