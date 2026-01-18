import React, { useState } from 'react'
import './DiningManagement.scss'
import Sidebar from '../../components/sidebar/Sidebar'
import DiningForm from '../../components/dining/DiningForm'
import DiningDataTable from '../../components/dining/DiningDataTable'
import StudentCard from '../../components/studentCard/StudentCard'

export default function DiningManagement() {
  const diningManagers = [
    { id: '2021201', name: 'Zarif Ahmed', batch: '21', department: 'CSE' },
    { id: '2021215', name: 'Rafiul Islam', batch: '21', department: 'EEE' }
  ]

  const [isDiningManager, setIsDiningManager] = useState(true)

  const [diningData, setDiningData] = useState([
    {
      date: '2026-01-15',
      items: [
        { item: 'Rice', amount: 2, price: 20 },
        { item: 'Chicken Curry', amount: 1.5, price: 60 },
        { item: 'Dal', amount: 1, price: 15 }
      ]
    },
    {
      date: '2026-01-16',
      items: [
        { item: 'Rice', amount: 2, price: 20 },
        { item: 'Fish Curry', amount: 1, price: 55 },
        { item: 'Vegetables', amount: 1.2, price: 18 }
      ]
    }
  ])

  const [formItems, setFormItems] = useState([{ item: '', amount: '', price: '' }])
  const today = new Date().toISOString().split('T')[0]
  const todaysDataExists = diningData.some(day => day.date === today)

  const handleInputChange = (index, field, value) => {
    const newFormItems = [...formItems]
    newFormItems[index][field] = value
    setFormItems(newFormItems)
  }

  const addNewItem = () => setFormItems([...formItems, { item: '', amount: '', price: '' }])

  const saveData = () => {
    const itemsToSave = formItems.map(f => ({
      item: f.item,
      amount: parseFloat(f.amount),
      price: parseFloat(f.price)
    }))
    setDiningData([{ date: today, items: itemsToSave }, ...diningData])
    setFormItems([{ item: '', amount: '', price: '' }])
  }

  return (
    <div className="page">
      <Sidebar />
      <div className="main">
        <header className="header">
          <h1>Dining Management</h1>
        </header>

        {/* Show manager list only if not a dining manager */}
        {!isDiningManager && (
          <div className="manager-list">
            <h2>Current Dining Managers</h2>
            <StudentCard students={diningManagers} />
            <button className="btn apply-btn">Apply To Be Next Dining Manager</button>
          </div>
        )}

        {/* Show form and table only if is dining manager */}
        {isDiningManager && (
          <>
            {!todaysDataExists && (
              <DiningForm
                formItems={formItems}
                handleInputChange={handleInputChange}
                addNewItem={addNewItem}
                saveData={saveData}
              />
            )}

            <DiningDataTable diningData={diningData} />
          </>
        )}
      </div>
    </div>
  )
}
