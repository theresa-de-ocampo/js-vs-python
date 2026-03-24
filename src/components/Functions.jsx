import CheatSheet from "./generic/CheatSheet.jsx";

export default function Functions() {
  const rows = [
    {
      description: "Default Parameters",
      javascript: [
        [
          "function greeting(name, age=18) {",
          { text: "/* body */", className: "indent-1" },
          "}"
        ],
        [
          "greeting('Teriz') // Default Used",
          "greeting('Teriz', undefined) // Default Used",
          "greeting('Teriz', null) // Default NOT Used"
        ]
      ],
      python: [
        [
          "def greeting(name, age=18):",
          { text: "# body", className: "indent-1" }
        ],
        [
          "greeting('Teriz') # Default used",
          "greeting('Teriz', None) # Default NOT used"
        ]
      ]
    },
    {
      description: "Named Arguments",
      javascript: [
        [
          "// JS does not support named arguments",
          "// but you can do:",
          "greeting({ name: 'Teriz', age: 26})"
        ]
      ],
      python: [["greeting(name='Teriz', age=26)"]]
    },
    {
      description: "Return Tuple",
      javascript: [["// No direct equivalent"]],
      python: [["return amount, tax, total amount"]]
    },
    {
      description: "Return Set",
      javascript: [["// No direct equivalent"]],
      python: [["return { amount, tax, total amount }"]]
    },
    {
      description: "Return Object",
      javascript: [["return { amount, tax, total amount }"]],
      python: [["// TODO: After refresher on dictionaries"]]
    },
    {
      description: "Short-Hand Notation",
      javascript: [["// Arrow Functions", "const multiply = (x, y) => x * y"]],
      python: [["# Lambda Functions", "multiply = lambda x, y: x * y"]]
    }
  ];

  return <CheatSheet title="Functions" rows={rows} />;
}
