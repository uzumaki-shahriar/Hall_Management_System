import React from 'react'
import './DinningApplication.scss'
import Sidebar from '../../components/sidebar/Sidebar'

export default function DinningApplication() {
    const applications = [
        {
            id: '2021201',
            name: 'Zarif Ahmed',
            batch: '21',
            department: 'CSE',
        },
        {
            id: '2021215',
            name: 'Rafiul Islam',
            batch: '21',
            department: 'EEE',
        },
        {
            id: '2020305',
            name: 'Mahmud Hasan',
            batch: '20',
            department: 'ME',
        },
        {
            id: '2022209',
            name: 'Tanvir Rahman',
            batch: '22',
            department: 'CE',
        }
    ]

    return (
        <div className="page">
            <Sidebar />
            <div className="dinning-application-container main">
                <header className="header">
                    <h1>Dinning Applications</h1>
                </header>

                <div className="applications-list">
                    {applications.map(app => (
                        <div className="application-card" key={app.id}>
                            <div className="std-info">
                                <h3>{app.name}</h3>
                                <p>ID:<strong> {app.id}</strong> </p>
                                <p>Batch:<strong> {app.batch}</strong></p>
                                <p>Department:<strong> {app.department}</strong></p>
                            </div>
                            <button className="appointment-btn btn">Appoint as Dinning Manager</button>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}
