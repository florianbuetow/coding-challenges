# Default recipe shows available commands
default:
    @just --list

# Build Docker image if it doesn't exist
init:
    #!/usr/bin/env bash
    if ! docker image inspect readme-generator >/dev/null 2>&1; then
        docker build --no-cache -t readme-generator .
        echo ""
        echo "Image built successfully."
        echo ""
    fi

# Generate README.md using Docker
generate: init
    @rm -f README.md
    @echo ""
    @echo "Running Docker container to generate README.md..."
    @docker run --rm \
        -v "$(pwd)":/app \
        -w /app \
        readme-generator
    @echo "README.md generated successfully."
    @echo ""

# Remove Docker image
destroy:
    @echo ""
    @echo "Removing readme-generator image..."
    @docker rmi -f readme-generator:latest
    @echo "Cleanup complete."
    @echo ""

# Check if Docker image exists
status:
    @echo ""
    @if docker image inspect readme-generator >/dev/null 2>&1; then \
        echo "Docker container exists."; \
        echo "You can run 'just generate' to generate the README.md"; \
    else \
        echo "Docker container does not exist."; \
        echo "Run 'just init' to create it."; \
    fi
    @echo ""
