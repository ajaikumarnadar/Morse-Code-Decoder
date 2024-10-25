import sys

# Morse code dictionary
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!',
    '-....-': '-', '.-..-.': '"', '---...': ':', '-.-.-.': ';', '-.--.': '(',
    '-.--.-': ')', '.----.': "'", '.-.-.': '+', '-..-.': '/', '.--.-.': '@'
}

def morse_to_text(morse_code):
    """Convert Morse code to ASCII text."""
    words = morse_code.split(' / ')
    decoded_words = []

    for word in words:
        characters = word.split()
        decoded_word = ''.join(MORSE_CODE_DICT.get(char, '') for char in characters)
        decoded_words.append(decoded_word)

    return ' '.join(decoded_words)

def decode_morse_file(input_file, output_file="ascii_output.txt"):
    """Read Morse code from input file, decode it, and write to output file."""
    try:
        with open(input_file, 'r') as infile:
            morse_code = infile.read()

        decoded_text = morse_to_text(morse_code)

        with open(output_file, 'w') as outfile:
            outfile.write(decoded_text)

        print("Decoded text has been written to file.")
    except FileNotFoundError:
        print("Error: The file does not exist.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python morse_decoder.py <input_file>")
    else:
        input_file = sys.argv[1]
        decode_morse_file(input_file)
