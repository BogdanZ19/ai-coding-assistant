# AI Coding Agent (Guided project from [boot.dev](https://www.boot.dev/))

This project implements a helpful AI coding agent powered by the Google Gemini API. The agent can explore a codebase, read and write files, and execute Python scripts within a restricted directory to assist with development tasks.

---

## ⚠️ Security & Usage Warning

This project is a **toy / proof-of-concept agent** built for learning and experimentation. It is **not production-ready**, and its tool-calling capabilities are **not securely sandboxed**.<br><br>
Do **NOT** grant this agent access to sensitive data, real credentials, production systems, or critical infrastructure. The agent may execute arbitrary code or modify files in unintended ways, and its safeguards are limited.<br><br>
Do **NOT** deploy or use this agent “as-is” in real-world environments.<br><br>

 
 

---

## Project Structure

The project is organized into a core logic layer and a set of tool functions that the agent can invoke:

* **`main.py`**: The entry point for the application. It handles CLI arguments, initializes the Gemini client, and manages the conversation loop.
* **`get_response.py`**: Configures the model (Gemini 2.5 Flash) and attaches the available tool schemas.
* **`functions/`**: Contains the logic for the agent's tools:
* `get_files_info.py`: Lists files and directories.
* `get_file_content.py`: Reads the content of a specific file (up to 10k characters).
* `run_python_file.py`: Executes a Python script and returns STDOUT/STDERR.
* `write_file.py`: Overwrites or creates files with new content.


* **`schema.py`**: Defines the JSON schema for each function so the LLM understands how to call them.
* **`config.py`**: Holds global constants like the `SYSTEM_PROMPT` and `MAX_CHARS` limits.

---

## Getting Started

### Prerequisites

* Python 3.10+
* A Google Gemini API Key.
* [uv](https://github.com/astral-sh/uv) installed (recommended for dependency management).

### Installation

1. **Clone the repository** and navigate to the project root.
2. **Set up your environment variables**:
Create a `.env` file in the root directory:
```bash
GEMINI_API_KEY=your_api_key_here

```


3. **Sync dependencies**:
I recommend using `uv` for a fast, reproducible environment setup:
```bash
uv sync

```



### Usage

Run the agent by providing a prompt as a command-line argument. You can use the `--verbose` flag to see token usage and specific function calls.

```bash
# Example: Ask the agent to run tests for the calculator
uv run main.py "Run the tests in tests.py and tell me if they pass." --verbose

# Example: Ask the agent to modify code
uv run main.py "Add a power operator (**) to the calculator logic."

```

---

## Available Tools

The agent has access to the following functions, all of which are restricted to the `./calculator` working directory for safety:

| Function | Description |
| --- | --- |
| `get_files_info` | Lists files and directories with sizes. |
| `get_file_content` | Reads the first 10,000 characters of a file. |
| `run_python_file` | Executes a `.py` file with optional arguments. |
| `write_file` | Writes or overwrites a file with provided text. |
