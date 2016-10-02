# unitconvert
Unit Conversion Tool

This project is to design a helpful tool to convert compatible units.
It is designed to be simple and easy to use in scripts.

## Usage
```unitconvert -i INPUT_UNIT -o OUTPUT_UNIT VALUE_TO_CONVERT```

For example:

    $ unitconvert -i fahrenheit -o celsius
    37.7777777778

Note: the precision currently uses python's default for printing floats, but that should be controlled by an argument eventually.

## Requirements:
Python 2
