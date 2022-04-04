class VigenereCipher:
    @classmethod
    def CharToInt(self, ch):
        ch = ch.upper()
        arr = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
               'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
               'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
        return arr[ch]
    @classmethod
    def IntToChar(self, i):
        i = i % 26
        arr = (
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V',
            'W', 'X', 'Y', 'Z')
        return arr[i]

    @classmethod
    def __init__(self, key='fortification'):
        self.key = [k.upper() for k in key]

    @classmethod
    def encode(self, arguments):
        text = arguments['input_text']
        key = arguments['key']
        ret = ''
        for (i, c) in enumerate(text):
            i %= len(key)
            ret += self.IntToChar(self.CharToInt(c) + self.CharToInt(key[i]))
        return ret

    @classmethod
    def decode(self, arguments):
        text = arguments['input_text']
        key = arguments['key']
        ret = ''
        for (i, c) in enumerate(text):
            i %= len(key)
            ret += self.IntToChar(self.CharToInt(c) - self.CharToInt(key[i]))
        return ret
