# Unique ID Generator

A Twitter Snowflake-inspired distributed unique ID generator implemented in Python.

## Features

- 64-bit IDs
- Thread-safe
- Time sortable
- Worker ID support
- FastAPI endpoint
- Unit tests
- Benchmark utility

## Project Structure

```
id_generator/
tests/
app.py
benchmark.py
```

## Install

```bash
pip install -r requirements.txt
```

## Run API

```bash
uvicorn app:app --reload
```

Open:

http://127.0.0.1:8000/docs

## Run Tests

```bash
pytest
```

## Benchmark

```bash
python benchmark.py
```