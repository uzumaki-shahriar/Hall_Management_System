import React from 'react'
import './StudentCard.scss'

export default function StudentCard({ students }) {
    return (
        <div className="students-list">
            {students.map(student => (
                <div className="student-card" key={student.id}>
                    <div className="std-info">
                        <h3>{student.name}</h3>
                        <p>ID:<strong> {student.id}</strong> </p>
                        <p>Batch:<strong> {student.batch}</strong></p>
                        <p>Department:<strong> {student.department}</strong></p>
                    </div>
                </div>
            ))}
        </div>
    )
}
