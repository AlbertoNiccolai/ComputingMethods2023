#write the license here

import argparse
import time #use time.time()

import matplotlib.pyplot as plt
import numpy as np
import pandas
from loguru import logger

#then import my stuff

Parser = argparse.ArgumentParser(prog = 'WordsCounter', description = 'It counts the relative frequency of each letter and can provide an histogram of this occurrences. It only works with plain text files.')

Parser.add_argument('infile', help ='Insert the path to the book downloaded.')
Parser.add_argument('--plot', action = 'store_true', help = 'if you write --plot the argument takes a "True" value, otherwise it will be still on "False". If this value is "True", an histogram of the occurrences will be shown.')

#any argument that starts with -- is optional, otherwise it's mandatory.

Alphabet= {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

Occurrence = []
Label = list(Alphabet)


def ProcessFile(FilePath, InputHist):
    """
    This function opens the text through the input of the path (FilePath) and counts the occurrences of each
    letter of the alphabet in the text.

    There is also an optional argument (InputHist) which tells the machine to show an histogram of the
    occurrences through the command --plot.
    """
    StartTime = time.time()
    logger.info(f'Opening input file {FilePath}...')
    Data = open(FilePath).read()
    Data = Data.lower()
    Spaces = Data.count(" ")
    Punctuation = Data.count('?') + Data.count("!") + Data.count('.') + Data.count(',') + Data.count("'")
    Spaces = Spaces + Punctuation


    #A cicle to count the frequence of each letter
    for x in Alphabet:
        Ct = Data.count(x)
        Occurrence.append(Ct)
        Alphabet[str(x)] = Alphabet[str(x)] + Ct
        RelativeFrequency = (Alphabet[str(x)]/(len(Data) - Spaces) * 100 )
        logger.info(f" {x} = %.2f" % RelativeFrequency)

    #Calculate the elapsed time and show it on the terminal
    EndTime = time.time()
    ElapsedTime = EndTime - StartTime
    logger.info(f'Done, {len(Data) - Spaces}')
    logger.info(f'Elapsed time: %.3f s' % ElapsedTime)

    #"if" condition to optionally show the histogram of occurrences
    if InputHist == True:
        logger.info(f'Showing an histogram of relative frequency of each letter...')
        RelativeOccurrence = np.array(Occurrence) /(len(Data) - Spaces) * 100
        plt.bar(Label, RelativeOccurrence)
        plt.ylabel('Relative Frequency (%)')
        plt.show()

#this is always at the bottom

if __name__ == '__main__':
    """
    This actually tells the code to be used only if executed, not imported.
    If I remove this, i cannot import it as a module. Every module, when loaded in memory has
    a "__name__" that does the magic.
    Never leave a floating code in the module, otherwise it will be executed when you don't want.
    """
    args = Parser.parse_args()
    print(args)
    ProcessFile(args.infile, args.plot)


#nota: la funzione len() su una stringa legge pure gli spazi
