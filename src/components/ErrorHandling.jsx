import CheatSheet from "./generic/CheatSheet";

export default function ErrorHandling() {
  const rows = [
    {
      description: "Re-Throw Error",
      javascript: [
        [
          "try {",
          {
            text: "// some code",
            className: "indent-1"
          },
          "} catch (e) {",
          { text: "throw e", className: "indent-1" },
          "}"
        ]
      ],
      python: [
        [
          "try:",
          {
            text: "# some code",
            className: "indent-1"
          },
          "except:",
          {
            text: "raise",
            className: "indent-1"
          }
        ]
      ]
    },
    {
      description: "Error Narrowing",
      javascript: [
        [
          "try {",
          {
            text: "const dividend = 30",
            className: "indent-1"
          },
          {
            text: "const divisor = // some input",
            className: "indent-1"
          },
          {
            text: " ",
            className: "indent-1"
          },
          {
            text: "if (divisor === 0) {",
            className: "indent-1"
          },
          {
            text: "throw new Error('Division by zero')",
            className: "indent-2"
          },
          {
            text: "}",
            className: "indent-1"
          },
          {
            text: " ",
            className: "indent-1"
          },
          {
            text: "if (divisor > 30) {",
            className: "indent-1"
          },
          {
            text: "throw new RangeError('Must be <= 30')",
            className: "indent-2"
          },
          {
            text: "}",
            className: "indent-1"
          },
          {
            text: " ",
            className: "indent-1"
          },
          {
            text: "const result = dividend / divisor",
            className: "indent-1"
          },
          "} catch (e) {",
          {
            text: "if (e.message === 'Division by zero') {",
            className: "indent-1"
          },
          {
            text: "// Handler for division by zero",
            className: "indent-2"
          },
          {
            text: "} else if (e instanceof RangeError) {",
            className: "indent-1"
          },
          {
            text: "// Handler for invalid input (<= 30 rule)",
            className: "indent-2"
          },
          {
            text: "} else {",
            className: "indent-1"
          },
          {
            text: "// Handler for generic error",
            className: "indent-2"
          },
          {
            text: "}",
            className: "indent-1"
          },
          "}"
        ]
      ],
      python: [
        [
          "try:",
          {
            text: "dividend = 30",
            className: "indent-1"
          },
          {
            text: "divisor = # some input",
            className: "indent-1"
          },
          {
            text: " ",
            className: "indent-1"
          },
          {
            text: "if divisor > 30:",
            className: "indent-1"
          },
          {
            text: "raise ValueError('Must be <= 30')",
            className: "indent-2"
          },
          {
            text: " ",
            className: "indent-1"
          },
          {
            text: "result = 30 / divisor",
            className: "indent-1"
          },
          {
            text: " ",
            className: "indent-1"
          },
          "except ZeroDivisionError as e:",
          {
            text: "# Handler for division by zero",
            className: "indent-1"
          },
          "except ValueError as e:",
          {
            text: "# Handler for invalid input (<= 30 rule)",
            className: "indent-1"
          },
          "except Exception as e:",
          {
            text: "# Handler for generic error",
            className: "indent-1"
          }
        ]
      ]
    }
  ];

  return <CheatSheet title="Error Handling" rows={rows} />;
}
