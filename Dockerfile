FROM python:3.9-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /servicio_social

# Copy code
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Disable ONEDNN if needed
ENV TF_ENABLE_ONEDNN_OPTS=0

# Default run command
CMD ["python3", "app.py"]
