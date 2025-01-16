import { useCallback, useEffect, useMemo, useRef, useState } from "react";

interface User {
  id: number;
  username: string;
}

type fibFunc = (n: number) => number;

const fibo: fibFunc = (n) => {
  if (n < 2) return n;
  return fibo(n - 1) + fibo(n - 2);
};

const myNum: number = 37;

const Lesson = () => {
  const [count, setCount] = useState<number>(0);
  const [users] = useState<User[] | null>(null);

  const inputRef = useRef<HTMLInputElement>(null);

  console.log(inputRef?.current);
  console.log(inputRef?.current?.value);

  useEffect(() => {
    console.log("Mounting");
    console.log("Users: ", users);

    return () => console.log("Unmounting");
  }, [users]);

  const addTwo = useCallback((): void => setCount((prev) => prev + 2), []);

  const result = useMemo<number>(() => fibo(myNum), [myNum]);

  return (
    <div
      style={{
        marginBottom: "30px",
        borderBottom: "1px solid black",
        padding: "20px",
        textAlign: "center",
      }}
      className="App"
    >
      <h1>{count}</h1>
      <button onClick={addTwo}>Add</button>
      <h2>{result}</h2>
      <input ref={inputRef} type="text"></input>
    </div>
  );
};

export default Lesson;
