import React from 'react'
import './DiningForm.scss'

export default function DiningForm({ formItems, handleInputChange, addNewItem, saveData }) {
    return (
        <div className="dining-form">
            <h2>Add Today's Dining Items</h2>
            {formItems.map((row, index) => (
                <div className="form-row" key={index}>
                    <span className="item-number">Item {index + 1}</span>
                    <input
                        type="text"
                        placeholder="Item Name"
                        value={row.item}
                        onChange={e => handleInputChange(index, 'item', e.target.value)}
                        required
                    />
                    <input
                        type="number"
                        step="0.01"
                        placeholder="Amount (kg)"
                        value={row.amount}
                        onChange={e => handleInputChange(index, 'amount', e.target.value)}
                        required
                    />
                    <input
                        type="number"
                        step="0.01"
                        placeholder="Price (৳)"
                        value={row.price}
                        onChange={e => handleInputChange(index, 'price', e.target.value)}
                        required
                    />
                </div>
            ))}

            <div className="form-buttons">
                <button type="button" className="btn dining-form-btn" onClick={addNewItem}>
                    Add New Item
                </button>
                <button type="button" className="btn dining-form-btn" onClick={saveData}>
                    Save Data
                </button>
            </div>
        </div>
    )
}
