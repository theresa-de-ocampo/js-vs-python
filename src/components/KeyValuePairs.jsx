import CheatSheet from "./generic/CheatSheet";

export default function KeyValuePairs() {
  const rows = [
    {
      description: "Declaration",
      javascript: [
        [
          "// Object",
          "const employee = {",
          { text: "fname: 'Teriz',", className: "indent-1" },
          { text: "lname: 'De Ocampo',", className: "indent-1" },
          { text: "age: 26", className: "indent-1" },
          "}"
        ]
      ],
      python: [
        [
          "// Dictionary",
          "employee = {",
          { text: "'fname': 'Teriz',", className: "indent-1" },
          { text: "'lname': 'De Ocampo',", className: "indent-1" },
          { text: "'age': 26", className: "indent-1" },
          "}"
        ]
      ]
    },
    {
      description: "Property Access",
      javascript: [["employee.fname", "employee['fname']"]],
      python: [["employee['fname']"]]
    },
    {
      description: "Access Non-Existent Property",
      javascript: [
        ["employee.salary // undefined", "employee.salary || 'not found'"]
      ],
      python: [
        [
          "employee['salary'] // KeyError",
          "employee.get('salary') // None",
          "employee.get('salary', 'not found')"
        ]
      ]
    },
    {
      description: "Update a Property",
      javascript: [["employee.age = 27"]],
      python: [["employee['age'] = 27", "employee.update({ 'age': 27 })"]]
    },
    {
      description: "Delete a Property",
      javascript: [["delete employee.age"]],
      python: [["del employee['age']"]]
    },
    {
      description: "Get Keys",
      javascript: [["Object.keys(employee)"]],
      python: [["employee.keys()"]]
    },
    {
      description: "Get Values",
      javascript: [["Object.values(employee)"]],
      python: [["employee.values()"]]
    },
    {
      description: "Get Keys & Values",
      javascript: [
        ["Object.entries(employee)"],
        [
          "for (const [k, v] of Object.entries(employee))",
          { text: "console.log(k, v)", className: "indent-1" }
        ]
      ],
      python: [
        ["employee.items()"],
        [
          "for k, k in employee.items():",
          { text: "print(k, v)", className: "indent-1" }
        ]
      ]
    },
    {
      description: "Length",
      javascript: [["Object.keys(employee).length"]],
      python: [["len(employee)"]]
    },
    {
      description: "Check if Property Exists",
      javascript: [["Object.hasOwn(employee, 'salary'))"]],
      python: [["'salary' in employee"]]
    },
    {
      description: "Merge Objects",
      javascript: [["{...order, ...payment}"]],
      python: [["{**order, **payment}"]]
    },
    {
      description: "Find first element that passes the test",
      javascript: [["employees.find(e => e.name === 'Teriz')"]],
      python: [["next(e for e in employees if e['fname'] == 'Teriz')"]]
    }
  ];

  return <CheatSheet title="Key Value Pairs" rows={rows} />;
}
