import React from 'react';
import './Dashboard.scss';
import Sidebar from '../../components/sidebar/Sidebar';

export default function Dashboard() {
  const hallStats = [
    { id: 1, title: 'Total Students', value: 400 },
    { id: 2, title: 'Rooms', value: 120 }
  ];

  const hallName = "Kabi Kazi Nazrul Islam Hall";

  const feedbacks = [
    {
      id: 1,
      text: "I really appreciate the efforts of the hostel staff in maintaining cleanliness and order, but I have noticed that the Wi-Fi connectivity in my room is extremely unstable, especially during peak hours, which makes it difficult to attend online classes and complete assignments on time."
    },
    {
      id: 2,
      text: "The dining hall provides a decent variety of food, but I feel that the portion sizes are sometimes too small and the quality of certain dishes, like the rice and curry, could be improved. It would also be helpful if there were more vegetarian options available consistently."
    },
    {
      id: 3,
      text: "While the common areas of the hall are generally well-maintained, I have observed that the laundry service often takes longer than expected to return clothes, and sometimes the machines are out of order, causing inconvenience for students who rely on them."
    },
    {
      id: 4,
      text: "I am satisfied with the study environment in my room and the quiet hours, but I have noticed that the library lacks enough seating and some of the books are outdated. Adding more modern study materials and increasing seating capacity would greatly benefit all students."
    },
    {
      id: 5,
      text: "The hostel security is generally reliable, and I feel safe within the premises, but I believe that more frequent night patrols and better lighting around the hostel’s exterior areas could further enhance safety, especially for students returning late from the library or labs."
    }
    // Add more feedbacks here...
  ];

  return (
    <div className="page">
      <Sidebar />
      <div className="dashboard-container main">
        <header className="header">
          <h1>{hallName}</h1>
        </header>

        {/* Hall Stats */}
        <div className="dashboard-stats">
          <h3>Hall Information</h3>
          <section className="hall-stats">
            {hallStats.map((stat) => (
              <div className="stat-card" key={stat.id}>
                <h2>{stat.value}</h2>
                <p>{stat.title}</p>
              </div>
            ))}
          </section>
        </div>

        {/* Feedbacks */}
        <div className="dashboard-content">
          <h3>My Feedbacks</h3>
          <section className="feedback-list">
            {feedbacks.length === 0 ? (
              <p>No feedback yet</p>
            ) : (
              feedbacks.map((fb) => (
                <div className="feedback-card" key={fb.id}>
                  {/* <h2>ID: {fb.id}</h2> */}
                  <p>{fb.text}</p>
                </div>
              ))
            )}
          </section>
        </div>
      </div>
    </div>
  );
}
