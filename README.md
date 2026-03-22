# JavaScript vs Python Cheat Sheet

This repository is a JavaScript vs Python cheat sheet built while learning Python from a JavaScript background.

It combines quick language comparisons, learning notes, and small Python exercises collected while going through the Scrimba course [Learn Python](https://scrimba.com/learn-python-c03).

## What This Repository Contains

- `exercises/` contains Python code written while working through the course.
- The rest of the repository contains learning notes, including comparisons between JavaScript and Python.
- Most of the content is Python-focused because the goal of the repository is to support learning Python from a JavaScript perspective.

## How To Run

### View the cheat sheet app

Install dependencies:

```bash
npm install
```

Start the local development server:

```bash
npm run dev
```

Build the app:

```bash
npm run build
```

### Run Python exercises

Run any exercise file directly with Python:

```bash
python exercises/17-error-handling/division-by-zero.py
```

Another example:

```bash
python exercises/16-reading-files/dirname.py
```

---

## Personal Python Learning Notes

### [Why does Python use the `try-except-else` pattern?](https://stackoverflow.com/questions/16138232/is-it-a-good-practice-to-use-try-except-else-in-python)

```python
try:
    file = open("data.txt")
    content = file.read()
    processed = process(content)
    print(processed)
except Exception as e:
    print("Error:", e)
finally:
    file.close()
```

If `process(content)` fails, Python will still catch it even though that error has nothing to do with opening the file. This makes debugging harder because it becomes less clear which line failed.

```python
try:
    file = open("data.txt")
    content = file.read()
except Exception as e:
    print("Error reading file:", e)
else:
    processed = process(content)
    print(processed)
finally:
    file.close()
```

In this second version, the program will crash if `process(content)` fails. This is an intentional Python **design choice**.

> Only catch what is understood. Let everything else fail loudly.
