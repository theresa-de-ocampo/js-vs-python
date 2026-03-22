# JavaScript vs Python CheatSheet

## [Why does Python use the `try-except-else` pattern?](https://stackoverflow.com/questions/16138232/is-it-a-good-practice-to-use-try-except-else-in-python)

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

If `process(content)` fails, Python will still catch it — even though that error has nothing to do with opening the file. This makes debugging harder as it's difficult to tell which line failed.

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

In this second version, the program will crash if `process(content)` fails. This is a **design decision** in Python.

> Only catch what you understand. Let everything else fail loudly.
