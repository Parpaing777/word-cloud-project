from flask import Flask, render_template, request, jsonify
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import base64
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import matplotlib as mpl
mpl.use('Agg')
from flask_cors import CORS

app = Flask(__name__, static_folder="static", template_folder="templates") 
CORS(app)

nltk.download('punkt_tab', quiet=True) 
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

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
    
    tokens = word_tokenize(text)
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def genWordCloud():
    try:
        text = request.form.get('text','')
        lng = request.form.get('lng')

        if not text:
            return jsonify({'error': 'Please provide some text.'}), 400
        
        # Transform the text and create word chain
        text = transformText(text, lng)
        text = " ".join(text)
        # Generate the word cloud
        try:
            wordCloud = WordCloud(width=800, height=400, background_color="white", max_words=5000, contour_width=3)
            wordCloud.generate(text)
            print("WordCloud generated successfully")
        except Exception as e:
            print(f"WordCloud generation error: {str(e)}")
            return jsonify({'error': f'WordCloud generation failed: {str(e)}'}), 500

        try:
            img = io.BytesIO() 
            plt.figure(figsize=(8,4))
            plt.imshow(wordCloud, interpolation='bilinear')
            plt.axis("off")
            plt.savefig(img, format='png')
            plt.close()
            img.seek(0)
            img_base64 = base64.b64encode(img.getvalue()).decode()
            print("Image processing completed successfully")
            
            return jsonify({'image': f"data:image/png;base64,{img_base64}"})
        except Exception as e:
            print(f"Image processing error: {str(e)}")
            return jsonify({'error': f'Image processing failed: {str(e)}'}), 500

    except Exception as e:
        print(f"General error in generate: {str(e)}")
        return jsonify({'error': f'Failed to generate cloud: {str(e)}'}), 500

@app.route('/stats', methods=['POST'])
def stats():
    try:
        text = request.form.get('text')
        print(f"Received text for stats: {len(text) if text else 'None'}")
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
            
        lng = request.form.get('lng', 'en')
        print(f"Language for stats: {lng}")
        
        try:
            text = transformText(text, lng)
            print("Text transformation successful")
        except Exception as e:
            print(f"Text transformation error: {str(e)}")
            return jsonify({'error': f'Text transformation failed: {str(e)}'}), 500
            
        num_words = len(text)
        num_unique_words = len(set(text))
        word_freq = nltk.FreqDist(text)
        most_common_words = word_freq.most_common(10)
        stats = [{'word': word, 'frequency': freq} for word, freq in most_common_words]
        print("Stats generated successfully")
        
        return jsonify({
            'num_words': num_words, 
            'num_unique_words': num_unique_words, 
            'stats': stats
        })
    except Exception as e:
        print(f"General error in stats: {str(e)}")
        return jsonify({'error': f'Stats generation failed: {str(e)}'}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)