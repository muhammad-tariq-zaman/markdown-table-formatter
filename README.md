# markdown-table-formatter

Align and normalise Markdown tables in a file: columns are padded to the
widest cell, separator rows are rebuilt, and non-table lines are left alone.

## How to run

```bash
python3 main.py notes.md --output notes-formatted.md
python3 main.py notes.md
```

## Example output (sample from test fixture data)

```text
| Name           | Age |
| -------------- | --- |
| Ali            | 30  |
| Muhammad Tariq | 24  |
```

Standard library only. No network access.
