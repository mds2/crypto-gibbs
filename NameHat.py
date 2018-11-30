# Quick little silly utility that prints out a bunch of plausible-sounding
# "fantasy names"

from CryptoGibbs import *
import random

def make_name(len_range=(6,10)):
    n = random.randrange(len_range[0], len_range[1])
    letters = 'abcdefghijklmnopqrstuvwxyz'
    l = [letters[random.randrange(26)] for i in range(n)]
    w = " " + "".join(l) + " "
    c = CryptoGibbs(w)
    c.jump_for(10000)
    return c.c.unscramble(c.s)

if __name__ == "__main__":
    print("Calculating names")
    names = [make_name((7,12)) for i in range(20)]
    print("printing the names")
    [print(n) for n in names]

