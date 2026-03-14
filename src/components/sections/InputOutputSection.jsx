import CheatsheetSection from '../CheatsheetSection.jsx'

function InputOutputSection() {
  const rows = [
    {
      description: 'Logging',
      javascript: [['console.log()']],
      python: [['print()']],
    },
    {
      description: 'User Input',
      javascript: [
        ['// Method 1', 'process.argv.slice(2)'],
        ['// Method 2', '// Built-in readline module'],
        ['// Method 3', '// readline-sync package'],
        ['// Method 4 (browser)', 'prompt()'],
      ],
      python: [['input()']],
    },
    {
      description: 'String Interpolation',
      javascript: [['`Hi ${name}`']],
      python: [['f"Hi {name}"']],
    },
  ]

  return <CheatsheetSection title="Input & Output" rows={rows} />
}

export default InputOutputSection
