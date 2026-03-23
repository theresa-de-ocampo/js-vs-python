import Arrays from "./components/Arrays.jsx";
import Arithmetic from "./components/Arithmetic.jsx";
import Comments from "./components/Comments.jsx";
import ComparisonsAndBooleans from "./components/ComparisonsAndBooleans.jsx";
import ErrorHandling from "./components/ErrorHandling.jsx";
import FileHandling from "./components/FileHandling.jsx";
import Functions from "./components/Functions.jsx";
import InputOutput from "./components/InputOutput.jsx";
import KeyValuePairs from "./components/KeyValuePairs.jsx";
import Loops from "./components/Loops.jsx";
import OOP from "./components/OOP.jsx";
import SearchAndFiltering from "./components/SearchAndFiltering.jsx";
import Sets from "./components/Sets.jsx";
import StringManipulation from "./components/StringManipulation.jsx";
import Tuples from "./components/Tuples.jsx";
import TypesAndTypeChecking from "./components/TypesAndTypeChecking.jsx";

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
  ComparisonsAndBooleans,
  Loops,
  KeyValuePairs,
  SearchAndFiltering,
  FileHandling,
  ErrorHandling,
  OOP
];

function App() {
  return (
    <main className="app-shell">
      <header className="page-header">
        <p className="eyebrow">Learning Notes</p>
        <h1>JavaScript vs Python Cheat Sheet</h1>
        <p className="page-intro">
          Written by{" "}
          <a href="https://www.linkedin.com/in/ma-theresa7/">Teriz De Ocampo</a>
          . You can check out this{" "}
          <a href="https://github.com/theresa-de-ocampo/js-vs-python">repo</a>{" "}
          if you wish to contribute.
        </p>
      </header>

      <div className="sections">
        {sections.map((Section) => (
          <Section key={Section.displayName ?? Section.name} />
        ))}
      </div>
    </main>
  );
}

export default App;
