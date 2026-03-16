```javascript
import React from 'react';

function Details({ ponies }) {
  const id = window.location.pathname.split('/').pop();
  const pony = ponies.find((pony) => pony.id === parseInt(id));

  if (!pony) {
    return <div>Pony not found</div>;
  }

  return (
    <div>
      <h1>{pony.name}</h1>
      <p>Age: {pony.age}</p>
      <p>Breed: {pony.breed}</p>
    </div>
  );
}

export default Details;
```

####