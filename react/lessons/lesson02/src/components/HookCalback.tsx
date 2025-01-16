import { useState, useCallback } from "react";


/**
 * THE useCallBack HOOK IS USED TO MEMOIZE FUNCTIONS MEANS IT WILL RETURN
 * THE SAME FUNCTION INSTANCE UNLESS ITS DEPENDENCIES CHANGE. THIS IS
 * ESPECIALLY USEFUL WHEN PASSING FUNCTIONS AS PROPS TO CHILD COMPONENTS,
 * TO PREVENT UNNECESSARY RE-RENDERS.
 */


// CHILD COMPONENT WITH EXPLICIT TYPING FOR PROPS
interface ChildProps {
  clicked: () => void;
}

const Child = ({ clicked }: ChildProps) => {
  console.log("CHILD COMPONENT RENDERED!");
  return <button onClick={clicked}>CLICK ME</button>;
};

const HookCallback = () => {

  // STATE TO KEEP TRACK OF COUNT
  const [count, setCount] = useState<number>(0);
  const [otherState, setOtherState] = useState<boolean>(false);

  // useCallback TO MEMIOZE THE CALLBACK FUNCTION
  const incrementCount = useCallback(() => {
    setCount((prevCount) => prevCount + 1);
  }, []); // Empty dependency array means this function is memoized once and does not change unless dependencies change.

  // Another function that doesn't change unless otherState changes
  const toggleOtherState = useCallback(() => {
    setOtherState((prev) => !prev);
  }, [otherState]);

  return (
    <div style={{
        marginBottom: "30px",
        borderBottom: "5px solid black",
        padding: "20px",
        textAlign: "center",
      }}>

      <h2>useCallback Example</h2>
      <p>Count: {count}</p>
      <button onClick={incrementCount}>Increment Count</button>
      <p>Other State: {otherState ? "True" : "False"}</p>
      <button onClick={toggleOtherState}>Toggle Other State</button>

      {/* Child component that uses the memoized function */}
      <Child clicked={incrementCount} />
    </div>
  );
};

export default HookCallback;
