import CheatSheet from "./generic/CheatSheet.jsx";

export default function Arrays() {
  const rows = [
    {
      description: "Collection Type",
      javascript: [["// Arrays can contain mixed types"]],
      python: [["# Lists can contain mixed types"]]
    },
    {
      description: "Length",
      javascript: [["fruits.length"]],
      python: [["len(fruits)"]]
    },
    {
      description: "Last Element",
      javascript: [["fruits.at(-1)"]],
      python: [["fruits[-1]"]]
    },
    {
      description: "Count Occurrences",
      javascript: [
        [
          "fruits.reduce((tally, fruit) => {",
          {
            text: "return tally + (fruit === 'Orange')",
            className: "indent-1"
          },
          "}, 0)"
        ]
      ],
      python: [["fruits.count('Orange')"]]
    },
    {
      description: "Slice",
      javascript: [["fruits.slice(2,4)"]],
      python: [["fruits[2:4]"]]
    },
    {
      description: "Find Index",
      javascript: [
        [
          "fruits.findIndex(f => f === 'Orange')",
          "fruits.findIndex(f => f === 'Broccoli') // -1"
        ]
      ],
      python: [
        ["fruits.index('Orange')", "fruits.index('Broccoli') // ValueError"]
      ]
    },
    {
      description: "Sort",
      javascript: [["fruits.sort()", "const sortedFruits = fruits.toSorted()"]],
      python: [["fruits.sort()", "sorted_fruits = sorted(fruits)"]]
    },
    {
      description: "Reverse Sort",
      javascript: [["fruits.sort().reverse()"]],
      python: [["fruits.sort(reverse=True)"]]
    },
    {
      description: "Reverse Order",
      javascript: [["fruits.reverse()", "fruits.toReversed()"]],
      python: [["fruits.reverse()", "list(reversed(fruits))", "fruits[::-1]"]]
    },
    {
      description: "Sorting Numbers",
      javascript: [
        [
          "// JS sorts numbers as strings by default",
          "tally.sort((a, b) => a - b)"
        ],
        ["tally.toSorted((a, b) => Math.abs(a) - Math.abs(b))"]
      ],
      python: [
        ["# Works normally for numbers", "tally.sort()"],
        ["sorted(tally, key=abs)"]
      ]
    },
    {
      description: "Sort 2D Array",
      javascript: [["fruitsTally.toSorted((a, b) => a[1] - b[1])"]],
      python: [["sorted(fruits_tally, key=lambda item: item[1])"]]
    },
    {
      description: "Minimum Value",
      javascript: [
        [
          "tally.reduce((a, b) => Math.min(a, b))",
          "// Alternative but slower for large arrays",
          "Math.min(...tally)"
        ]
      ],
      python: [["min(tally)"]]
    },
    {
      description: "Maximum Value",
      javascript: [["tally.reduce((a, b) => Math.max(a, b))"]],
      python: [["max(tally)"]]
    },
    {
      description: "Sum Values",
      javascript: [["tally.reduce((total, n) => total + n, 0)"]],
      python: [["sum(tally)"]]
    },
    {
      description: "Combine Two Arrays",
      javascript: [["const fruitsAndVeggies = fruits.concat(veggies)"]],
      python: [["fruits_and_veggies = fruits + veggies"]]
    },
    {
      description: "Extend Existing Array",
      javascript: [["fruits.push(...veggies)"]],
      python: [["fruits.extend(veggies)"]]
    },
    {
      description: "Add Element to End",
      javascript: [["fruits.push('Mango')"]],
      python: [["fruits.append('Mango')"]]
    },
    {
      description: "Insert at Specific Index",
      javascript: [["fruits.splice(index, 0, 'Mango')"]],
      python: [["fruits.insert(index, 'Mango')"]]
    },
    {
      description: "Remove First Occurrence",
      javascript: [
        [
          "const i = fruits.indexOf('Orange')",
          "if (i !== -1) fruits.splice(i, 1)"
        ]
      ],
      python: [["fruits.remove('Orange')"]]
    },
    {
      description: "Remove Last Element",
      javascript: [["fruits.pop()"]],
      python: [["fruits.pop()"]]
    },
    {
      description: "Remove at Specific Index",
      javascript: [["fruits.splice(2, 1)", "fruits.splice(-2, 1)"]],
      python: [["fruits.pop(2)", "fruits.pop(-2)", "del fruits[2]"]]
    },
    {
      description: "Empty an Array",
      javascript: [["fruits = []"]],
      python: [["fruits = []", "fruits.clear()", "fruits = list()"]]
    },
    {
      description: "Shallow Copy",
      javascript: [
        [
          "const newFruits = [...fruits]",
          "const newFruits = fruits.slice()",
          "const newFruits = Array.from(fruits)"
        ]
      ],
      python: [
        [
          "new_fruits = fruits[:]",
          "new_fruits = fruits.copy()",
          "new_fruits = list(fruits)"
        ]
      ]
    },
    {
      description: "Deep Copy",
      javascript: [["const newEmployees = structuredClone(employees)"]],
      python: [["import copy", "new_employees = copy.deepcopy(employees)"]]
    },
    {
      description: "Join to String",
      javascript: [["fruits.join(',')"]],
      python: [["','.join(fruits)"]]
    }
  ];

  return <CheatSheet title="Arrays" rows={rows} />;
}
