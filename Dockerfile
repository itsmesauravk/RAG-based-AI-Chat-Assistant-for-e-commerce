FROM python:3.11.9-slim-bullseye

WORKDIR /app

# Copy only requirements first to leverage Docker cache on dependencies
COPY requirements.txt .

# Install dependencies without cache for smaller image
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose port
EXPOSE 8000

# Start the FastAPI app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
