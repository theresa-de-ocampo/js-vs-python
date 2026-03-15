import CheatSheet from "./generic/CheatSheet.jsx";

export default function TypesAndTypeChecking() {
  const rows = [
    {
      description: "No Value",
      javascript: [["null"]],
      python: [["None"]]
    },
    {
      description: "Get Variable Type",
      javascript: [["typeof value"]],
      python: [["type(value)"]]
    },
    {
      description: "Implicit Type Coercion",
      javascript: [
        [
          "// JS is loosely typed",
          "console.log('My fav no. is ' + 7) // Allowed",
          "console.log(42 + false) // 7"
        ]
      ],
      python: [
        [
          "// Python is strongly typed",
          "print('My fav no. is' + 7) // TypeError",
          "print(7 + False) // 7 (Compatible Coercion)"
        ]
      ]
    }
  ];

  return <CheatSheet title="Types & Type Checking" rows={rows} />;
}
