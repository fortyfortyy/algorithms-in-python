"""
Function that takes in a given string of available characters and a string representing a document that need to be
generated. Function returns true if can generate the document using the available characters, otherwise, it returns false.

The document may contain any characters, including special characters, capital letters, numbers and spaces.

Sample Input                                          |  Sample Output
characters = "agig tepo rrleP xnlkldan nkiaewa!"     |     "True"
document = "People are walking and talking!"          |
"""

# O(n + m) time | O(c) space - where n is the number of characters, m is the length of the document and c is the number
# of unique characters in the characters string
def generate_document(characters, document):
    available_characters = {}

    for character in characters:
        if character not in available_characters:
            available_characters[character] = 0

        available_characters[character] += 1

    for character in document:
        if character not in available_characters or available_characters[character] == 0:
            return False
        available_characters[character] -= 1

    return True

characters = "agig tepo rrleP xnlkldan nkiaewa!"
document = "People are walking and talking!"
print(generate_document(characters, document))