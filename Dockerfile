FROM python:3.10-slim

WORKDIR /app

# Install system dependencies required for matplotlib and wordcloud
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# More comprehensive NLTK data download
RUN python -c "import nltk; \
    nltk.download('punkt', download_dir='/usr/local/share/nltk_data'); \
    nltk.download('stopwords', download_dir='/usr/local/share/nltk_data'); \
    nltk.download('wordnet', download_dir='/usr/local/share/nltk_data'); \
    nltk.download('omw-1.4', download_dir='/usr/local/share/nltk_data')"

# Set NLTK_DATA environment variable
ENV NLTK_DATA=/usr/local/share/nltk_data
# Set path for stopwords


COPY . .

EXPOSE 5000

CMD ["python", "app.py"]