from Ciphers.Cipher import Cipher


class CaesarCipher(Cipher):
    def __init__(self, shift):
        self.shift = shift

    english_frequences = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
                          0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                          0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                          0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def shiftedForwardText(self, text):
        result = str()
        for symbol in text:
            if symbol.isalpha():
                if symbol.isupper():
                    result += chr((ord(symbol) + int(self.shift) - 65) % 26 + 65)
                else:
                    result += chr((ord(symbol) + int(self.shift) - 97) % 26 + 97)
            else:
                result += symbol
        return result

    def shiftedBackwardText(self, text):
        decoded = ''
        for symbol in text:
            if symbol.isalpha:
                num = self.alphabet.find(symbol)
                num = num - int(self.shift)
                if num < 0:
                    num = num + 26
                decoded = decoded + self.alphabet[num]
            else:
                decoded = decoded + symbol
        return decoded

    def decode(self, text):
        return self.shiftedBackwardText(text)

    def encode(self, text):
        return self.shiftedForwardText(text)

    @classmethod
    def getFrequencys(cls, text):
        dict = {}
        for alpha in cls.alphabet:
            dict[alpha.lower()] = 0
        for alpha in text:
            if alpha.isalpha():
                dict[alpha.lower()] += 1
        for value in dict.values():
            value /= len(text)
        return dict

    @classmethod
    def errorFunction(cls, frequencys):
        sum = 0
        for i in range(len(cls.alphabet)):
            sum += (frequencys[cls.alphabet[i]] - cls.english_frequences[i]) ** 2
        sum /= len(cls.alphabet)
        return sum ** 0.5

    def hack(self, text):
        best_shift = 0
        shifted_text = self.shiftedForwardText(0, text)
        frequencys = self.getFrequencys(shifted_text)
        bestError = self.errorFunction(frequencys)
        for shift in range(-26, 26):
            shifted_text = self.shiftedForwardText(shift, text)
            frequencys = self.getFrequencys(shifted_text)
            error = self.errorFunction(frequencys)
            if bestError > error:
                bestError = error
                best_shift = shift
        return self.shiftedForwardText(best_shift, text)
