import React, { useState } from "react";

const Counter = () => {
    const [count, setCount] = useState(0);

    function handleIncrementClick() {
        setCount(prev => prev + 1);
    }

    const handleDecrementClick = () => {
        setCount(count - 1);
    }

  return (
    <div>
        <h2>{count}</h2>
        <button onClick={handleIncrementClick} type="button">Increment</button>
        <button onClick={handleDecrementClick} type="button">Decrement</button>
    </div>
  );
};

export default Counter;
