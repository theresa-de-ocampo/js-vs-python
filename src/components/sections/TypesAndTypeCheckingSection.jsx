import CheatsheetSection from '../CheatsheetSection.jsx'

function TypesAndTypeCheckingSection() {
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

  return <CheatsheetSection title="Types & Type Checking" rows={rows} />
}

export default TypesAndTypeCheckingSection
