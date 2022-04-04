class CaesarCipher:
    english_frequences = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
                          0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                          0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                          0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    @classmethod
    def shiftedForwardText(cls, shift, text):
        result = str()
        for symbol in text:
            if (symbol.isupper()):
                result += chr((ord(symbol) + shift - 65) % 26 + 65)
                # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(symbol) + shift - 97) % 26 + 97)
        return result

    @classmethod
    def shiftedBackardText(cls, shift, text):
        for key in range(len(LETTERS)):
            translated = ''
            for symbol in message:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                else:
                    translated = translated + symbol
        print('Hacking key #%s: %s' % (key, translated))

    @classmethod
    def decode(cls, arguments):
        return CaesarCipher.shiftedBackardText(arguments['key'], arguments['input_text'])

    @classmethod
    def encode(cls, arguments):
        return CaesarCipher.shiftedForwardText(arguments['key'], arguments['input_text'])

    @classmethod
    def getFrequencys(cls, text):
        dict = {}
        for alpha in cls.alphabet:
            dict[alpha.lower()] = 0
        for alpha in text:
            dict[alpha.lower] += 1
        for value in dict:
            value /= len(text)
        return dict
    @classmethod
    def errorFunction(cls, frequencys):
        sum = 0
        for alpha in cls.alphabet:
            sum += (frequencys[alpha] - cls.english_frequences[alpha])**2
        sum /= len(cls.alphabet)
        return sum**0.5
    @classmethod
    def hack(cls, arguments):
        best_shift = 0
        shifted_text = cls.shiftedForwardText(0,arguments["input_text"])
        frequencys = cls.getFrequencys(shifted_text)
        bestError = cls.errorFunction(frequencys)
        for shift in range(-30,30):
            shifted_text = cls.shiftedForwardText(shift, arguments["input_text"])
            frequencys = cls.getFrequencys(shifted_text)
            error = cls.errorFunction(frequencys)
            if bestError > error:
                bestError = error
                best_shift = shift
        return cls.shiftedForwardText(best_shift,arguments['input_text'])