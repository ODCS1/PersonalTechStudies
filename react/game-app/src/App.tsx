// import Message  from "./Message";
import ListGroup from "./components/ListGroup";
import Counter from "./components/Counter";
import Alert from "./components/Alert";

function App() {
  // let cities = ["São Paulo", "Tokyo", "Paris", "Roma"];
  let colors = ["Black", "Blue", "Grey", "Cyan"];

  const handleSelectItem = (item: string) => {
    console.log(item);
  }

  let textValue: string = "Alert Element"


  return (
    <>
      <div>
        <ListGroup items={colors} heading="Colors" onSelectItem={handleSelectItem}/>
      </div>

      <div>
        <Counter />
      </div>

      <>
        <Alert>
          <p><b>{textValue}</b></p>
        </Alert>
      </>
    </>
  );
}


export default App;