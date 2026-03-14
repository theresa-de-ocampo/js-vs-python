import CheatsheetSection from '../CheatsheetSection.jsx'

function FunctionsSection() {
  const rows = [
    {
      description: 'Default Parameter Behavior',
      javascript: [
        ['function greeting(name, age=18) { /* body */ }'],
        [
          "greeting('Teriz') // Default Used",
          "greeting('Teriz', undefined) // Default Used",
          "greeting('Teriz', null) // Default NOT Used",
        ],
      ],
      python: [
        [
          'def greeting(name, age=18):',
          { text: '# body', className: 'indent-1' },
        ],
        ["greeting('Teriz') # Default used", "greeting('Teriz', None) # Default NOT used"],
      ],
    },
    {
      description: 'Named Function Arguments',
      javascript: [
        [
          '// JS does not support named arguments',
          '// but you can do:',
          "greeting({ name: 'Teriz', age: 26})",
        ],
      ],
      python: [["greeting(name='Teriz', age=26)"]],
    },
    {
      description: 'Return a Tuple',
      javascript: [['// No direct equivalent']],
      python: [['return amount, tax, total amount']],
    },
    {
      description: 'Return a Set',
      javascript: [['// No direct equivalent']],
      python: [['return { amount, tax, total amount }']],
    },
    {
      description: 'Return an Object',
      javascript: [['return { amount, tax, total amount }']],
      python: [['// TODO: After refresher on dictionaries']],
    },
  ]

  return <CheatsheetSection title="Functions" rows={rows} />
}

export default FunctionsSection
