import React from 'react'
import './Payment.scss'
import Sidebar from '../../components/sidebar/Sidebar'

export default function Payment() {

  // Hall Fees: amount, level, term
  const hallFees = [
    { id: 1, amount: 15000, level: 1, term: 1 },
    { id: 2, amount: 16000, level: 1, term: 2 },
  ];

  // Dining Fees: amount, month, year
  const diningFees = [
    { id: 1, amount: 5000, month: 'January', year: 2026 },
  ];

  return (
    <div className='page'>
      <Sidebar />
      <div className="main">
        <header className="header">
          <h1>Pay Fees</h1>
        </header>

        <div className="fees-section">
          <section className="hall-fees">
            <h2>Hall Fees</h2>
            <div className="fees">
              {hallFees.map(fee => (
                <div className="fee-card" key={fee.id}>
                  <p>Level: <strong>{fee.level}</strong></p>
                  <p>Term: <strong>{fee.term}</strong></p>
                  <p>Amount: <strong>{fee.amount} BDT</strong></p>
                  <button className="btn pay-btn">Pay Now</button>
                </div>
              ))}
            </div>
          </section>

          <section className="dining-fees">
            <h2>Dining Fees</h2>
            <div className="fees">
              {diningFees.map(fee => (
                <div className="fee-card" key={fee.id}>
                  <p>Month: <strong>{fee.month}</strong></p>
                  <p>Year: <strong>{fee.year}</strong></p>
                  <p>Amount: <strong>{fee.amount} BDT</strong></p>
                  <button className="btn pay-btn">Pay Now</button>
                </div>
              ))}
            </div>
          </section>
        </div>
      </div>
    </div>
  )
}
