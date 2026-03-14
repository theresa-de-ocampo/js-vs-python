import CheatSheet from "./generic/CheatSheet.jsx";

export default function StringManipulation() {
  const rows = [
    {
      description: "Capitalize first letter",
      javascript: [["str.charAt(0).toUpperCase() + str.slice(1)"]],
      python: [["capitalize()"]]
    },
    {
      description: "Title Case",
      javascript: [["// No direct equivalent"]],
      python: [["title()"]]
    },
    {
      description: "Uppercase",
      javascript: [["toUpperCase()"]],
      python: [["upper()"]]
    },
    {
      description: "Lowercase",
      javascript: [["toLowerCase()"]],
      python: [["lower()"]]
    },
    {
      description: "Length of String",
      javascript: [["msg.length"]],
      python: [["len(msg)"]]
    },
    {
      description: "Check Substring",
      javascript: [["msg.includes('Python')", "!msg.includes('Python')"]],
      python: [["'Python' in msg", "'Python' not in msg"]]
    },
    {
      description: "Count Substring Occurrence",
      javascript: [["// No direct equivalent", "// Use Regex"]],
      python: [["msg.count('Python')"]]
    },
    {
      description: "Slice String",
      javascript: [["msg.slice(2)"]],
      python: [["msg[2:]"]]
    },
    {
      description: "Find Substring Index",
      javascript: [
        [
          "// No direct equivalent",
          "// Closer concept:",
          "// findIndex() but it takes in a callback"
        ]
      ],
      python: [["msg.find('H')"]]
    },
    {
      description: "Replace Substring",
      javascript: [
        ["// Strings are immutable", "sentence.replace('JavaScript', 'Python')"]
      ],
      python: [
        ["// Strings are immutable", "sentence.replace('JavaScript', 'Python')"]
      ]
    },
    {
      description: "Split Strings",
      javascript: [
        [
          "msg.split(' ') // Splits by a single space",
          "msg.split() // Returns original array"
        ]
      ],
      python: [
        [
          "msg.split(' ') // Splits by a single space",
          "msg.split() // Splits by spaces"
        ]
      ]
    }
  ];

  return <CheatSheet title="String Manipulation" rows={rows} />;
}
