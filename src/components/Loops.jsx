import CheatSheet from "./generic/CheatSheet.jsx";

export default function Loops() {
  const rows = [
    {
      description: "Counted Loop",
      javascript: [
        [
          "for (let i = 0; i < 5; i++)",
          "for (let i = 2; i < 10; i++)",
          "for (let i = 3; i <= 30; i+= 3)"
        ]
      ],
      python: [
        [
          "for i in range(5)",
          "for i in range(2, 10)",
          "for i in range(3, 31, 3)"
        ]
      ]
    },
    {
      description: "Increment Operator",
      javascript: [["++i", "i++"]],
      python: [["# No Equivalent"]]
    },
    {
      description: "Iterate Values",
      javascript: [
        [
          "for (const fruit of fruits) {",
          { text: "console.log(fruit)", className: "indent-1" },
          "}"
        ],
        ["fruits.forEach(fruit => console.log(fruit))"]
      ],
      python: [
        [
          "for fruit in fruits:",
          { text: "print(fruit)", className: "indent-1" }
        ]
      ]
    },
    {
      description: "Iterate With Index",
      javascript: [
        [
          "for (let i = 0; i < fruits.length; i++) {",
          { text: "console.log(fruits[i])", className: "indent-1" },
          "}"
        ],
        [
          "for (const [i, fruit] of fruits.entries()) {",
          { text: "console.log(i, fruit)", className: "indent-1" },
          "}"
        ]
      ],
      python: [
        [
          "for i in range(len(fruits)):",
          { text: "print(fruits[i])", className: "indent-1" }
        ],
        [
          "for i, fruit in enumerate(fruits):",
          {
            text: "print(i, fruit)",
            className: "indent-1"
          }
        ]
      ]
    },
    {
      description: "Start Index at 1",
      javascript: [
        [
          "fruits.forEach(",
          {
            text: "(fruit, i) => console.log(i + 1, fruit)",
            className: "indent-1"
          },
          ")"
        ]
      ],
      python: [
        [
          "for i, fruit in enumerate(fruits, 1):",
          { text: "print(i, fruit)", className: "indent-1" }
        ]
      ]
    },
    {
      description: "Transform",
      javascript: [
        [
          "const uppercased = fruits.map(",
          {
            text: "fruit => fruit.toUpperCase()",
            className: "indent-1"
          },
          ")"
        ]
      ],
      python: [
        ["uppercased = [fruit.upper() for fruit in fruits]"],
        ["uppercased = list(map(str.upper, fruits))"]
      ]
    }
  ];

  return <CheatSheet title="Loops" rows={rows} />;
}
