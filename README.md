# unitconvert
Unit Conversion Tool

This project is to design a helpful tool to convert compatible units.
It is designed to be simple and easy to use in scripts.

## Usage
```unitconvert -i INPUT_UNIT -o OUTPUT_UNIT VALUE_TO_CONVERT```

For example:

    $ unitconvert -i fahrenheit -o celsius 45
    7.22222222222

You can use the `-p` flag to set precision:

    $ unitconvert -i fahrenheit -o celsius -p 2 45
    7.22

    $ unitconvert -i fahrenheit -o celsius -p 0 45
    7

## Requirements:
Python 2
