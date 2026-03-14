import CheatsheetSection from '../CheatsheetSection.jsx'
import { cheatsheetSections } from '../../data/cheatsheetData.js'

function InputOutputSection() {
  return <CheatsheetSection {...cheatsheetSections.inputOutput} />
}

export default InputOutputSection
