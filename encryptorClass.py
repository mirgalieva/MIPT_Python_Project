import sys
import argparse
from Ciphers.caesarCipher import CaesarCipher
from Ciphers.vernamCipher import VernamCipher
from Ciphers.vigenereCipher import  VigenereCipher

from sys import stdin


class InfoManager:
    """Read and write into files or console"""
    def __init__(self, _in, _out):
        self.input = _in
        self.output = _out
        self.text = []

    def read_text(self):
        """read from input"""
        if self.input is None:
            while True:
                line = stdin.readline()
                if line.strip() == "":
                    break
                line = line.replace('\n', '')
                self.text.append(line)
        else:
            with open(self.input, "r") as file:
                self.text = [line.replace('\n', '') for line in file.readlines()]
                file.close()

    def write_text(self):
        """write in output"""
        if self.output is None:
            for line in self.text:
                print(line)
        else:
            with open(self.output, "w") as file:
                for line in self.text:
                    file.write(line + "\n")
                file.close()




class Parser:
    parser = argparse.ArgumentParser()

    def __init__(self):
        self.modulename = sys.argv[1:]
        self.parser.add_argument('module')
        self.parser.add_argument('--cipher', default="caesar")
        self.parser.add_argument('--key', default="1")
        self.parser.add_argument('--input_file', default=None)
        self.parser.add_argument('--output_file', default=None)

    def get_arguments(self):
        args = vars(self.parser.parse_args())
        args['input_text'] = input() if args['input_file'] is None else args['input_file'].read()
        return args


if __name__ == "__main__":
    parser = Parser()
    namespace = parser.parser.parse_args()
    manager = InfoManager(namespace.input_file, namespace.output_file)
    manager.read_text()
    if namespace.cipher == "caesar":
        text_ = CaesarCipher(namespace.key)
    elif namespace.cipher == "vigenere":
        text_ = VigenereCipher(namespace.key)
    elif namespace.cipher == "vernam":
        text_ = VernamCipher(namespace.key)
    if namespace.module == "encode":
        manager.text = [text_.encode(line) for line in manager.text]
    elif namespace.module == "decode":
        manager.text = [text_.decode(line) for line in manager.text]
    elif namespace.module == "hack":
        manager.text = [text_.hack(line) for line in manager.text]

    manager.write_text()