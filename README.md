# Word-cloud-project
This is a small personal project. 
This project is the creation of a web app and deployment/hosting to google cloud using Docker. 

## Main Idea
The goal of this web app is to generate a word cloud and/or see the statistics of a paragraph of texts. 

**Example Usecase**  
Let's say we are trying to make our CV or write a Cover Letter to apply to a job offer you have found on the internet.  
Sure you can just make and submit a generic CV and Cover Letter but what if you want to tailor your CV, Cover Letter to grab the attention of the hiring manager or anyone who sees ur profile?  

That's where the webapp comes in. You can simply copy and paste the Job Description that you have found and generate a word cloud of it or see the top 10 words of the JD(Job Description).  
The word cloud shows the words that are repeating in the JD with bigger size, i.e the bigger the word size, the more repeting it is in the JD.  

This was a fun little project to help people elevate their work.  
This is a proof of concept and it is not "perfect". The way that the app stem and lemmatize words are not perfect. It sometimes leaves the word cut up.As an example, the word 'generator' from the JD will be transformed into 'generat' but you get the idea.  

# How to run the web app?
For now, I have deployed the app to google cloud.  
And you can check it out and use it on [this link](https://wcloudapp-872609966024.europe-west9.run.app).  
But I do not guarantee that it will be up for a long time.  
If the link is down, it means that i have stopped hosting it.  
In that case follow the instructions below to run it on your own machine. 

1. Download the code source of this project.  
2. Make sure you have python installed on your PC.  
3. Open a terminal in the directory of the project file.  
4. Type in command `pip install requirements.txt`. 
5. Type in command `python app.py` (Depending on your system, the command to run the app might be a bit different)
6. The app will run on your localhost with the port 8080. 

If you wish to build a docker image, containerize it and run, follow the below instructions.  
1. Make sure u have all the requirements installed and Docker CLI installed. 
2. The Dockerfile is already provided. Therefore to build the docker file, `docker build -t <name-you-want> .`  
3. To run the container locally for testing purposes, you can use, `docker run -p 8080:8080 <name-you-want>`  

To deploy the web app, i suggest you follow online guides or ask any kind of LLM for help with it since it is more complex and I don't wish to write a lengthy readme file. 

Happy testing! ;) 