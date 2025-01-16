import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import "../index.css";

interface ChildProps {
  clicked: () => void;
}

type MultFunc = (a: number, b: number) => number;

const Mult: MultFunc = (n1: number, n2: number): number => {
    return n1 * n2;
}

const ChildDecrement = ({ clicked }: ChildProps) => {
  console.log("clicked!");
  return <button onClick={clicked}>DECREMENT HERE</button>;
};

const Practice = () => {
  const [count, setCount] = useState<number>(0);

  const decrement = useCallback(() => {

    setCount((prev) => prev - 1);
  }, []);

  const increment = useCallback(() => {
    setCount((prev) => prev + 1);
  }, []);

  useEffect(() => {
    const handleSize: EventListener = () => {
      console.log("Window Resized!");
    };

    window.addEventListener("resize", handleSize);

    return () => {
      window.removeEventListener("resize", handleSize);
    };
  }, []);

  useEffect(() => {
    console.log("Component Mounted.");

    return () => {
      console.log("Component Unmounted.");
    };
  }, []);


  const inputRef = useRef<HTMLInputElement>(null);
  console.log(inputRef?.current);
  console.log(inputRef.current?.value);
  let num1: number = 4;
  let num2: number = 5;
  let result: number = useMemo<number>(() => Mult(num1, num2), [num1, num2]);

  return (
    <>
      <div>Pratica {count}</div>
      <button onClick={increment}>Adicionar</button>
      <ChildDecrement clicked={decrement} />
      <input ref={inputRef} type="text" />
      <h3>{result}</h3>
    </>
  );
};

export default Practice;
