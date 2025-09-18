# New Dockerfile 

# Stage 1: Build react app
FROM node:18 AS frontend-builder

WORKDIR /frontend

# Copy package.json and package-lock.json
COPY FrontEnd/package*.json ./
RUN npm install

# Copy the rest of the frontend source code
COPY FrontEnd/ ./

# Build the React app
RUN npm run build

# Stage 2: Set up the backend with Flask and serve the React app
FROM python:3.11-slim AS backend

WORKDIR /app

# Install system dependencies (if needed for nltk or other packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy backend requirements and install them
COPY Backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Setup nltk resources
ENV NLTK_DATA=/app/nltk_data
RUN python -m nltk.downloader -d /app/nltk_data punkt stopwords wordnet omw-1.4

# Copy backend source code
COPY Backend/ ./

# Copy the built React app from the previous stage
COPY --from=frontend-builder /frontend/dist ./static

# Expose the port the app runs on
EXPOSE 8080

#Run the Flask app
CMD [ "python", "app.py" ]
