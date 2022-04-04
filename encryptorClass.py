from services.commandLineArgumentsParser import Parser
from Ciphers.caesarCipher import CaesarCipher
from Ciphers.vigenereCipher import VigenereCipher
from Ciphers.vernamCipher import VernamCipher
from services.outputFunction import output


class Encryption:
    ciphersDict = {'caesar': CaesarCipher, 'vigenere': VigenereCipher, 'vernam': VernamCipher}

    def __init__(self):
        arguments = Parser().getArguments()
        if arguments['module'] == "decode":
            decodedText = self.ciphersDict[arguments['cipher']].decode(arguments)
            output(decodedText, arguments['output_file'])
        if arguments['module'] == "encode":
            encodedText = self.ciphersDict[arguments['cipher']].encode(arguments)
            output(encodedText, arguments['output_file'])
        if arguments['module'] == "hack":
            encodedText = CaesarCipher.hack(arguments)
            output(encodedText, arguments['output_file'])
