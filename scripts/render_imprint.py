"""Render the public provider page from deployment-only environment values."""

from __future__ import annotations

import argparse
import html
import os
from pathlib import Path


FIELDS = ("PROVIDER_NAME", "PROVIDER_STREET", "PROVIDER_CITY", "PROVIDER_COUNTRY")


def render(template: Path, output: Path) -> None:
    values = {name: os.environ.get(name, "").strip() for name in FIELDS}
    missing = [name for name, value in values.items() if not value]
    if missing:
        raise SystemExit("Missing required deployment values: " + ", ".join(missing))

    document = template.read_text(encoding="utf-8")
    for name, value in values.items():
        document = document.replace("{{" + name + "}}", html.escape(value, quote=True))

    unresolved = [name for name in FIELDS if "{{" + name + "}}" in document]
    if unresolved:
        raise SystemExit("Unresolved provider fields: " + ", ".join(unresolved))

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", type=Path, default=Path("imprint.template.html"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    render(args.template, args.output)


if __name__ == "__main__":
    main()
