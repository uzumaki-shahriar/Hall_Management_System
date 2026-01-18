import React from 'react'
import './DiningDataTable.scss'
import { formatDate } from '../../helperFunctions/formatDate'

export default function DiningDataTable({ diningData }) {
    return (
        <div className="dining-tables">
            {diningData.map((day, index) => {
                const totalPrice = day.items.reduce((sum, item) => sum + item.price, 0)

                return (
                    <div className="dining-table" key={index}>
                        <h2 className="date-title">{formatDate(day.date)}</h2>

                        <table>
                            <thead>
                                <tr>
                                    <th>Item</th>
                                    <th>Amount (kg)</th>
                                    <th>Price (৳)</th>
                                </tr>
                            </thead>
                            <tbody>
                                {day.items.map((row, i) => (
                                    <tr key={i}>
                                        <td>{row.item}</td>
                                        <td>{row.amount}</td>
                                        <td>{row.price}</td>
                                    </tr>
                                ))}
                                <tr className="total-row">
                                    <td colSpan={2} style={{ fontWeight: 600 }}>
                                        Total
                                    </td>
                                    <td style={{ fontWeight: 600 }}>{totalPrice}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                )
            })}
        </div>
    )
}
