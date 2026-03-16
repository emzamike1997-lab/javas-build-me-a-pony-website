```javascript
import React, { useState, useEffect } from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Details from './pages/Details';
import AddPony from './pages/AddPony';
import './App.css';

function App() {
  const [ponies, setPonies] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchPonies();
  }, []);

  const fetchPonies = async () => {
    try {
      const response = await fetch('https://example.com/ponies');
      const data = await response.json();
      setPonies(data);
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div className="App">
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/add-pony">Add Pony</Link>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<Home ponies={ponies} error={error} />} />
        <Route path="/details/:id" element={<Details ponies={ponies} />} />
        <Route path="/add-pony" element={<AddPony />} />
      </Routes>
    </div>
  );
}

export default App;
```

####