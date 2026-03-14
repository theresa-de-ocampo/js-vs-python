import CheatsheetSection from '../CheatsheetSection.jsx'
import { cheatsheetSections } from '../../data/cheatsheetData.js'

function SetsSection() {
  return <CheatsheetSection {...cheatsheetSections.sets} />
}

export default SetsSection
