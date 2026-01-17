import React from 'react'
import './Feedbacks.scss'
import Sidebar from '../../components/sidebar/Sidebar'

export default function Feedbacks() {
    const feedbacks = [
        {
            id: '2021201',
            name: 'Jamil Ahmed',
            text: 'The internet connection in the hall has been extremely slow for the past few weeks. Online classes and assignment submissions are becoming very difficult because of frequent disconnections and high latency, especially during the evening hours.'
        },
        {
            id: '2021215',
            name: 'Rafiul Islam',
            text: 'The quality of food in the dining hall has declined noticeably. Meals are often served cold, and the menu lacks variety. Many students feel that the portion size is also insufficient considering the dining fees we pay.'
        },
        {
            id: '2020305',
            name: 'Mahmud Hasan',
            text: 'Washrooms are not cleaned regularly, especially on higher floors. Broken taps and poor water drainage make the situation worse. This is causing serious hygiene issues and needs immediate attention from the hall authority.'
        },
        {
            id: '2022209',
            name: 'Tanvir Rahman',
            text: 'The common room does not have enough seating arrangements, and most of the chairs are broken. During peak hours, it becomes overcrowded and uncomfortable, making it difficult for students to study or relax.'
        }
    ]

    return (
        <div className='page'>
            <Sidebar />
            <div className='main'>
                <header className='header'>
                    <h1>Feedbacks</h1>
                </header>

                <div className='feedbacks-list'>
                    {feedbacks.map(feedback => (
                        <div className='feedback-card' key={feedback.id}>
                            <div className="std-info">
                                <h3>{feedback.name}</h3>
                                <p>ID:<strong> {feedback.id}</strong></p>
                            </div>
                            <p className='feedback-text'>{feedback.text}</p>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}
