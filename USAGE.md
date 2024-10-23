
## Generating the README

The following outlines the steps to build and run the Docker container that generates the `README.md` file using the `generate_readme.py` script.

#### 0. Prerequisites

- Clone this repository.
- Ensure that Docker is installed and running on your system.

#### 1. Make the Bash Script Executable

Run the following command to make the script executable:

```bash
chmod +x ./generate_readme_using_docker.sh
```

#### 2. Build and Run the Docker Container

```bash
./generate_readme_using_docker.sh
```

- This will build the Docker image every time it is run (to avoid caching)
- It will then run the Docker container to execute the `generate_readme.py` script, which generates the `README.md` file and persists it to your local directory.

#### 3. Verify the Output

Once the container execution is finished, you should see the updated `README.md` file in the same directory where you ran the script.
