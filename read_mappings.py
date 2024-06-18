#!/usr/bin/env python
"""
Read mapping tables and output in different formats that can be used in PyGMT.
"""

import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class UnicodeChar:
    hex: str  # The Unicode value in hexadecimal (e.g., `0x220b`).
    name: str  # The Unicode name (e.g., "CONTAINS AS MEMBER").
    char: str  # The Unicode character (e.g., `'∋'`).
    ncr: str  # Numeric character reference in markup languages (e.g., `&#x220b;`).
    unicode: str  # The Unicode representation (e.g., '\u220b')


# Undefined octal codes are mapped to the REPLACEMENT CHARACTER.
UNDEFINED = UnicodeChar(
    hex="0xfffd",
    name="REPLACEMENT CHARACTER",
    char="�",
    ncr="&#xFFFD;",
    unicode="\\ufffd",
)

if len(sys.argv) != 2:
    sys.exit(f"Usage: python {sys.argv[0]} charset.txt")

charset = Path(sys.argv[1])

match charset.name:
    case "symbol.txt" | "zdingbat.txt":
        octranges = [*range(0o040, 0o200), *range(0o240, 0o400)]
    case _:
        octranges = range(0o030, 0o400)

mappings = {}
with charset.open("r") as fp:
    for line in fp:
        if line.startswith("#"):
            continue
        encoding_oct, unicode_hex, unicode_name = line.strip().split(",")
        unicode_hex = unicode_hex.lower()
        mappings[encoding_oct] = UnicodeChar(
            hex=f"0x{unicode_hex}",
            name=unicode_name,
            char=f"{int(unicode_hex, 16):c}",
            ncr=f"&#x{unicode_hex};",
            unicode=f"\\u{unicode_hex}",
        )

# List of 256 unicodes. Some are undefined.
unicode_list = [mappings.get(f"{i:03o}", UNDEFINED) for i in range(0o000, 0o400)]

# Generate the string of all characters, 8 per line.
string = ""
for i in range(0o000, 0o400, 8):
    string += '"' + "".join(char.unicode for char in unicode_list[i : i + 8]) + '"\n'
print(string + "\n")

# Generate Markdown Table
markdown = "| octal | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n"
markdown += "|---|---|---|---|---|---|---|---|---|\n"
for i in range(0o000, 0o400, 8):
    chars = unicode_list[i : i + 8]
    if chars == [UNDEFINED] * 8:  # All characters in this row are undefined. Skip.
        continue
    row = f"\\{i:03o}"[:-1] + "x"
    markdown += f"| {row} |  {' | '.join(char.ncr for char in chars)} |\n"
print(markdown)

# Generate Markdown Table
markdown = "| Octal Code | Character | Unicode | HTML entity | Unicode Name |\n"
markdown += "|---|---|---|---|---|\n"
for i in range(0o000, 0o400):
    encoding_oct = f"{i:03o}"
    char = unicode_list[i]

    if char == UNDEFINED:  # Skip undefined characters
        continue
    elif char.char == "|":  # Change | to \| to avoid Markdown table formatting issue
        charstr = "\\|"
    else:
        charstr = char.char
    markdown += (
        f"| {encoding_oct} | {charstr} | {char.hex} | {char.ncr} | {char.name} |\n"
    )
print(markdown)
