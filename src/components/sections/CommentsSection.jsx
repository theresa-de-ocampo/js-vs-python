import CheatsheetSection from '../CheatsheetSection.jsx'
import { cheatsheetSections } from '../../data/cheatsheetData.js'

function CommentsSection() {
  return <CheatsheetSection {...cheatsheetSections.comments} />
}

export default CommentsSection
