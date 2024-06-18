#!/usr/bin/env python#
#
# Convert GMT's C header files of ISO encodings to a common format.
#
import sys
import pandas as pd
import unicodedata

if len(sys.argv) != 2:
    sys.exit(f"Usage: python {sys.argv[0]} PSL_xxx.h")

charfile = sys.argv[1]

# Read the Adobe Glyph List as a dictionary
glyph_dict = {}
glyph_dict["notdef"] = "FFFD"  # Unicode replacement character
with open("glyphlist.txt", "r") as f:
    for line in f:
        if line.startswith("#"):
            continue
        glyph_name, unicode_hex = line.strip().split(";")
        glyph_dict[glyph_name] = unicode_hex

# Read the C header files
glyph_names = []
with open(charfile, "r") as fp:
    for line in fp:
        if "[" in line or "]" in line:  # skip first and last line
            continue
        glyph_names.extend(
            [item.lstrip("/.") for item in line.replace("\\n\\\n", "").split()]
        )

for i, glyph_name in enumerate(glyph_names):
    if glyph_name == "notdef":  # Skip if undefined.
        continue

    encoding_oct = f"{i:03o}"
    unicode_hex = glyph_dict[glyph_name]
    unicode_name = unicodedata.name(chr(int(unicode_hex, 16)))
    print(f"{encoding_oct},{unicode_hex},{unicode_name}")
