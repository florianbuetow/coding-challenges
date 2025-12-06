# Use a minimal base image with Python 3.11
FROM python:3.11-slim

# Install git for generate_changes.py
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the generator scripts (not entire project)
COPY generate_readme.py .
COPY generate_changes.py .

# The folder where the generated README.md will be persisted
VOLUME ["/app/output"]

# Run the generator script to generate the README.md file
CMD ["bash", "-c", "python generate_readme.py"]

# Automatically exit the container after execution
