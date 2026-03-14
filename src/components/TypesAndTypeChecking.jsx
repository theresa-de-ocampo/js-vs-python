import CheatSheet from './generic/CheatSheet.jsx'

export default function TypesAndTypeChecking() {
  const rows = [
    {
      description: 'No Value',
      javascript: [['null']],
      python: [['None']],
    },
    {
      description: 'Get Variable Type',
      javascript: [['typeof value']],
      python: [['type(value)']],
    },
  ]

  return <CheatSheet title="Types & Type Checking" rows={rows} />
}
