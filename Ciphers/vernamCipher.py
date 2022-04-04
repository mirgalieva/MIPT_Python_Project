import string

abc = string.ascii_lowercase
one_time_pad = list(abc)


class VernamCipher:
    @classmethod
    def __init__(self, key='fortification'):
        self.key = [k.upper() for k in key]

    @classmethod
    def encode(self, arguments):
        text = arguments['input_text'].lower
        key = arguments['key'].lower()
        ciphertext = ''
        for idx, char in enumerate(text):
            charIdx = abc.index(char)
            keyIdx = one_time_pad.index(key[idx])
            cipher = (keyIdx + charIdx) % len(one_time_pad)
            ciphertext += abc[cipher]

        return ciphertext

    @classmethod
    def BackwardText(self, text, key):
        if text == '' or key == '':
            return ''
        text = text.lower()
        key = key.lower()
        charIdx = abc.index(text[0])
        keyIdx = one_time_pad.index(key[0])

        cipher = (charIdx - keyIdx) % len(one_time_pad)
        char = abc[cipher]
        return char + self.BackwardText(text[1:], key[1:])

    @classmethod
    def decode(self, arguments):
        return VernamCipher.BackwardText(arguments['input_text'], arguments['key'])
