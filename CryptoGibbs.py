from Cipher import *
from TriGram import *
from math import log, exp
import random


class CryptoGibbs:
    def __init__(self, encoded_str):
        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.c = Cipher(self.letters)
        self.best = self.c
        self.s = encoded_str
        print("About to build trigram map")
        self.t = TriGram()
        print("built trigram map")
        self.prior = 1
        self.p = self.get_prob_log(self.c)
        self.best_p = self.p
        print("Initial perm prob log is " + str(self.p))
    def get_prob_log(self, cipher):
        s = cipher.unscramble(self.s)
        fs = self.t.freqs(s, self.prior)
        return sum([log(f) for f in fs])
    def jump_for(self, iters):
        def rand_log():
            x = random.random()
            while x <= 0.0:
                x = random.random()
            return log(x)
        for i in range(iters):
            r1 = rand_log()
            r2 = rand_log()
            candidate = self.c.rand_mutation()
            pc = self.get_prob_log(candidate)
            if (r1 + pc > r2 + self.p):
                self.c = candidate
                self.p = pc
            if (pc > self.best_p):
                self.best_p = pc
                self.best = candidate
        print("Current guess is " + self.c.unscramble(self.s))
        print("Best guess was " + self.best.unscramble(self.s))
