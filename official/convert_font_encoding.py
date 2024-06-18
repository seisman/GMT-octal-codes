#!/usr/bin/env python
#
# Convert the Adobe Symbol/ZapfDingbats mapping files into a common format.
#
import sys

if len(sys.argv) != 2:
    sys.exit(
        f"Usage: python {sys.argv[0]} charset.txt > ../charset.txt\n\n"
        "   charset.txt can be either symbol.txt or zdingbat.txt\n"
    )

charfile = sys.argv[1]
with open(charfile, "r") as f:
    for line in f:
        if line.startswith("#"):
            continue
        unicode_hex, encoding_hex, unicode_name, glyph_name = line.strip().split("\t")
        encoding_oct = f"{int(encoding_hex, 16):03o}"
        unicode_name = unicode_name.lstrip("# ")
        print(f"{encoding_oct},{unicode_hex},{unicode_name}")
