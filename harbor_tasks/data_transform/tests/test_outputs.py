"""
Pytest tests for verifying the JSON output of the data transform task.

This file is copied to /tests/test_outputs.py and executed by /tests/test.sh.
It ensures that the task generates the correct output file and contents.
"""

import json
from pathlib import Path


def test_output_exists():
    """Verify that /app/output.json is created by the task."""
    test_outputs_path = Path("/app/output.json")
    assert test_outputs_path.exists(), f"File {test_outputs_path} does not exist"


def test_exact_match():
    """Verify that the JSON output exactly matches the expected filtered people list."""
    output = Path("/app/output.json").read_text()
    data = json.loads(output)

    expected = [
        {
            "id": 1,
            "name": "Manas Agarwal",
            "age": 28,
            "email": "manas@example.com",
            "city": "Delhi",
        },
        {
            "id": 2,
            "name": "Riya Sharma",
            "age": 26,
            "email": "riya@example.com",
            "city": "Mumbai",
        },
    ]

    assert data == expected, f"Expected {expected}, but got {data}"
