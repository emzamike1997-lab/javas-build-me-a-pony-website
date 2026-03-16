```javascript
import React from 'react';
import { Link } from 'react-router-dom';

function Home({ ponies, error }) {
  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h1>Ponies</h1>
      <ul>
        {ponies.map((pony) => (
          <li key={pony.id}>
            <Link to={`/details/${pony.id}`}>
              {pony.name}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Home;
```

####