# Harbor Assignment - Age Filter Task

A Python project that filters people data based on age criteria using the Harbor framework.

## Prerequisites

- Python 3.13+
- uv package manager

## Installation

```bash
# Clone the repository
git clone https://github.com/manasagar/harborAssignment.git
cd harborAssignment     

# Install dependencies
uv sync
```

## Project Structure

```
harbour_assignment/
├── input.txt           # Input data file (JSON array)
├── output.json         # Generated output (filtered results)
├── main.py             # Main application logic
├── tests/
│   └── test_outputs.py # Test suite
├── pyproject.toml      # Project configuration
└── README.md           # This file
```

## Input Format

The `input.txt` file should contain a JSON array of people:

```json
[
  {
    "id": 1,
    "name": "Manas Agarwal",
    "age": 28,
    "email": "manas@example.com",
    "city": "Delhi"
  },
  {
    "id": 2,
    "name": "Riya Sharma",
    "age": 26,
    "email": "riya@example.com",
    "city": "Mumbai"
  },
  {
    "id": 3,
    "name": "Arjun Patel",
    "age": 15,
    "email": "arjun@example.com",
    "city": "Ahmedabad"
  },
  {
    "id": 4,
    "name": "Neha Gupta",
    "age": 19,
    "email": "neha@example.com",
    "city": "Bengaluru"
  }
]
```

## Output Format

The `output.json` file contains filtered results (age > 25):

```json
[
  {
    "id": 1,
    "name": "Manas Agarwal",
    "age": 28,
    "email": "manas@example.com",
    "city": "Delhi"
  },
  {
    "id": 2,
    "name": "Riya Sharma",
    "age": 26,
    "email": "riya@example.com",
    "city": "Mumbai"
  }
]
```

## Usage

### Run the validations

```bash
uv run harbor run --agent oracle --path harbor_tasks/data_transform --job-name test-oracle
uv run harbor run --agent nop --path harbor_tasks/data_transform --job-name test-nop
uvx ruff check harbor_tasks/data_transform 
```


uv run harbor run --agent nop --path harbor_tasks/data_transform --job-name test-nop
uv run harbor run --agent oracle --path harbor_tasks/data_transform --job-name test-oracle
uvx ruff check harbor_tasks/data_transform 
