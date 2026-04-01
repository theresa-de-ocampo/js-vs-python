import CheatSheet from "./generic/CheatSheet";

export default function FileHandling() {
  const rows = [
    {
      description: "Script File Path",
      javascript: [["__filename"]],
      python: [["__file__"]]
    },
    {
      description: "Script Directory",
      javascript: [
        ["// CommonJS", "__dirname"],
        [
          "// ES Modules",
          "import { fileURLToPath } from 'url'",
          "import { dirname, sep } from 'path'",
          "const __dirname = dirname(",
          {
            text: "fileURLToPath(import.meta.url)",
            className: "indent-1"
          },
          ") + sep"
        ]
      ],
      python: [["from pathlib import Path", "dirname = Path(__file__).parent"]]
    },
    {
      description: "Path Object",
      javascript: [
        [
          "import { parse } from 'path'",
          "const p = parse(__filename)",
          " ",
          "p.root // C:\\",
          "p.dir  // C:\\app\\files\\",
          "p.base // demo.js",
          "p.ext  // .js",
          "p.name // demo"
        ]
      ],
      python: [
        [
          "from pathlib import Path",
          "p = Path(__file__)",
          " ",
          "p.anchor # c:\\",
          "p.parent # C:\\app\\files\\",
          "p.name   # demo.py",
          "p.suffix # .py",
          "p.stem   # demo"
        ]
      ]
    },
    {
      description: "Read Text File",
      javascript: [
        [
          "const contentBuffer = await fsPromises.readFile(",
          {
            text: "path.join(__dirname, 'files', 'hello.txt'),",
            className: "indent-1"
          },
          {
            text: "'utf-8'",
            className: "indent-1"
          },
          ")"
        ]
      ],
      python: [
        [
          "file_path = dirname / 'files' / 'hello.txt'",
          "with open(file_path, 'r', encoding='utf-8') as f:",
          {
            text: "contentStr = f.read()",
            className: "indent-1"
          }
        ]
      ]
    }
  ];

  return <CheatSheet title="File Handling" rows={rows} />;
}
