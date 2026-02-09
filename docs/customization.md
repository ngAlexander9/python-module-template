# Customization

This guide covers how to customize the Python Module Template (PMT) to fit your specific project needs.

## Change the command

The PMT template comes with a default CLI command named `pmt`. You can customize both the command name and its functionality to match your project's requirements.

### Changing the Command Name

To change the command name from `pmt` to something else (e.g., `myapp`), modify the script entry point in `pyproject.toml`:

```toml
[project.scripts]
myapp = "pmt.main:main"  # Changed from "pmt = "pmt.main:main""
```

After making this change, you can run your command using the new name:

```bash
uv run myapp
```

### Changing the Command Functionality

The command's behavior is defined in the `main()` function in `pmt/main.py`. Modify this function to implement your desired functionality:

```python
def main():
    print("Hello from my awesome application!")  # Custom message
    # Add your custom logic here
    # For example, argument parsing, file operations, API calls, etc.

if __name__ == "__main__":
    main()
```

### Adding Command-Line Arguments

For more sophisticated CLI functionality, you can add argument parsing using Python's built-in `argparse` module:

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description='My awesome application')
    parser.add_argument('--version', action='version', version='1.0.0')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    parser.add_argument('input_file', help='Input file to process')

    args = parser.parse_args()

    if args.verbose:
        print(f"Processing file: {args.input_file}")

    # Your processing logic here

if __name__ == "__main__":
    main()
```

## Use `uv` to add dependencies

`uv` is a fast Python package installer and resolver that makes dependency management simple and efficient. Use it to add regular (runtime) dependencies to your project.

### Adding a Basic Dependency

To add a dependency, use the `uv add` command followed by the package name:

```bash
uv add requests
```

This command will:

- Download and install the `requests` package
- Add it to the `dependencies` section in `pyproject.toml`
- Update the `uv.lock` file with the exact versions

### Specifying Version Constraints

You can specify exact versions or version ranges when adding dependencies:

```bash
# Exact version
uv add requests==2.31.0

# Minimum version
uv add requests>=2.30.0

# Version range
uv add requests>=2.30.0,<3.0.0

# Compatible release (recommended for most cases)
uv add requests~=2.31.0
```

### Adding Git Dependencies

You can also add dependencies directly from Git repositories:

```bash
# From GitHub
uv add git+https://github.com/psf/requests.git

# From a specific branch
uv add git+https://github.com/psf/requests.git@main

# From a specific tag or commit
uv add git+https://github.com/psf/requests.git@v2.31.0
```

### Installing Dependencies

After adding dependencies, install them in your virtual environment:

```bash
uv pip install -e .
```

Or if you're using the virtual environment directly:

```bash
uv sync
```

## Use `uv` to add dev dependencies

Development dependencies are packages used during development but not required for the application to run in production. These include testing frameworks, linters, formatters, and other development tools.

### Adding Development Dependencies

Use the `--dev` flag to add packages as development dependencies:

```bash
uv add --dev black  # Code formatter
uv add --dev ruff   # Linter
uv add --dev pytest # Testing framework
```

These packages will be added to the `[dependency-groups.dev]` section in `pyproject.toml`.

### Installing Development Dependencies

Install all development dependencies with:

```bash
uv add --group dev
```

Or install specific dev dependencies by name:

```bash
uv add --group dev black ruff pytest
```

### Common Development Dependencies

Here are some commonly used development dependencies and their purposes:

```bash
# Code formatting
uv add --dev black
uv add --dev isort

# Linting and static analysis
uv add --dev ruff
uv add --dev flake8
uv add --dev mypy

# Testing
uv add --dev pytest
uv add --dev pytest-cov
uv add --dev hypothesis

# Documentation
uv add --dev mkdocs
uv add --dev mkdocs-material

# Pre-commit hooks
uv add --dev pre-commit
```

### Managing Multiple Dependency Groups

You can create custom dependency groups for different purposes. For example, you might want separate groups for testing, documentation, and deployment:

```toml
[dependency-groups]
dev = [
    "black>=23.0.0",
    "ruff>=0.1.0",
    "pytest>=7.0.0",
]

test = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "hypothesis>=6.0.0",
]

docs = [
    "mkdocs>=1.4.0",
    "mkdocs-material>=9.0.0",
]

deploy = [
    "build>=0.10.0",
    "twine>=4.0.0",
]
```

Install a specific group with:

```bash
uv add --group test
uv add --group docs
uv add --group deploy
```

## Best Practices

### Dependency Management

1. **Pin exact versions in production**: Use exact versions (`==`) for production dependencies to ensure reproducible builds
2. **Use compatible releases for libraries**: Use `~=` for library dependencies to allow patch updates
3. **Regular updates**: Periodically update dependencies to get security fixes and new features
4. **Lock files**: Always commit the `uv.lock` file to ensure consistent environments across all developers and deployment environments

### Command Design

1. **Clear naming**: Choose command names that clearly indicate their purpose
2. **Consistent interface**: Follow standard CLI conventions for your command-line arguments
3. **Help documentation**: Always provide clear help text for your commands and arguments
4. **Error handling**: Implement proper error handling and user-friendly error messages

### Development Workflow

1. **Separate concerns**: Keep development dependencies separate from runtime dependencies
2. **Automated checks**: Use pre-commit hooks to run linting and formatting automatically
3. **Testing**: Always include testing dependencies and write comprehensive tests
4. **Documentation**: Keep your documentation up to date with any changes to the command interface or dependencies

## Troubleshooting

### Common Issues

**Dependency conflicts**: If you encounter dependency conflicts, try updating all dependencies or using more specific version constraints.

```bash
uv add --upgrade
```

**Missing dependencies**: If a dependency is missing, ensure you've run `uv sync` or `uv pip install -e .` after adding it.

**Command not found**: If your custom command isn't found, verify that:

- The script entry point is correctly defined in `pyproject.toml`
- You're running the command from the correct directory
- The virtual environment is activated (if not using `uv run`)

**Permission errors**: If you encounter permission errors, ensure you're working in a virtual environment and not trying to install packages system-wide.

### Getting Help

- Check the [uv documentation](https://docs.astral.sh/uv/) for detailed usage information
- Use `uv --help` for command-specific help
- Review the `uv.lock` file to understand exact dependency versions being used

This customization guide should help you adapt the Python Module Template to your specific project needs. Remember to test your changes thoroughly and update this documentation as your project evolves.
