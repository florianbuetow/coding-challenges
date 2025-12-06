.PHONY: help init generate destroy status

IMAGE_NAME := readme-generator

# Function to check if Docker image exists
# Returns 0 if exists, 1 if not
define check_image_exists
	docker image inspect $(IMAGE_NAME) >/dev/null 2>&1
endef

# Default target - show help
help:
	@echo ""
	@echo "Available targets:"
	@echo "  make init       - Build Docker image (run this first)"
	@echo "  make generate   - Generate README.md"
	@echo "  make status     - Check if Docker image exists"
	@echo "  make destroy    - Delete Docker image"
	@echo "  make help       - Show this help message"
	@echo ""

# Generate README using existing image (depends on init)
generate: init
	@echo ""
	@echo "Removing existing README.md file..."
	@rm -f README.md
	@echo "Running Docker container to generate README.md..."
	@docker run --rm \
		-v "$$(pwd)/leetcode":/app/leetcode:ro \
		-v "$$(pwd)/deep-ml":/app/deep-ml:ro \
		-v "$$(pwd)/aoc":/app/aoc:ro \
		-v "$$(pwd)/DESCRIPTION.md":/app/DESCRIPTION.md:ro \
		-v "$$(pwd)/USAGE.md":/app/USAGE.md:ro \
		-v "$$(pwd)":/app/output \
		$(IMAGE_NAME)
	@echo "README.md generated successfully."
	@echo ""

init:
	@if ! $(check_image_exists); then \
		docker build --no-cache -t $(IMAGE_NAME) .; \
		echo ""; \
		echo "Image built successfully."; \
		echo ""; \
	fi

# Remove docker image
destroy:
	@echo ""
	@echo "Removing $(IMAGE_NAME) image..."
	@docker rmi -f $(IMAGE_NAME):latest
	@echo "Cleanup complete."
	@echo ""

# Check if Docker image exists
status:
	@echo ""
	@if $(check_image_exists); then \
		echo "Docker container exists."; \
		echo "You can run 'make generate' to generate the README.md"; \
	else \
		echo "Docker container does not exist."; \
		echo "Run 'make init' to create it."; \
	fi
	@echo ""
