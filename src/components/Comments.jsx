import CheatSheet from "./generic/CheatSheet.jsx";

export default function Comments() {
  const rows = [
    {
      description: "Single Line Comment",
      javascript: [["// This is a comment"]],
      python: [["# This is a comment"]]
    },
    {
      description: "Multi Line Comment",
      javascript: [["/*", "This is a multiline", "comment", "*/"]],
      python: [
        [
          "'''",
          "No dedicated syntax",
          "for multiline comments.",
          "Use of triple quotes is discouraged",
          "as it is actually a string literal.",
          "If it appears on top of a module,",
          "class, or function,",
          "Python treats it as a docstring.",
          "Using triple quotes can accidentally",
          "modify documentation.",
          "'''"
        ]
      ]
    }
  ];

  return <CheatSheet title="Comments" rows={rows} />;
}
