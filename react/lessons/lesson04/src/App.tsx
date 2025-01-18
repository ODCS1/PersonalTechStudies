import './App.css'
import { CounterProvider } from './context/CounterContext'
import Counter from './Counter'

function App() {

  return (
    <>
      <CounterProvider>
        <Counter>{(num: number) => <>Current Count: {num}</>}</Counter>
      </CounterProvider>
    </>
  )
}

export default App
