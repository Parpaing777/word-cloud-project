from flask import Flask, render_template, request, jsonify
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import base64
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import re
import matplotlib as mpl
mpl.use('Agg')
from flask_cors import CORS

app = Flask(__name__, static_folder="static", template_folder="templates") 
CORS(app)

def check_nltk():
    """ helper function to check nltk downloads"""
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
        nltk.data.find('corpora/wordnet')
        nltk.data.find('corpora/omw')
    except LookupError:
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('wordnet', quiet=True)
        nltk.download('omw', quiet=True)

def tokenize(text):
    """
    This function takes the text input and tokenizes it.
    """
    tokens = word_tokenize(text)
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

check_nltk()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/stats', methods=['POST'])
def stats():
    try:
        text = request.form['text']
        lng = request.form['lng']
        text = transformText(text, lng)
        num_words = len(text)
        num_unique_words = len(set(text))
        word_freq = nltk.FreqDist(text)
        most_common_words = word_freq.most_common(10)
        stats = [{'word': word, 'frequency': freq} for word, freq in most_common_words]
        return jsonify({'num_words': num_words, 'num_unique_words': num_unique_words, 'stats': stats})
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/generate', methods=['POST'])
def genWordCloud():
    try:
        text = request.form.get('text','')
        lng = request.form.get('lng')
        if not text:
            return jsonify({'error': 'Please provide some text.'}),400
        
        # set figure dpi
        mpl.rcParams['figure.dpi'] = 100
        # Transform the text and create word chain
        text = transformText(text, lng)
        text = " ".join(text)
        # Generate the word cloud
        wordCloud = WordCloud(width=800, height=400, background_color="white",max_words=5000,contour_width=3)
        wordCloud.generate(text)

        img = io.BytesIO() 
        plt.figure(figsize=(8,4))
        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        img_base64 = base64.b64encode(img.getvalue()).decode()

        return jsonify({'image': f"data:image/png;base64,{img_base64}"})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500
    
