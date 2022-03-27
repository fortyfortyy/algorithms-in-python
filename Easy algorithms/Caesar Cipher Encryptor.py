"""
Function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet,
where k is the key.

Sample Input           |        Sample Output
string = 'xyz'         |             "zab"
"""

# O(n) time | O(n) space - where n is the length of the input string
def caesar_cipher_encryptor(string, key):
    new_letters = []
    new_key = key % 26

    for letter in string:
        new_letters.append(get_new_letter(letter, new_key))

    return "".join(new_letters)


def get_new_letter(letter, key):
    new_letter_code = ord(letter) + key
    return chr(new_letter_code) if new_letter_code <= 122 else chr(96 + new_letter_code % 122)


print(caesar_cipher_encryptor('xyz', 2))