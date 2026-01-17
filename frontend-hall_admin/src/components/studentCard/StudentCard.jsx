import React from 'react'
import './StudentCard.scss'

export default function StudentCard({ student, onClose }) {
    if (!student) return null

    return (
        <div className="student-card-overlay">
            <div className="student-card">

                <h2>Student Details</h2>

                <div className="info">
                    <p>ID: <strong>{student.id}</strong></p>
                    <p>Name: <strong>{student.name}</strong></p>
                    <p>Batch: <strong>{student.batch}</strong></p>
                    <p>Department: <strong>{student.department}</strong></p>
                    <p>Room No: <strong>{student.room}</strong></p>
                    <p>Email: <strong>{student.email}</strong></p>
                    <p>Phone: <strong>{student.phone}</strong></p>
                    <p>Address: <strong>{student.address}</strong></p>
                </div>

                <button className="close-btn btn" onClick={onClose}>Close</button>
            </div>
        </div>
    )
}
