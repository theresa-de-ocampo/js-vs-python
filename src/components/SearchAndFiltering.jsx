import CheatSheet from "./generic/CheatSheet.jsx";

export default function SearchAndFiltering() {
  const rows = [
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
      description: "Any Match",
      javascript: [["states.some(state => state === 'suspended')"]],
      python: [["any(state == 'suspended' for state in states)"]]
    },
    {
      description: "First Match",
      javascript: [["employees.find(e => e.fname === 'Teriz')"]],
      python: [["next(e for e in employees if e['fname'] == 'Teriz')"]]
    },
    {
      description: "Filter + Transform",
      javascript: [
        [
          "fruits",
          {
            text: ".filter(fruit => fruit.includes('a'))",
            className: "indent-1"
          },
          {
            text: ".map(fruit => fruit.toUpperCase())",
            className: "indent-1"
          }
        ]
      ],
      python: [["[fruit.upper() for fruit in fruits if 'a' in fruit]"]]
    }
  ];

  return (
    <CheatSheet
      title="Search and Filtering"
      intro={
        <>
          <code>fruits</code> and <code>states</code> are arrays of strings, and{" "}
          <code>employees</code> is an array of objects.
        </>
      }
      rows={rows}
    />
  );
}
