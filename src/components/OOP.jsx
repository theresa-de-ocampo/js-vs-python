import CheatSheat from "./generic/CheatSheet";

export default function OOP() {
  const rows = [
    {
      description: "Declaration",
      javascript: [
        [
          "class Account {",
          {
            text: "public owner: string",
            className: "indent-1"
          },
          {
            text: "private _balance: number",
            className: "indent-1"
          },
          " ",
          {
            text: "constructor(owner: string, balance: number) {",
            className: "indent-1"
          },
          {
            text: "this.owner = owner",
            className: "indent-2"
          },
          {
            text: "this._balance = balance",
            className: "indent-2"
          },
          {
            text: "}",
            className: "indent-1"
          },
          " ",
          {
            text: "deposit(amount: number): number {",
            className: "indent-1"
          },
          {
            text: "if (amount <= 0)",
            className: "indent-2"
          },
          {
            text: "throw new Error('Invalid deposit amount')",
            className: "indent-3"
          },
          " ",
          {
            text: "this._balance += amount",
            className: "indent-2"
          },
          {
            text: "return this._balance",
            className: "indent-2"
          },
          {
            text: "}",
            className: "indent-1"
          },
          " ",
          {
            text: "get balance() {",
            className: "indent-1"
          },
          {
            text: "return this._balance",
            className: "indent-2"
          },
          {
            text: "}",
            className: "indent-1"
          },
          "}",
          " ",
          "const myAccount = new Account('Teriz', 30000)"
        ]
      ],
      python: [
        [
          "class Account:",
          {
            text: "def __init__(self, owner, balance):",
            className: "indent-1"
          },
          {
            text: "self.owner = owner",
            className: "indent-2"
          },
          {
            text: "self._balance = balance",
            className: "indent-2"
          },
          " ",
          {
            text: "def deposit(self, amount):",
            className: "indent-1"
          },
          {
            text: "if amount <= 0:",
            className: "indent-2"
          },
          {
            text: "raise ValueError('Invalid deposit amount')",
            className: "indent-3"
          },
          " ",
          {
            text: "self._balance += amount",
            className: "indent-2"
          },
          {
            text: "return self._balance",
            className: "indent-2"
          },
          " ",
          {
            text: "@property",
            className: "indent-1"
          },
          {
            text: "def balance(self):",
            className: "indent-1"
          },
          {
            text: "return self._balance",
            className: "indent-2"
          },
          " ",
          "my_account = Account('Teriz', 30000)"
        ]
      ]
    },
    {
      description: "Inheritance",
      javascript: [
        [
          "class Person {",
          {
            text: "constructor(",
            className: "indent-1"
          },
          {
            text: "public fname: string,",
            className: "indent-2"
          },
          {
            text: "public lname: string",
            className: "indent-2"
          },
          {
            text: ") {}",
            className: "indent-1"
          },
          " ",
          {
            text: "walk() {",
            className: "indent-1"
          },
          {
            text: "console.log('Walking')",
            className: "indent-2"
          },
          {
            text: "}",
            className: "indent-1"
          },
          "}",
          " ",
          "class Student extends Person {",
          {
            text: "constructor(",
            className: "indent-1"
          },
          {
            text: "public readonly studentId: number,",
            className: "indent-2"
          },
          {
            text: "fname: string,",
            className: "indent-2"
          },
          {
            text: "lname: string",
            className: "indent-2"
          },
          {
            text: ") {",
            className: "indent-2"
          },
          {
            text: "super(fname, lname)",
            className: "indent-3"
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
          "class Person:",
          {
            text: "def __init__(self, fname, lname):",
            className: "indent-1"
          },
          {
            text: "self.fname = fname",
            className: "indent-2"
          },
          {
            text: "self.lname = lname",
            className: "indent-2"
          },
          " ",
          {
            text: "def walk(self):",
            className: "indent-1"
          },
          {
            text: "print('Walking')",
            className: "indent-2"
          },
          " ",
          "class Student(Person):",
          {
            text: "def __init__(self, student_id, fname, lname):",
            className: "indent-1"
          },
          {
            text: "super().__init__(fname, lname)",
            className: "indent-2"
          },
          {
            text: "self._student_id = student_id",
            className: "indent-2"
          },
          " ",
          {
            text: "@property",
            className: "indent-1"
          },
          {
            text: "def student_id(self):",
            className: "indent-1"
          },
          {
            text: "return self._student_id",
            className: "indent-2"
          }
        ]
      ]
    },
    {
      description: "Multiple Inheritance",
      javascript: [
        ["// No direct equivalent", "// Closest would be interfaces"]
      ],
      python: [
        [
          "class WorkingStudent(Employee, Student):",
          {
            text: "# ...",
            className: "indent-1"
          }
        ]
      ]
    },
    {
      description: "Instance Of",
      javascript: [["john instanceof Person"]],
      python: [["john instanceof Person"]]
    }
  ];

  return (
    <CheatSheat
      title="Object-Oriented Programming (OOP)"
      intro={
        <>
          This section uses <b>TypeScript</b> to illustrate object-oriented
          concepts in JavaScript, since it adds features like access modifiers
          and abstract classes that make OOP patterns easier to understand and
          compare with Python.
        </>
      }
      rows={rows}
    />
  );
}
