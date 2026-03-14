import CheatSheet from './generic/CheatSheet.jsx'

export default function Arithmetic() {
  const rows = [
    {
      description: 'Floor Division',
      javascript: [['Math.floor()']],
      python: [['//']],
    },
    {
      description: 'Round',
      javascript: [['Math.round()']],
      python: [['round()']],
    },
    {
      description: 'Power',
      javascript: [['Math.pow()', '**']],
      python: [['**']],
    },
    {
      description: 'Number Formatting',
      javascript: [['price.toFixed(2)']],
      python: [['f"{price:.2f}"']],
    },
  ]

  return <CheatSheet title="Arithmetic" rows={rows} />
}
