import React from 'react';
import './Dashboard.scss';
import Sidebar from '../../components/sidebar/Sidebar';

export default function Dashboard() {
  const stats = [
    { id: 1, title: 'Total Students', value: 400 },
    { id: 2, title: 'Rooms', value: 120 },
    { id: 3, title: 'Dinning Applications', value: 57 },
    { id: 4, title: 'Total Feedbacks', value: 430 },
  ];

  const hallName = "Kabi Kazi Nazrul Islam Hall";

  const dinningManagers = [
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
    }
  ]

  // Dummy applications
  const applications = [
    { id: 'S101', name: 'Kamal Ahmed', room: 201 },
    { id: 'S102', name: 'Nadim Rahman', room: 305 },
    { id: 'S103', name: 'Rafiq Khan', room: 112 },
    { id: 'S104', name: 'Zamal Khan', room: 210 },
  ];

  // Dummy feedbacks
  const feedbacks = [
    { id: 'S101', name: 'Kamal Ahmed', text: 'The internet is very slow.' },
    { id: 'S105', name: 'Sadiq Hossain', text: 'The dining hall needs more staff.' },
    { id: 'S103', name: 'Rafiq Khan', text: 'Washrooms are not clean enough.' },
    { id: 'S106', name: 'Rinku Islam', text: 'Please extend the library hours.' },
  ];

  return (
    <div className="page">
      <Sidebar />
      <div className="dashboard-container main">
        <header className="header">
          <h1>{hallName}</h1>
        </header>

        <div className="dashboard-stats">
          <section className="hall-stats">
            {stats.map((stat) => (
              <div className="stat-card" key={stat.id}>
                <h2>{stat.value}</h2>
                <p>{stat.title}</p>
              </div>
            ))}
          </section>
          <div className="dinning-managers">
            <h3>Dinning Managers</h3>
            {dinningManagers.length === 0 ? (
              <p>No data yet</p>
            ) : (
              <div className="mangers-list">
                {dinningManagers.map(manager => (
                  <div className="manger-card" key={manager.id}>
                    <div className="std-info">
                      <h3>{manager.name}</h3>
                      <p>ID: <strong>{manager.id}</strong></p>
                      <p>Batch: <strong>{manager.batch}</strong></p>
                      <p>Department: <strong>{manager.department}</strong></p>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>

        </div>

        <section className="dashboard-content">
          <div className="content-card">
            <h3>Recent Dinning Applications</h3>
            {applications.length === 0 ? (
              <p>No data yet</p>
            ) : (
              <ul>
                {applications.map((app) => (
                  <li key={app.id}>
                    <strong>{app.name}</strong> (ID: {app.id}) - Room {app.room}
                  </li>
                ))}
              </ul>
            )}
          </div>

          <div className="content-card">
            <h3>Recent Feedbacks</h3>
            {feedbacks.length === 0 ? (
              <p>No data yet</p>
            ) : (
              <ul>
                {feedbacks.map((fb) => (
                  <li key={fb.id}>
                    <strong>{fb.name}</strong> (ID: {fb.id}): {fb.text}
                  </li>
                ))}
              </ul>
            )}
          </div>
        </section>
      </div>
    </div>
  );
}
