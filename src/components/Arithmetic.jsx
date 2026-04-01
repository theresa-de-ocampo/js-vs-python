import CheatSheet from "./generic/CheatSheet.jsx";

export default function Arithmetic() {
  const rows = [
    {
      description: "Floor Division",
      javascript: [["Math.floor(n)"]],
      python: [["//"]]
    },
    {
      description: "Round to Whole Number",
      javascript: [["// Round Half Up", "Math.round(n)"]],
      python: [["# Banker's Rounding", "round()"]]
    },
    {
      description: "Round to 2 Decimal Places",
      javascript: [["Math.round((n + Number.EPSILON) * 100) / 100"]],
      python: [["round(n, 2)"]]
    },
    {
      description: "Power",
      javascript: [["Math.pow(base, expo)", "base ** expo"]],
      python: [["base ** expo"]]
    },
    {
      description: "Number Formatting",
      javascript: [["price.toFixed(2)"]],
      python: [['f"{price:.2f}"']]
    }
  ];

  return <CheatSheet title="Arithmetic" rows={rows} />;
}
