# Quick little silly utility that prints out a bunch of plausible-sounding
# "fantasy names"

from CryptoGibbs import *
import random

def make_names(words=2, len_range=(6,10)):
    sentence = ""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(words):
        n = random.randrange(len_range[0], len_range[1])
        l = [letters[random.randrange(26)] for i in range(n)]
        sentence = sentence + " " + "".join(l)
    sentence = sentence + " "
    c = CryptoGibbs(sentence)
    c.jump_for(10000)
    return c.c.unscramble(c.s).strip().split(" ")

if __name__ == "__main__":
    from sys import argv
    print("Calculating names")
    names = []
    sentences = 25
    words_per_sentence = 1
    try:
        num_words = int(argv[-1])
        words_per_sentence = num_words
        sentences = int(sentences/num_words)
    except:
        print("Defaulting to " + str(words_per_sentence) +
              " words per sentence and " + str(sentences) +
              " sentences")
    for i in range(sentences):
        names = names + make_names(words=words_per_sentence, len_range=(7,12))
    print("printing the names")
    [print(n) for n in names]

