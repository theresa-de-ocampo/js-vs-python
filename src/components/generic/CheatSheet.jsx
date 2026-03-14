function renderLine(line, index) {
  if (typeof line === "string") {
    return <span key={index}>{line}</span>;
  }

  return (
    <span key={index} className={line.className}>
      {line.text}
    </span>
  );
}

function CodeStack({ blocks }) {
  return (
    <div className="stack">
      {blocks.map((block, blockIndex) => (
        <code key={blockIndex}>
          {block.map((line, lineIndex) => renderLine(line, lineIndex))}
        </code>
      ))}
    </div>
  );
}

export default function CheatSheet({ title, intro, rows }) {
  return (
    <section className="cheatsheet-section">
      <div className="section-heading">
        <h2>{title}</h2>
        {intro ? <p>{intro}</p> : null}
      </div>

      <table>
        <thead>
          <tr>
            <th>Description</th>
            <th>JavaScript</th>
            <th>Python</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((row) => (
            <tr key={row.description}>
              <td data-label="Description">{row.description}</td>
              <td data-label="JavaScript">
                <CodeStack blocks={row.javascript} />
              </td>
              <td data-label="Python">
                <CodeStack blocks={row.python} />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}
