from unittest import TestCase

from challenges import Ceaser_Cipher


expected_words = ["hello", "world", "computer", "science"]
offset = [1, 2, 3, 4]
encrypted = [['i', 'f', 'm', 'm', 'p'], ['y', 'q', 't', 'n', 'f'], ['f', 'r', 'p', 's', 'x', 'w', 'h', 'u'], ['w', 'g', 'm', 'i', 'r', 'g', 'i']]

def test_cypher_encyrpt():
    for i in range (len(encrypted)):
        yield check_cypher_decrypt, encrypted[i],offset[i],expected_words[i]


def check_cypher_decrypt(input, offset, expected_out):
    output = Ceaser_Cipher.decrypt(input,offset)
    if type(output) != str:
        output = ''.join(map(str, output))
    assert output == expected_out, '{} != {}'.format(expected_out, output)
