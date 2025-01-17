FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Set NLTK_DATA environment variable
ENV NLTK_DATA=/app/nltk_data

RUN python -m nltk.downloader -d /app/nltk_data punkt stopwords wordnet omw-1.4

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]