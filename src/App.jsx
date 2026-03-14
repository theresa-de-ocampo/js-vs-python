import ArraysSection from './components/sections/ArraysSection.jsx'
import ArithmeticSection from './components/sections/ArithmeticSection.jsx'
import CommentsSection from './components/sections/CommentsSection.jsx'
import FunctionsSection from './components/sections/FunctionsSection.jsx'
import InputOutputSection from './components/sections/InputOutputSection.jsx'
import SetsSection from './components/sections/SetsSection.jsx'
import StringManipulationSection from './components/sections/StringManipulationSection.jsx'
import TuplesSection from './components/sections/TuplesSection.jsx'
import TypesAndTypeCheckingSection from './components/sections/TypesAndTypeCheckingSection.jsx'

const sections = [
  InputOutputSection,
  CommentsSection,
  StringManipulationSection,
  ArraysSection,
  TuplesSection,
  SetsSection,
  ArithmeticSection,
  TypesAndTypeCheckingSection,
  FunctionsSection,
]

function App() {
  return (
    <main className="app-shell">
      <header className="page-header">
        <p className="eyebrow">Learning Notes</p>
        <h1>JavaScript vs Python Cheat Sheet</h1>
        <p className="page-intro">
          Migrated from the original single HTML file into a Vite + React app,
          with one component per cheatsheet section.
        </p>
      </header>

      <div className="sections">
        {sections.map((Section) => (
          <Section key={Section.displayName ?? Section.name} />
        ))}
      </div>
    </main>
  )
}

export default App
