
## Generating the README

The following outlines the steps to generate the `README.md` file using the automated system.

### Prerequisites

- Clone this repository
- Ensure that [uv](https://docs.astral.sh/uv/) is installed on your system

### Using Just

#### 1. Generate README

```bash
just generate
```

This runs the generator script to produce the `README.md` and `CHANGES.md` files.

#### 2. Cleanup

```bash
just destroy
```

This removes the virtual environment.
