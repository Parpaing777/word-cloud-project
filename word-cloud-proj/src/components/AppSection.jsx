import { useState } from "react";


export const AppSection = () => {
    const [text, setText] = useState("");
    const [language, setLanguage] = useState("en");
    const [wordCloud, setWordCloud] = useState(null);
    const [wordStats, setWordStats] = useState(null);

    const handleClearText = () => { 
        setText("");
        setWordCloud(null);
        setWordStats(null);
    }

    const handleGenerateWC = async () => {
        try {
            const response = await fetch("/generate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text, lng: language }),
            });
            const data = await response.json();
            if (data.image) {
                setWordCloud(data.image);
            }
        } catch (error) {
            console.error("Error generating word cloud:", error);
        }
    }

    const handleStats = async () => {
        try {
            const response = await fetch("/stats", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text, lng: language }),
            });
            const data = await response.json();
            if (data.stats) {
                setWordStats(data);
            }
        } catch (error) {
            console.error("Error fetching word stats:", error);
        }
    };




    return (
        <>
        <div className="pt-4 opacity-0 animate-fade-in-delay-2">
            <div className="flex gap-2 items-start">
                <textarea
                className="flex-1 p-3 border rounded-lg text-sm md:text-base"
                placeholder="Enter your text here..."
                rows={10}
                value={text}
                onChange={(e) => setText(e.target.value)}
                />
                
            <div className="flex flex-col gap-2">
                <button
                className="cosmic-button" onClick={handleClearText}>
                Clear Text
                </button>
                        
                <select 
                    id="lng"
                    value={language}
                    onChange={(e) => setLanguage(e.target.value)}
                    className="px-2 py-2 opacity-0 animate-fade-in-delay-2 border rounded-lg text-sm md:text-base bg-background text-foreground min-w-fit"
                >
                    <option value="en">English</option>
                    <option value="fr">French</option>
                </select>
                        
            </div>
            </div>
        </div>        

        <div className="mt-4 opacity-0 animate-fade-in-delay-3 flex justify-center gap-4">
            <button className="cosmic-button" onClick={handleGenerateWC}>
                    Generate Word Cloud
                </button>
                <button
                    className="px-6 py-2 rounded-full border border-primary text-primary hover:bg-primary/10 transition-colors duration-300 hover:scale-105 active:scale-95"
                    onClick={handleStats}>
                    Show Word Statistics
                </button>
        </div>
        
        {wordCloud && (
            <div className="mt-4 flex justify-center opacity-0 animate-fade-in-delay-4">
                <img 
                    src={wordCloud} 
                    alt="Word Cloud"
                    className="rounded-lg shadow-md" />
            </div>
        )}
        
        {wordStats && (
            <div className="mt-4 p-4 border rounded-lg ">
                <p>Total Words: {wordStats.num_words}</p>
                <p>Unique Words: {wordStats.num_unique_words}</p>
                <ul className="list-disc ml-6">
                    {wordStats.stats.map((s, i)=> (
                        <li key={i}>
                            {s.word} : {s.frequency}
                        </li>
                    ))}
                </ul>
            </div>
        )}
        </>
        
    )
}