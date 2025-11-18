
## Generating the README

The following outlines the steps to generate the `README.md` file using the automated system.

### Prerequisites

- Clone this repository
- Ensure that Docker is installed and running on your system

### Using Make (Recommended)

#### 1. Initialize the Docker Container

```bash
make init
```

This builds the Docker image with the README generator. You only need to run this once, or after modifying `generate_readme.py`.

#### 2. Generate README

```bash
make generate
```

This runs the Docker container to generate the `README.md` file and appends `USAGE.md` to it.

#### 3. Check Status

```bash
make status
```

This checks if the Docker image already exists.

#### 4. Cleanup

```bash
make destroy
```

This removes the Docker image.
