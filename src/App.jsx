import Arrays from './components/Arrays.jsx'
import Arithmetic from './components/Arithmetic.jsx'
import Comments from './components/Comments.jsx'
import Functions from './components/Functions.jsx'
import InputOutput from './components/InputOutput.jsx'
import Sets from './components/Sets.jsx'
import StringManipulation from './components/StringManipulation.jsx'
import Tuples from './components/Tuples.jsx'
import TypesAndTypeChecking from './components/TypesAndTypeChecking.jsx'

const sections = [
  InputOutput,
  Comments,
  StringManipulation,
  Arrays,
  Tuples,
  Sets,
  Arithmetic,
  TypesAndTypeChecking,
  Functions,
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
