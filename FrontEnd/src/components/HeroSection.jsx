import { useState } from "react"
import { AppSection } from "./AppSection";


export const HeroSection = () => {
    const [isStarted, setIsStarted] = useState(false);
    
    const handleStart = () => {
        // Hide the description and show the input text box
        setIsStarted(true);
        
    }


    return (
        <section className="relative px-2 py-8">
            <div className="container max-w-4xl mx-auto text-center z-10">
                <div className="space-y-6">

                    {!isStarted ? (
                        // Show the description and start button
                        <>
                            <div className="text-lg md:text-xl text-muted-foreground items-center max-w-4xl mx-auto opacity-0 animate-fade-in-delay-2 space-y-4">
                                <p className="text-muted-foreground text-justify mb-1">
                                    This web app is aimed to generate word cloud from user input text.
                                </p>
                                <p className="text-muted-foreground text-justify mb-1">
                                    The goal of this app is to use the job description texts to generate a word cloud so that you can easily identify the key skills and requirements for the job.
                                </p>
                                <p className="text-muted-foreground text-justify mb-1">
                                    This app serves as a tool to help job seekers quickly grasp the main points of a job description and tailor their resumes and cover letters accordingly.
                                </p>
                                <p className="text-muted-foreground text-justify mb-4">
                                    It can also show the statistics of the words in the text input.
                                </p>
                            </div>
                            
                            <div className="pt-2 px-4 opacity-0 animate-fade-in-delay-4">
                                <button
                                    className="cosmic-button"
                                    onClick={handleStart}
                                >
                                    Start
                                </button>
                            </div>
                        </>
                    ) : (
                        // Swap the AppSection component
                            <AppSection />
                    )}

                </div>
            </div>
        </section>
    )
}