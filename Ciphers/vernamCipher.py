import string
from Ciphers.Cipher import Cipher

abc = string.ascii_lowercase
one_time_pad = list(abc)


class VernamCipher(Cipher):
    shift: string

    def __init__(self, shift='fortification'):
        self.shift = shift

    def encode(self, text):
        text = text.lower()
        key = self.shift.lower()*len(text)
        ciphertext = ''
        for idx, char in enumerate(text):
            charIdx = abc.index(char)
            keyIdx = one_time_pad.index(key[idx])
            cipher = (keyIdx + charIdx) % len(one_time_pad)
            ciphertext += abc[cipher]
        return ciphertext


    def BackwardText(self, text, shift):
        if text == '' or self.shift == '':
            return ''
        text = text.lower()
        key = self.shift.lower()
        charIdx = abc.index(text[0])
        keyIdx = one_time_pad.index(key[0])
        cipher = (charIdx - keyIdx) % len(one_time_pad)
        char = abc[cipher]
        return char + self.BackwardText(text[1:], shift[1:])


    def decode(self, text):
        return self.BackwardText(text, self.shift)


    def hack(self, arguments) -> None:
        pass


