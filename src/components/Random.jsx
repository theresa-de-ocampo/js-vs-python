import CheatSheet from "./generic/CheatSheet";

export default function Random() {
  const rows = [
    {
      description: "[0,1)",
      javascript: [["Math.random()"]],
      python: [["import random", "random.random()"]]
    },
    {
      description: "[min,max] Integers",
      javascript: [["Math.floor(Math.random() * (max - min + 1) + min)"]],
      python: [["random.randint(min, max)"]]
    },
    {
      description: "[2,100] Even Integers",
      javascript: [["// No direct equivalent"]],
      python: [["random.randrange(2, 101, 2)"]]
    },
    {
      description: "[1,100] Odd Integers",
      javascript: [["// No direct equivalent"]],
      python: [["random.randrange(1, 100, 2)"]]
    },
    {
      description: "Pick from Array",
      javascript: [["fruits[Math.floor(Math.random() * fruits.length)]"]],
      python: [["random.choice(fruits)"]]
    },
    {
      description: "Multiple Unique Draws",
      javascript: [["// No direct equivalent"]],
      python: [["random.sample(fruits, 3)"]]
    },
    {
      description: "Multiple Non-Unique Draws",
      javascript: [["// No direct equivalent"]],
      python: [["random.choice(fruits, 3)"]]
    },
    {
      description: "Shuffle an Array",
      javascript: [
        ["// No direct equivalent", "// Implement Fisher–Yates Shuffle"]
      ],
      python: [["random.shuffle(fruits)"]]
    }
  ];

  return <CheatSheet title="Randomness" rows={rows} />;
}
