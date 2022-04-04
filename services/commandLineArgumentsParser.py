import argparse
import sys


class Parser:
    parser = argparse.ArgumentParser()

    def __init__(self):
        self.modulename = sys.argv[1]
        self.parser.add_argument('module')
        self.parser.add_argument('--cipher', choices=['caesar', 'vigenere', 'vernam'])
        self.parser.add_argument('--key',type = int)
        self.parser.add_argument('--input-file', type=argparse.FileType(mode='r'))
        self.parser.add_argument('--output-file', type=argparse.FileType(mode='w'))
    def getArguments(self):
        args = vars(self.parser.parse_args())
        args['input_text'] = input() if args['input_file'] is None else args['input_file'].read()
        return args
