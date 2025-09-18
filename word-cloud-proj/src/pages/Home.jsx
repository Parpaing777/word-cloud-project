import { ThemeToggle } from "@/components/ThemeToggle";
import { HeroSection } from "../components/HeroSection";

export const Home = () => { 
    return (
        <div className="min-h-screen bg-background text-foreground overflow-x-hidden">
            {/* Theme Toggle */}
            <ThemeToggle />
            {/* Title */}
            <div>
                <h1 className="text-4xl md:text-6xl font-bold tracking-tight">
                    <span className="opacity-0 animate-fade-in">
                        Word Cloud
                    </span> {""}
                    <span className="text-green-400 opacity-0 animate-fade-in-delay-1">
                        Generator
                    </span>
                </h1>
            </div>
            
            {/* Main body */}
            <main>
                <HeroSection />
            </main>
            {/* Footer */}
        </div>
    )
}