# GitHub Agent Demo

A lightweight demonstration project illustrating an automated GitHub AI agent capable of simulating code reviews, repository health checks, and changelog generation.

## Features

- **PR Review Simulation**: Analyzes pull request diffs for debug statements, pending TODOs, and empty diffs.
- **Repository Health Check**: Checks for critical repository files (README, .gitignore, LICENSE) and computes a health score.
- **Automated Release Notes**: Categorizes commit messages (`feat`, `fix`, etc.) into formatted markdown release notes.
- **Zero External Dependencies**: Built entirely using Python's standard library.

## Project Structure

```text
.
├── .gitignore          # Python git ignore rules
├── README.md           # Project documentation
├── main.py             # CLI runner for demonstration
├── src/
│   ├── __init__.py
│   └── agent.py        # Core GitHubAgent implementation
└── tests/
    └── test_agent.py   # Unit tests
```

## Getting Started

### Prerequisites

- Python 3.8+ (no `pip install` required)

### Running the Demo

Execute the agent demo to see all workflows:

```bash
python main.py
```

Run a specific action:

```bash
# Health check only
python main.py --action health

# PR Review only
python main.py --action review

# Release notes only
python main.py --action release
```

### Running Tests

Run the test suite using Python's built-in test runner:

```bash
python -m unittest discover -s tests
```