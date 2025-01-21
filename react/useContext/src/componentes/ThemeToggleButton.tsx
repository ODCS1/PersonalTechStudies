import { useTheme } from "../context/ThemeContext";

const ThemeToggleButton = () => {
  const { isDarkMode, toggleTheme } = useTheme();

  return (
    <button onClick={toggleTheme}
      style={{
        borderRadius: "4px",
        padding: "5px",
        background: isDarkMode ? "#344CB7" : "#000957",
        color: isDarkMode ? "#000" : "#fff",
        cursor: "pointer"
      }}
    >
      { isDarkMode ? "Light Mode" : "Dark Mode" }
    </button>
  )
};

export default ThemeToggleButton;
