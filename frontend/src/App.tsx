import { useState, useEffect } from 'react'
import { api } from './api'
import { type Garment } from './Models'

function App() {
    const [garments, setGarments] = useState<Garment[]>([])

    useEffect(() => {
        const fetchGarments = async () => {
            const res = await api.get('/garments')
            setGarments(res.data)
        }

        fetchGarments().then(r => void r)
    }, [])

    return (
        <div>
            <h1>My Wardrobe</h1>
            <ul>
                {garments.map(garment => (
                    <li key={garment.id}>
                        {garment.brand} {garment.type} - {garment.color} - Size: {garment.size}
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default App