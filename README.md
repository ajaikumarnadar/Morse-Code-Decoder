# Morse Code Decoder

A simple Python tool to decode Morse code into readable ASCII text. This tool reads Morse code from an input file, translates it, and writes the decoded text to an output file.

## Features
- Translates Morse code letters and numbers, as well as common punctuation.
- Saves decoded output in a separate file for easy access.
- Accepts input file as a command-line argument for flexible usage.

## Requirements
- Python 3.x

## Usage

1. **Run the script:**

   `python morse_decoder.py morse_input.txt`

2. **View output:**

   The decoded ASCII text will be saved in ascii_output.txt.

## Example

For an input file with content:

`.... . .-.. .-.. --- / .-- --- .-. .-.. -..`

The `ascii_output.txt` file will contain:

`HELLO WORLD`
