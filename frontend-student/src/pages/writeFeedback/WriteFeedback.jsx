import React, { useState } from 'react'
import './WriteFeedback.scss'
import Sidebar from '../../components/sidebar/Sidebar'

export default function WriteFeedback() {
  const [feedback, setFeedback] = useState('')

  const handleSubmit = () => {
    if (!feedback.trim()) return
    console.log(feedback)
    setFeedback('')
  }

  return (
    <div className='page'>
      <Sidebar />
      <div className="feedback-container main">
        <header className="header">
          <h1>Write Feedback</h1>
        </header>

        <div className="feedback-box">
          <textarea
            value={feedback}
            onChange={(e) => setFeedback(e.target.value)}
            placeholder="Write your feedback here..."
          />
          <button className="feedback-submit-btn btn" onClick={handleSubmit}>
            Submit Feedback
          </button>
        </div>
      </div>
    </div>
  )
}
