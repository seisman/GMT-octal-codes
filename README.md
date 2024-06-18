# Mapping Unicode characters to octal codes for GMT and PyGMT

This repository contains mapping tables for converting Unicode characters to octal codes
that can be used in GMT and PyGMT.

The mapping tables are stored as comma-separated values files with the following columns:

1. Octal code
2. Unicode value (in hexadecimal)
3. Unicode name

The `read_mappings.py` script can read the mapping tables in the `mappings` directory
and then output in various formats that can be directly embedded in PyGMT source code
and documentation.

Usage:
```
python read_mappings.py charset.txt
```

Notes:

1.  The original mapping files from different sources are in the `official` directory.
    Check the `official/README.md` file for more information.
2.  Some octal codes are not assigned to any characters. Here the special Unicode character
    `�` (`U+FFFD`, REPLACEMENT CHARACTER) is assigned.
