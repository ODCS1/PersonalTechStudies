import  { useCallback, useRef, useState } from "react";

type CalculateProps = (n1: number, n2: number) => number;

const Calculate:CalculateProps = (n1: number, n2: number) => {
    return n1 * n2;
}


interface ChildProps {
    clicked: () => void;
}

const Child = ({ clicked }: ChildProps) => {
    return <button onClick={clicked}>CALCULATE</button>
}


const Multiplication = () => {

    const ref1 = useRef<HTMLInputElement>(null);
    const ref2 = useRef<HTMLInputElement>(null);
    const [result, setResult] = useState<number | null>(null);


    const handleClick = useCallback(() => {
        const num1 = ref1.current?.value.trim() ? Number(ref1.current.value) : undefined;
        const num2 = ref2.current?.value.trim() ? Number(ref2.current.value) : undefined;

        if (typeof num1 === "undefined" || typeof num2 === "undefined"){
            setResult(null);
            return;
        }


        setResult(Calculate(num1, num2));
    }, []);

  return (
    <>
        <div>
            <input ref={ref1} id="in1" type="text" />
            <input ref={ref2} id="in2" type="text" />
            <Child clicked={handleClick} />
            <span>
                Result: {result !== null ? result : "Enter numbers to calculate!"}
            </span>
            
        </div>
    </>
  );
};

export default Multiplication;
