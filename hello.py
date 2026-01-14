#!/usr/bin/env python
# dirty python hello appsec world
# works in python3 / python / pypy

#!/usr/bin/env python3
"""Hello AppSec World (patch2 style)."""

PROMPT = "Enter your name: "
DEFAULT_NAME = "anonymous"


def format_greeting(name: str) -> str:
    name = (name or "").strip() or DEFAULT_NAME
    return f"Hello appsec world from @{name}"


def read_name() -> str:
    try:
        return input(PROMPT)
    except (EOFError, KeyboardInterrupt):
        return ""


def main() -> None:
    print(format_greeting(read_name()))


if __name__ == "__main__":
    main()
