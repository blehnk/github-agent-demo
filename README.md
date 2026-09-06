# GitHub Agent Demo

## Purpose

This repository provides a lightweight demonstration of an automated GitHub AI agent. The agent showcases capabilities such as:

- Simulating pull‑request reviews (detecting debug statements, TODOs, and empty diffs).
- Performing repository health checks.
- Generating release notes from conventional commit messages.

The implementation uses only Python's standard library, making it easy to explore and extend.

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/github-agent-demo.git
   cd github-agent-demo
   ```

2. **Python version**
   Ensure you have Python 3.8 or newer installed:
   ```bash
   python --version
   # Expected output: Python 3.8+ 
   ```

   No additional dependencies are required; the project relies solely on the standard library.

---

## Usage

The project includes a small CLI entry point (`main.py`). You can run the full demo or individual actions.

### Run the full demo
```bash
python main.py
```
This will execute the health check, PR review simulation, and release‑notes generation sequentially.

### Run a specific action
```bash
# Repository health check only
python main.py --action health

# Pull‑request review simulation only
python main.py --action review

# Release notes generation only
python main.py --action release
```

### Running the test suite
```bash
python -m unittest discover -s tests
```
All tests should pass, confirming the core functionality works as expected.

---

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. **Fork the repository** on GitHub.
2. **Create a new branch** for your feature or bug fix:
   ```bash
   git checkout -b my-feature-branch
   ```
3. **Make your changes**, ensuring existing tests continue to pass. Add new tests for new functionality.
4. **Commit your changes** with clear, conventional commit messages (e.g., `feat: add new review rule`).
5. **Push to your fork** and open a Pull Request against the `main` branch.
6. **Review** – maintainers will review your PR, provide feedback, and merge once approved.

### Code style
- Follow PEP 8 guidelines.
- Use descriptive variable and function names.
- Keep functions small and focused.

### Testing
- Add unit tests under the `tests/` directory.
- Run the test suite locally before submitting a PR.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or suggestions, feel free to open an issue or contact the maintainer.