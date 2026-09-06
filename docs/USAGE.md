# Usage Guide

This guide provides step‑by‑step instructions for using the **GitHub Agent Demo** project.

## 1. Installation

The project has **no external dependencies** – it only requires Python 3.8 or newer. Clone the repository and you are ready to go:

```bash
git clone https://github.com/your-org/github-agent-demo.git
cd github-agent-demo
```

## 2. Running the Demo

The entry point is the `main.py` script. It offers a small CLI that can execute the three core workflows:

- **Health Check** – validates the repository structure.
- **Pull‑Request Review** – runs a simulated automated review.
- **Release Notes Generation** – builds a markdown changelog from a list of commit messages.

### Run All Workflows

```bash
python main.py
```

### Run a Specific Workflow

```bash
# Only the health check
python main.py --action health

# Only the PR review simulation
python main.py --action review

# Only the release notes generation
python main.py --action release
```

## 3. Customising the Agent

You can change the agent’s displayed name and the underlying model (the model name is only for illustration) via the `--name` flag:

```bash
python main.py --name "MyAgent" --action all
```

## 4. Running the Test Suite

The repository ships with a small unit‑test suite located in the `tests/` directory. Run it with the standard library’s unittest runner:

```bash
python -m unittest discover -s tests
```

All tests should pass, confirming that the core logic works as expected.

---

For more details about the internal architecture, see the **Architecture Overview** document.
