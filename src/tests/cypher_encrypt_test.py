from unittest import TestCase

from challenges import Ceaser_Cipher


words = ["hello", "world", "computer", "science"]
offset = [1, 2, 3, 4]
expected_encrypted = ["ifmmp", "yqtnf", "frpsxwhu", "wgmirgi"]

def test_cypher_encyrpt():
    for i in range (len(words)):
        yield check_cypher_encrypt, words[i],offset[i],expected_encrypted[i]


def check_cypher_encrypt(input, offset, expected_out):
    output = Ceaser_Cipher.encyrpt(input,offset)
    if type(output) != str:
        output = ''.join(map(str, output))
    assert output == expected_out, '{} != {}'.format(expected_out, output)
