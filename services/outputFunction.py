def output(text, outputFile):
    if outputFile is None:
        print(text)
    else:
        outputFile.write(text)
        outputFile.close()
str = "aboba"