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

## 4. ReportLab

### Flowable

A flowable is a piece of content that can be placed into the document flow. You can think of it as "one renderable block" in the PDF story.

Examples:

- `Paragraph`
- `LongTable`
- `Spacer`
- `PageBreak`
- `TableOfContents`

When you build the PDF, you create a list called `story`, and that list is just an ordered list of flowables. ReportLab then lays them out one after another across pages.

```python
story = []
```

Section builders append things like headings and tables. Those appended objects are flowables.

#### `afterFlowable`

`afterFlowable` is a ReportLab lifecycle hook. It is called automatically by `BaseDocTemplate` after each flowable is rendered during `doc.multiBuild(story)`, so you would not expect any direct calls from your own modules.

### `bookmark_name`

`bookmark_name` is the internal PDF anchor ID for a heading. Each heading gets a unique value like:

```
heading-1
heading-2
```

Then, `afterFlowable` uses it here:

```
self.canv.bookmarkPage(bookmark_name)
self.notify("TOCEntry", (level, text, self.page, bookmark_name))
```

What that does:

- `bookmarkPage(bookmark_name)` creates a named destination in the PDF at the current page.
- the table of content entry stores that destination name.
- PDF outline/sidebar entries also use it.

So `bookmark_name` is what lets the TOC or PDF bookmarks jump to the correct setion, instead of only displaying page numbers.

Without it, you could still print the heading text, but clickable navigation targets would not exist.

- `toc_level` says what the level heading is.
- `bookmark_name` says where that heading lives in the PDF.
