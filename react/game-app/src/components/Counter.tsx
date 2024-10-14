import { useState } from "react";

function Counter () {
    // return <p>HELLOW</p>;

    const [clicked, setClicked] = useState(0);

    return (
        <>
            <br />

            <h2>Counter Clicks</h2>

            <br />

            <p>
                <button onClick={() => setClicked(clicked + 1)}>Click Here</button>
                <span> - </span>
                <button onClick={() => setClicked(0)}>Clear</button>
            </p>

            <br />
            
            <p>
                COUNTER:  { clicked } times!
            </p>
        </>
    );
}

export default Counter;