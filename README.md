# CSV JSON Data Analyzer

A Python learning project focused on reading, cleaning, analyzing and exporting structured data with CSV and JSON files.

This repository is part of my personal developer learning roadmap. The goal is to strengthen my foundations in file handling, structured data processing, data cleaning and report generation using only Python and the standard library.

This project is independent from any product or business project.

---

## Objectives

The main objectives of this repository are to:

- Understand the difference between Python dictionaries and JSON
- Read and write JSON files
- Convert JSON strings to Python objects
- Convert Python objects to JSON strings
- Read CSV files
- Use `csv.DictReader`
- Use `csv.DictWriter`
- Clean and convert raw data
- Handle file and data errors properly
- Export simple reports in JSON, CSV or text format

---

## Topics Covered

| Block | Topic | Status |
| --- | --- | --- |
| 15.1 | Difference between Python dict and JSON | Completed |
| 15.2 | Read JSON with `json.load()` | Completed |
| 15.3 | Write JSON with `json.dump()` | Completed |
| 15.4 | Convert JSON string with `json.loads()` | Completed |
| 15.5 | Convert Python dict/list with `json.dumps()` | Completed |
| 15.6 | Read simple CSV files | Completed |
| 15.7 | Read CSV with `csv.DictReader` | Completed |
| 15.8 | Write CSV with `csv.DictWriter` | Completed |
| 15.9 | Clean and convert CSV data | Completed |
| 15.10 | Handle file and data errors | To do |
| 15.11 | CSV/JSON consolidation | To do |
| 15.12 | Final CSV/JSON analyzer project | To do |

---

## Project Structure

```text
csv-json-data-analyzer/
├── data/
│   ├── input/
│   │   └── products.csv
│   └── output/
│       └── .gitkeep
├── exercises/
│   ├── block_15_1_dict_vs_json.py
│   ├── block_15_json_basics.py
│   └── block_15_csv_basics.py
├── README.md
├── README_FR.md
└── .gitignore
```

> Note: this repository is intentionally simple. Exercises are executed file by file. A central `main.py` is not required at this stage.

> Generated files inside `data/output/` are ignored by Git.

---

## How to Run

Each exercise can be executed independently from the project root.

Examples:

```bash
python exercises/block_15_1_dict_vs_json.py
python exercises/block_15_json_basics.py
python exercises/block_15_csv_basics.py
```

The CSV basics exercise reads data from:

```text
data/input/products.csv
```

and exports a cleaned CSV file to:

```text
data/output/clean_products.csv
```

Generated files inside `data/output/` are ignored by Git.

---

## Completed Exercises

### 15.1 — Dict Python vs JSON

This exercise introduces the difference between:

- Python dictionaries
- JSON strings
- Python boolean values: `True`, `False`
- JSON boolean values: `true`, `false`
- Python `None`
- JSON `null`

It also introduces:

```python
json.dumps()
json.loads()
```

---

### 15.2 to 15.5 — JSON Basics

This exercise practices the four main JSON conversion functions:

```python
json.dumps()  # Python -> JSON string
json.loads()  # JSON string -> Python
json.dump()   # Python -> JSON file
json.load()   # JSON file -> Python
```

It also practices:

- Writing JSON files
- Reading JSON files
- Using `encoding="utf-8"`
- Using `indent=4`
- Using `ensure_ascii=False`
- Preserving accents in JSON files

---

### 15.6 to 15.9 — CSV Basics

This exercise practices reading, cleaning, analyzing and exporting CSV data.

It covers:

- Reading CSV files with `csv.DictReader`
- Writing CSV files with `csv.DictWriter`
- Using `newline=""`
- Cleaning text fields with `.strip()`
- Normalizing text with `.lower()`
- Converting values with `int()` and `float()`
- Counting products by category
- Calculating total stock value
- Exporting cleaned CSV data

---

## Final Project Goal

The final project will analyze structured data from CSV and JSON files.

It should be able to:

- Read raw input data
- Clean text fields
- Convert numeric values
- Detect invalid rows
- Count records by category or status
- Calculate simple totals
- Export a clean report

Example final output:

```python
{
    "total_records": 120,
    "valid_records": 113,
    "invalid_records": 7,
    "categories": {
        "food": 45,
        "tools": 30,
        "other": 38
    }
}
```

---

## What I Am Practicing

Through this repository, I am practicing:

- Working with structured data
- Reading and writing files safely
- Transforming raw strings into clean Python values
- Converting JSON data between strings, files and Python objects
- Reading and exporting CSV files
- Reusing algorithmic patterns such as counters, accumulators, filtering and grouping
- Handling edge cases and invalid data
- Building small but realistic data-processing scripts

---

## Edge Cases to Consider

The exercises and project should handle:

- Missing files
- Empty files
- Empty lists
- Invalid JSON content
- Missing CSV columns
- Empty CSV rows
- Invalid numeric values
- Unknown categories or statuses
- Output folders that do not exist yet

---

## Future Improvements

Possible future improvements:

- Add unit tests with `pytest`
- Add a proper CLI entry point
- Refactor the project into modules after the Python modules block
- Add type hints after the typing block
- Add a larger dataset
- Add a Pandas version later in the data learning path

---

## Tech Stack

- Python 3
- Standard library only:
  - `json`
  - `csv`
  - `pathlib`

No external dependency is required at this stage.

---

## Repository Status

In progress as part of my Python CSV/JSON and structured data learning path.

Current progress:

```text
JSON basics: completed
CSV basics: completed
File/data error handling: next step
Final CSV/JSON analyzer project: upcoming
```