import CheatSheet from "./generic/CheatSheet.jsx";

export default function Loops() {
  const rows = [
    {
      description: "Prefix & Postfix Increment",
      javascript: [["++i", "i++"]],
      python: [["# No Equivalent"]]
    },
    {
      description: "for Loop",
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
      description: "Loop Through Elements",
      javascript: [
        ["fruits.map(f => console.log(f))"],
        [
          "for (let i = 0; i < fruits.length; i++) {",
          { text: "console.log(fruits[f])", className: "indent-1" },
          "}"
        ],
        ["fruits.map((f, i) => console.log(i + 1, f))"]
      ],
      python: [
        ["for f in fruits:", { text: "print(f)", className: "indent-1" }],
        [
          "for i in range(len(fruits)):",
          { text: "print(fruits[i])", className: "indent-1" }
        ],
        [
          "for i, fruit in enumerate(fruits):",
          {
            text: "print(i + 1, fruit)",
            className: "indent-1"
          },
          " ",
          "for i, fruit in enumerate(fruits, 1):",
          {
            text: "print(i, fruit)",
            className: "indent-1"
          },
          " ",
          "type(enumerate(fruits)) // <class 'enumerate'>"
        ]
      ]
    }
  ];

  return <CheatSheet title="Loops" rows={rows} />;
}
