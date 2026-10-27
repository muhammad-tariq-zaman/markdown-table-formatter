"""Markdown table formatter: align and normalise Markdown tables in a file."""
import argparse
import sys


def is_row(line):
    s = line.strip()
    return s.startswith("|") and s.endswith("|")


def is_separator(line):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return bool(cells) and all(set(c) <= set("-: ") and "-" in c for c in cells)


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def format_table(rows):
    widths = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))]
    out = []
    for idx, row in enumerate(rows):
        cells = [row[i].ljust(widths[i]) for i in range(len(row))]
        out.append("| " + " | ".join(cells) + " |")
        if idx == 0:
            sep = ["-" * max(3, widths[i]) for i in range(len(row))]
            out.append("| " + " | ".join(sep) + " |")
    return out


def format_text(text):
    lines, out, buf = text.splitlines(), [], []
    for line in lines:
        if is_row(line) and not is_separator(line):
            buf.append(split_row(line))
        else:
            if buf:
                out.extend(format_table(buf))
                buf = []
            if not is_separator(line):
                out.append(line)
    if buf:
        out.extend(format_table(buf))
    return "\n".join(out) + "\n"


def main(argv=None):
    p = argparse.ArgumentParser(description="Format Markdown tables in a file.")
    p.add_argument("file")
    p.add_argument("--output", default=None)
    args = p.parse_args(argv)
    result = format_text(open(args.file, encoding="utf-8").read())
    if args.output:
        open(args.output, "w", encoding="utf-8").write(result)
    else:
        sys.stdout.write(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
