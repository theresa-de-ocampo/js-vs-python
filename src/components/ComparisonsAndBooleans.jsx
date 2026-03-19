import CheatSheet from "./generic/CheatSheet.jsx";

export default function ComparisonsAndBooleans() {
  const rows = [
    {
      description: "Equality",
      javascript: [
        [
          "// JS is loosely typed",
          "5 == 5 // true",
          "5 == '5' // true",
          "5 === '5' // false"
        ]
      ],
      python: [
        [
          "# Python is strongly typed",
          "# It does not have ===",
          "# Because == is already strict",
          "5 == 5 # True",
          "5 == '5' # False"
        ]
      ]
    },
    {
      description: "Value Equality",
      javascript: [["// No direct equivalent"]],
      python: [["a = [3,7,42]", "b = a", "print(a == b) # True"]]
    },
    {
      description: "Reference Equality",
      javascript: [
        ["const a = [3,7,42]", "const b = a", "console.log(a == b) // true"]
      ],
      python: [
        [
          "a = [3,7,42]",
          "b = a",
          "c = [3,7,42]",
          "print(a is b) # True",
          "print(id(a), id(b)) # 2 2",
          "print(a is c) # False"
        ]
      ]
    },
    {
      description: "Truthy / Falsy",
      javascript: [["const fruits = []", "Boolean(fruits) // true"]],
      python: [["fruits = []", "bool(fruits) # False"]]
    }
  ];

  return <CheatSheet title="Comparisons and Booleans" rows={rows} />;
}
