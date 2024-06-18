# The official mapping files

This directory contains the official mapping files (or definition files) for the Adobe
character encodings, including Standard, Standard+, ISOLatin1, ISOLatin1+, and ISO-8859-*x*
(where *x* is in the range 1-11 or 13-16), and the Adobe Symbol and ZapfDingbats character
sets.

## The `PSL_*.h` files

The `PSL_*.h` files are definition files for different Adobe character encodings, obtained
from the GMT source code repository (https://github.com/GenericMappingTools/gmt). They
are C header files that contains 256 elements of Adobe Glyph names.

The `glyphlist.txt` file is the official Adobe glyph list file that maps Adobe glyph
names to Unicode values. The file is obtained from https://github.com/adobe-type-tools/agl-aglfn.

## The Adobe Symbol and ZapfDingbats character set

The mapping tables of Adobe Symbols, and ZapfDingbats fonts are obtained
from the official Unicode website (https://www.unicode.org/Public/MAPPINGS/VENDORS/ADOBE/).

The mapping tables have four tab-separated columns:

1. The Unicode value (in hexadecimal)
2. The Adobe Encoding code point (in hexadecimal)
3. The Unicode name
4. The Adobe Postscript character name

Likely due to historical reasons, some Adobe Postscript characters are marked as "CUS"
(Corporate Use Subarea) in the Postscript character name column. These characters are
mapped to Unicode values in the [Private Use Area (PUA) block](https://www.compart.com/en/unicode/block/U+E000)
(with Unicode values from `E0000` to `F8FF`), which are not assigned to any characters
by the Unicode Consortium. So we need to fix these mappings manually.

### Adobe Symbol Mapping Table

- Both Unicode values `0020` (space) and `00A0` (no-break space) are mapped to Symbol
  code point `20`. We can only keep one and `0020` makes more sense, so comment out `00A0`.
- 22 Unicode values (`F8E6`, `F8E7`, `F8EB`-`F8FE`) are replaced with standard Unicode
  values (`239B`-`23AF` and `23D0`). Reference: https://www.unicode.org/charts/PDF/U2300.pdf.
- The trademark, registered, and copyright characters are encoded twice: one version has
  serifs and the other is sans-serif, but Unicode only has one version. They're mapped to
  `2122`, `00AE`, and `00A9`, respectively.
- `F8E5` (RADICAL EXTENDER) is the only character that is not updated. See
  https://unicode.org/mail-arch/unicode-ml/y2003-m07/0542.html.

### Adobe ZapfDingbats Mapping Table

- Similar to the Symbol mapping table, `00A0` is commented out.
- 14 Unicode values (`F8D7`-`F8E4`) are replaced with standard Unicode values (`2768`-`2775`).
  Reference: https://www.compart.com/en/unicode/block/U+2700

## The conversion scripts

The mapping files are obtained from two different sources (one from the Unicode website
and one from the GMT source code) and have different formats. Two scripts are provided
to convert the mapping files into the same format.

The script `convert_font_encoding.py` can convert the Adobe Symbol and ZapfDingbats
character set, and `convert_iso_encoding.py` can convert the C header files of Adobe
character encodings.

The converted mapping files are in the same format and are stored in the root directory.
