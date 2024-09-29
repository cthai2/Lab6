import base64


# ++++++++++++++++++++function: decrypts using morse code+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def morse_code_decrypt(encrypted_string):
    # This dictionary consists the morse code character as the key and it's character equivalent as value
    morse_code_dictionary = \
        {
            '..-':    'U', '--..--': ', ', '....-': '4', '.....': '5',
            '-...':   'B', '-..-': 'X', '.-.': 'R', '--.-': 'Q',
            '--..':   'Z', '.--': 'W', '-..-.': '/', '..---': '2',
            '.-':     'A', '..': 'I', '-.-.': 'C', '..-.': 'F',
            '---':    'O', '-.--': 'Y', '-': 'T', '.': 'E',
            '.-..':   'L', '...': 'S', '-.--.-': ')',
            '..--..': '?', '.----': '1', '-----': '0',
            '-.-':    'K', '-..': 'D', '----.': '9',
            '-....':  '6', '.---': 'J', '.--.': 'P',
            '.-.-.-': '.', '-.--.': '(', '--': 'M',
            '-.':     'N', '....': 'H', '---..': '8',
            '...-':   'V', '--...': '7',
            '--.':    'G', '...--': '3', '-....-': '-'
        }

    # stores the decrypted morse code words
    decrypted_string = []
    # Iterating over the morse code by splitting it using / as the separator
    for word in encrypted_string.split('/'):
        # stores the decrypted word
        decrypted_word = ''
        # Iterating over word by splitting it using space as the separator
        for char in word.split():
            # Getting the character of morse code equivalent from the dictionary and adding it to decrypted_word string
            decrypted_word += morse_code_dictionary[char]
        # Adding the string to the decrypted_string list
        decrypted_string.append(decrypted_word)
        # Joining the list using space as separator and returning it
        return ' '.join(decrypted_string)


# ++++++++++++++++++++function: decrypts using encoded base64+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def base64_decrypt(encrypted_string):
    # Decoding the base64 text
    decrypted_string = str(base64.urlsafe_b64decode(encrypted_string.encode("utf-8")))
    return decrypted_string


# ++++++++++++++++++++function: decrypts using casear cipher+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def caesar_cipher(encrypted_string, shift):
    decrypted_string = []  # stores the decrypted text
    # Iterating over encrypted_string
    for word in encrypted_string.upper().split():
        # This string stores the decrypted string
        decrypted_word = ""
        # Iterating over words
        for char in word:
            if char.isalpha():
                # Decrypting the character
                decrypted_char = chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_char = char
            # Adding the decrypted character to the decrypted string
            decrypted_word += decrypted_char
        # Adding the decrypted word to the decrypted string
        decrypted_string.append(decrypted_word)
    return ' '.join(decrypted_string)


# +++++++++++++++++++++++++++++++++++++++++++++Main function++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def main():
    # This string stores the morse code text
    morse_code_encrypted_string = "- .... .. ... / ... -.. . ...- / ...-- ----- ----- / -.-. .-.. .- ... ... / .... " \
                                  ".- ... / ... --- -- . / ... - .-. .- -. --. . / .-. . --.- ..- . ... - ... .-.-.- "
    morse_code_decrypted_string = morse_code_decrypt(morse_code_encrypted_string)  # Decrypt the morse code and store

    print("Original Morse code: {}".format(morse_code_encrypted_string))  # Printing the morse code
    print("Message after decrypting morse code: {}".format(morse_code_decrypted_string))  # Prints the decrypted text

    base64_encrypted_string = "U28gdGhpcyBpcyBiYXNlNjQuIE5vdyBJIGtub3cu"  # base64 encoded message
    base64_decrypted_string = base64_decrypt(base64_encrypted_string)  # Decrypt the morse code and store

    print("\nBase 64 encrypted text: {}".format(base64_encrypted_string))  # Prints the encrypted text
    print("Base 64 decrypted text: {}".format(base64_decrypted_string))  # Prints the decrypted text

    # Caesar cipher encoded message
    caesar_cipher_encrypted_string = "--- Psuwb Ysm ---- W oa gc qzsjsf. Bc cbs qcizr dcggwpzm twuifs hvwg cih. --- " \
                                     "Sbr Ysm --- "
    caesar_cipher_decrypted_string = caesar_cipher(caesar_cipher_encrypted_string, 14)  # Decrypting the caesar
    # cipher text

    print("\nBase 64 encrypted text: {}".format(caesar_cipher_encrypted_string))  # Prints the encrypted text
    print("Base 64 decrypted text: {}".format(caesar_cipher_decrypted_string))  # Prints the decrypted text


main()
