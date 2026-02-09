# PMT (python module template)

<img src="/docs/assets/mascot-portrait.png" alt="PMT Mascot" width="200" align="right"/>

template repository for developing python modules - zero to full dev environment

features:

- uv managed virtual environments and dependencies
- invoke module with custom commands
- Github actions CI workflow
- pre-commit checks for linting

## Using this template

- [Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
- [Customizing the template](/docs/customization.md)

## Running PMT

You can run the `pmt` command using uv with these options:

### Option 1: Using uv run with script entry point (Recommended)

```bash
uv venv
uv pip install -e .
uv run pmt
```

### Option 2: Using uv run with module

```bash
# uv automatically creates `.venv`
uv run python -m main
```

### Option 3: Using uv run with file

```bash
# uv automatically creates `.venv`
uv run python main.py
```

The first option (`uv run pmt`) is the cleanest approach as it uses the script entry point defined in `pyproject.toml`.

## Running tests

```bash
uv run pytest
```

## Why Use uv with Virtual Environments?

Using uv with virtual environments provides several important benefits:

- **Isolation**: Virtual environments create isolated Python environments, preventing conflicts between project dependencies and system-wide packages
- **Reproducibility**: The `.venv` directory and `uv.lock` file ensure consistent environments across different machines and development setups
- **Dependency Management**: uv automatically manages dependencies and creates optimized virtual environments with fast package installation
- **Clean Development**: Each project gets its own isolated environment, making it easy to test and develop without affecting other projects
