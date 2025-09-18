# Word-cloud-project
This is the Version 2.0 of the Word Cloud project.
In this version, the front end is developped using the React + Vite framework with tailwind CSS for a modern look. 

## Main Idea
The goal of this web app is to generate a word cloud and/or see the statistics from a user input text paragraphs.  

**Example Usecase**  
Let's say we are trying to tailor our CV or write a Cover Letter to apply to a job offer you have found on the internet.  
Sure you can just make and submit a generic CV and Cover Letter but what if you want to tailor your CV, Cover Letter to grab the attention of the hiring manager or anyone who sees ur profile?  

That's where the webapp comes in. You can simply copy and paste the Job Description that you have found and generate a word cloud of it or see the top 10 words of the JD(Job Description).  
The word cloud shows the words that are repeating in the JD with bigger size, i.e the bigger the word size, the more repeting it is in the JD.  

This was a fun little project to help people in their job search.  
This is a proof of concept and a prototype. The way that the app stem and lemmatize words are not perfect. It sometimes leaves the word cut up.As an example, the word 'generator' from the JD will be transformed into 'generat'.  

# How to run the web app?
Currently, the application is not hosted on a server. 
But if you want to test, you can create a container using the Dockerfile provided in the project
To build the docker image, containerize and run on your own machine or host it on your own server, follow the instructions below: 


1. Make sure u have all the requirements installed and Docker CLI installed. 
2. The Dockerfile is already provided. Therefore to build the docker file, `docker build -t <name-you-want> .`  
3. To run the container locally for testing purposes, you can use, `docker run -p 8080:8080 <name-you-want>`  
 

Happy testing! ;) 