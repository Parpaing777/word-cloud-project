import { useEffect, useState } from "react";
import { cn } from "../lib/utils";
import { Sun, Moon } from "lucide-react";



export const ThemeToggle = () => {

    const [isDarkMode, setIsDarkMode] = useState(false);

    useEffect(() => {
        const storedTheme = localStorage.getItem('theme');
        if (storedTheme === 'dark') {
            setIsDarkMode(true);
            document.documentElement.classList.add('dark');
        } else {
            localStorage.setItem('theme', 'light');
            setIsDarkMode(false);
            
        }
    }, [])

    const toggleTheme = () => {
        if (isDarkMode) {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('theme', 'light');
            setIsDarkMode(false);
        } else {
            document.documentElement.classList.add('dark');
            localStorage.setItem('theme', 'dark');
            setIsDarkMode(true);
        }
    }

    return (
        <button
            onClick={toggleTheme}
            className={cn(
                "fixed top-2 right-2 z-50 p-2 rounded-full transition-colors duration-300",
                "focus:outline-hidden"
            )}
        >
            {
                isDarkMode
                    ? (
                        <Sun className="h-6 w-6 text-yellow-300 hover:scale-125 transition-transform duration-200" />
                    ) : (
                        <Moon className="h-6 w-6 text-gray-800 hover:scale-125 transition-transform duration-200" />
                    )
            }

        </button>
    )

}