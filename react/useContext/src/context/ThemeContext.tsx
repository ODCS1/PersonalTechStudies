import React, { createContext, ReactNode, useContext, useState } from "react";



interface ThemeContextType {
    isDarkMode: boolean;
    toggleTheme: () => void;
}

interface ThemeProviderProps {
    children: ReactNode;
}


// CREATE CONTEXT
const ThemeContext = createContext<ThemeContextType | null>(null);



// PROVIDER
export const ThemeProvider: React.FC<ThemeProviderProps> = ({ children }) => {
    const [isDarkMode, setIsDarkMode] = useState<boolean>(false);

    const toggleTheme = () => setIsDarkMode((prev) => !prev);

    return (
        <ThemeContext.Provider value={{ isDarkMode, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}

// CUSTOMIZED HOOK
export const useTheme = ():ThemeContextType => {
    const context = useContext(ThemeContext);
    if (!context) {
        throw new Error("useTheme needs to be inside of a ThemeProvider")
    }

    return context;
}