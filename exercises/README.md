# Python Learning Notes

## 1. PyCharm vs. VS Code + Extensions

- PyCharm feels better than VS Code for Python out the box, i.e., without extra configuration or installation. But [Codex support is still buggy](https://github.com/openai/codex/issues/14883).
- VS Code's Git Integration feels better—there's a badge for the total number of files edited. Built-in Git Integration with PyCharm feels confusing. TO DO: Research a little bit more on PyCharm's Git settings and perhaps extensions.

### VS Code Pylance Extension

PyCharm warns that tuples don't support item assignment.

```python
fruits = ("Orange", "Apple")
fruits[0] = "Strawberry"
print(fruits[0])
```

In order for VS Code to immediately detect this issue:

1.  Install Pylance
2.  Set the `python.analysis.typeCheckingMode` setting from `basic` to `strict`

### Pylance `strict` vs `standard` mode

While this fixes the tuple assignment warning, it requires type hinting for class attributes.

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
```

The code above will cause the following problems to be emitted.

```
Type of parameter "owner" is unknown.
Type of parameter "balance" is unknown.
```

If you don't want mandatory type checking, set `python.analysis.typeCheckingMode` to `standard` instead.

## 2. [Why does Python use the `try-except-else` pattern?](https://stackoverflow.com/questions/16138232/is-it-a-good-practice-to-use-try-except-else-in-python)

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

## 3. Tuples vs `collections.abc.Sequence`

- `Sequence` is better if you want to interface flexibility.
- `tuple` is better when you want concrete immutability or fixed shape.

### When to use `tuple`

- Fixed-length records: `rgb: tuple[int, int, int]`
- Exact Shape Matters: `fruits: tuple[str, int]`

### When to use `Sequence`

If the dataclasses are acting like blueprints for structured data, and the code only cares that the values are:

- ordered
- iterable
- indexable

using `Sequence` provides the following benefits:

- more reusable
- less restrictive
- easier to construct from different parts of the codebase
