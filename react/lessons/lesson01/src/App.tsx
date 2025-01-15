import Counter from "./components/Counter";
import Heading from "./components/Heading";
import List from "./components/List";
import Section from "./components/Section";

function App() {
  return (
    <>
      <Heading title={"Hello"} />
      <Section title="Different Title">This is my Section</Section>
      <Counter />
      <List
        items={["🧑‍💻 Coding", "🤖 Robot", "🍚 Rice"]}
        render={(item: string) => <span className="gold bold">{item}</span>}
      />
    </>
  );
}

export default App;
