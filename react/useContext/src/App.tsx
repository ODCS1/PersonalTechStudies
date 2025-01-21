import ThemeToggleButton from "./componentes/ThemeToggleButton";
import { useTheme } from "./context/ThemeContext";

function App() {
  const { isDarkMode } = useTheme();

  return (
    <div 
      style={{
        background: isDarkMode ? "#333" : "#fff",
        color: isDarkMode ? "#fff" : "#000",
        height: "100vh",
        padding: "20px"
      }}
    >
      <header style={{textAlign: "center"}}>
        <h1>USE CONTEXT</h1>
      </header>
      <section>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit, accusamus facilis laboriosam, architecto deserunt vero veritatis dolorum aperiam asperiores quos labore quae non iusto laborum eum facere qui rerum aspernatur.
      </section>
      <ThemeToggleButton />
    </div>
  );
}

export default App;
