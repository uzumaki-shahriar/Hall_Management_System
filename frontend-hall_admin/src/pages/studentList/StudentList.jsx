import React, { useState } from 'react'
import './StudentList.scss'
import Sidebar from '../../components/sidebar/Sidebar'
import StudentCard from '../../components/studentCard/StudentCard';
import { TiUserDeleteOutline } from "react-icons/ti";

export default function StudentList() {
    const [students, setStudents] = useState([
        {
            id: '2021201',
            name: 'Rahim Uddin',
            batch: '21',
            department: 'CSE',
            room: 201,
            email: 'rahim21@student.edu',
            phone: '017XXXXXXXX',
            address: 'Chattogram'
        },
        {
            id: '2021215',
            name: 'Karim Hasan',
            batch: '21',
            department: 'EEE',
            room: 305,
            email: 'karim21@student.edu',
            phone: '018XXXXXXXX',
            address: 'Dhaka'
        },
        {
            id: '2020305',
            name: 'Mahmud Ali',
            batch: '20',
            department: 'ME',
            room: 112,
            email: 'mahmud20@student.edu',
            phone: '019XXXXXXXX',
            address: 'Rajshahi'
        },
        {
            id: '2022209',
            name: 'Tanvir Hossain',
            batch: '22',
            department: 'CE',
            room: 210,
            email: 'tanvir22@student.edu',
            phone: '016XXXXXXXX',
            address: 'Khulna'
        }
    ])

    const [selectedStudent, setSelectedStudent] = useState(null)

    const handleDelete = (id, e) => {
        e.stopPropagation() // prevent row click
        setStudents(students.filter(student => student.id !== id))
    }

    return (
        <div className='page'>
            <Sidebar />
            <div className='main'>
                <header className='header'>
                    <h1>Student List</h1>
                </header>

                <div className='table-wrapper'>
                    <table className='student-table'>
                        <thead>
                            <tr>
                                <th>Student ID</th>
                                <th>Name</th>
                                <th>Batch</th>
                                <th>Department</th>
                                <th>Room No</th>
                                <th></th>
                            </tr>
                        </thead>

                        <tbody>
                            {students.map(student => (
                                <tr key={student.id} onClick={() => setSelectedStudent(student)}>
                                    <td>{student.id}</td>
                                    <td>{student.name}</td>
                                    <td>{student.batch}</td>
                                    <td>{student.department}</td>
                                    <td>{student.room}</td>
                                    <td>
                                        <button
                                            className='delete-btn'
                                            onClick={(e) => handleDelete(student.id, e)}
                                        >
                                            <TiUserDeleteOutline />
                                        </button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>

                {/* Student Card Modal */}
                <StudentCard
                    student={selectedStudent}
                    onClose={() => setSelectedStudent(null)}
                />
            </div>
        </div>
    )
}
