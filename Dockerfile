# Use a minimal base image with Python 3.11
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# The folder where the generated README.md will be persisted
VOLUME ["/app/output"]

# Run the generator script to generate the README.md file
CMD ["bash", "-c", "rm README.md"]
CMD ["bash", "-c", "rm /app/output/README.md"]
CMD ["bash", "-c", "python generate_readme.py && cp README.md /app/output/"]

# Automatically exit the container after execution
