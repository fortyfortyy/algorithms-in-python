"""
Function that takes in a non-empty string and returns its run-length encoding.
From Wikipedia, "run-length encoding is a form of lossless data compression in which runs of data are stored as a single
data value and count, rather than as the original run." For this problem, a run of data is any sequence of
consecutive, identical characters. So the run "AAA" would be run-length-encoded as "3A".

Strings can contain all sorts of special characters, including numbers and the encoded data must be decodable
(means that can't be naively run-length-encode long runs).

Sample Input:                            |       Sample Output
string = 'AAAAAAAAAAAAABBCCCCDDaba'      |       "9A4A2B4C2D1a1b1a"
"""


# O(n) time | O(n) space - where n is the length of the input string
def run_length_encoding(string):
    encoded_string_characters = []
    current_run_length = 1

    for i in range(1, len(string)):
        current_character = string[i]
        previous_character = string[i - 1]

        if current_character != previous_character or current_run_length == 9:
            encoded_string_characters.append(str(current_run_length))
            encoded_string_characters.append(str(previous_character))
            current_run_length = 0

        current_run_length += 1

    # Handle the last run
    encoded_string_characters.append(str(current_run_length))
    encoded_string_characters.append(string[len(string) - 1])

    return "".join(encoded_string_characters)


print(run_length_encoding('AAAAAAAAAAAAABBCCCCDDaba'))