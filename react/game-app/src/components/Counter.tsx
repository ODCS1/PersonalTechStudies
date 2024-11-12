import { useState } from "react";
import Button from "./Button";

function Counter () {
    // return <p>HELLOW</p>;

    const [clicked, setClicked] = useState(0);

    return (
        <>
            <br />

            <h2>Counter Clicks</h2>

            <br />

            <p>
                {/* <button type="button" className="btn btn-outline-primary" onClick={() => setClicked(clicked + 1)}>Click Here</button> */}
                <Button onClick={() => setClicked(clicked + 1)} 
                        label="Click Here" 
                        className="btn btn-outline-primary"
                />
                <span> - </span>
                <Button onClick={() => setClicked(0)} 
                        label="Clear" 
                        className="btn btn-outline-danger"
                />
                {/* <button type="button" className="btn btn-outline-danger" onClick={() => setClicked(0)}>Clear</button> */}
            </p>

            <br />
            
            <p>
                COUNTER:  { clicked } times!
            </p>
        </>
    );
}

export default Counter;