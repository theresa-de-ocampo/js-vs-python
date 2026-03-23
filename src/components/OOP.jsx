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
          "}"
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
            text: "self.__balance = balance",
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
            text: "self.__balance += amount",
            className: "indent-2"
          },
          {
            text: "return self.__balance",
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
            text: "return self.__balance",
            className: "indent-2"
          }
        ]
      ]
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
