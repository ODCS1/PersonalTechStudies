// import Message  from "./Message";
import ListGroup from "./components/ListGroup";
import Counter from "./components/Counter";

function App() {
  // let cities = ["São Paulo", "Tokyo", "Paris", "Roma"];
  let colors = ["Black", "Blue", "Grey", "Cyan"];

  const handleSelectItem = (item: string) => {
    console.log(item);
  }



  return (
    <>
      <div>
        <ListGroup items={colors} heading="Colors" onSelectItem={handleSelectItem}/>
      </div>

      <div>
        <Counter />
      </div>
    </>
  );
}


export default App;