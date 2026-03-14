import CheatsheetSection from '../CheatsheetSection.jsx'

function TuplesSection() {
  const rows = [
    {
      description: 'Declaration',
      javascript: [
        [
          '// No direct equivalent, closest:',
          "const fruits = Object.freeze('Orange', 'Apple')",
        ],
        [
          '// Note that the TS Tuple has a different meaning',
          '// It enforces specific types per index, and it is mutable.',
          'let fruits : [name: string, count: int]',
        ],
      ],
      python: [['// Faster access because of immutability', "fruits = ('Orange', 'Apple')"]],
    },
    {
      description: 'Empty a Tuple',
      javascript: [['// No direct equivalent']],
      python: [['fruits = ()', 'fruits = tuple()']],
    },
  ]

  return (
    <CheatsheetSection
      title="Tuples"
      intro="An ordered, fixed-sized collection of elements."
      rows={rows}
    />
  )
}

export default TuplesSection
