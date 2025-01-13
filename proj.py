"""
Project script for the word cloud project where it takes user input and generates a word cloud.
"""
import string
from string import punctuation
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from wordcloud import WordCloud

# Download the necessary NLTK resources
import nltk
nltk.download('punkt_tab', quiet=True) 
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

# Test corpus text
tText = "This is a test text for the word cloud project. This text will be used to test the word cloud generator. This text is a test text."


def takeText():
    """
    This function simply takes the text input from the user and returns it.
    """
    print("Enter the text you want to generate a word cloud for: ")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    text = " ".join(lines)
    return text

def tokenize(text):
    """
    This function takes the text input and tokenizes it.
    """
    tokens = nltk.word_tokenize(text)
    return tokens

def cleanText(text, lng="en"):
    """
    This function takes the text input and cleans it. Language is set to English by default. 
    """
    if lng == "en":
        stop_words = set(stopwords.words("english"))
    elif lng =="fr":
        stop_words = set(stopwords.words("french"))
    else:
        print("Language is not yet supported. Please pick either 'en' for English or 'fr' for French.")
        return None
    
    # call the tokenize function
    tokens = tokenize(text)
    # lowercase the text
    tokens = [word.lower() for word in tokens]
    # remove punctuation
    tokens = [re.sub(r'[^\w\s]', '', word) for word in tokens]
    # remove stop words
    tokens = [word for word in tokens if word not in stop_words]
    # remove tokens less than 1 character
    tokens = [word for word in tokens if len(word) > 1]
    return tokens

def stemText(tokens, lng="en"):
    """
    This function takes the tokens and stems them. User set the language.
    """
    if lng == "en":
        stemmer = nltk.SnowballStemmer("english")
    elif lng == "fr":
        stemmer = nltk.SnowballStemmer("french")
    else:
        print("Language is not yet supported. Please pick either 'en' for English or 'fr' for French.")
        return None
    # stem the tokens
    tokens = [stemmer.stem(word) for word in tokens]
    return tokens

def lemText(tokens, lng="en"):
    """
    This function takes the tokens and lemmatizes them. User set the language.
    """
    if lng == "en":
        lemmatizer = nltk.WordNetLemmatizer()
    elif lng == "fr":
        lemmatizer = nltk.WordNetLemmatizer()
    else:
        print("Language is not yet supported. Please pick either 'en' for English or 'fr' for French.")
        return None
    # lemmatize the tokens
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

def transformText(text, lng="en"):
    """
    This function applies all the text transformation functions to the tokens.
    """
    text = cleanText(text, lng)
    text = stemText(text, lng)
    text = lemText(text, lng)
    return text

def showStats(text, lng="en", nout=10):
    """
    This function shows the statistics of the text in a pd dataframe.
    """
    # Transform the text
    text = transformText(text, lng)
    # Get the number of words
    num_words = len(text)
    # Get the number of unique words
    num_unique_words = len(set(text))
    # Number of times each word appears
    word_freq = nltk.FreqDist(text)
    # Most common words
    most_common_words = word_freq.most_common(nout)
    # Show the stats in a dataframe
    df = pd.DataFrame(most_common_words, columns=["Word", "Frequency"])
    print(f"Number of words: {num_words}")
    print(f"Number of unique words: {num_unique_words}")
    print(df)

def genWordCloud(text, lng="en"):
    """
    Function to generate the word cloud.
    """
    # set figure dpi
    mpl.rcParams['figure.dpi'] = 100

    # Transform the text and create word chain
    text = transformText(text, lng)
    text = " ".join(text)

    # Generate the word cloud
    wordcloud = WordCloud(background_color="white",max_words=5000,contour_width=3)
    wordcloud.generate(text)
    wordcloud.to_image()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def main():
    """
    Main function that runs the project.
    """
    # Take the text input
    text = takeText()
    # Show the statistics
    showStats(text)
    # Generate the word cloud
    genWordCloud(text)

if __name__ == "__main__":
    main()

