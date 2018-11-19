from random import randrange
import random

def permute(in_str):
    a = [l for l in in_str.rstrip()]
    n = len(a)
    for i in range(n):
        idx = randrange(i, n)
        tmp = a[i]
        a[i] = a[idx]
        a[idx] = tmp
    return "".join(a) + in_str[n:]

class Cipher:
    def __init__(self, perm=None):
        self.letters = 'abcdefghijklmnopqrstuvwxyz '
        if perm:
            self.perm = perm
        else:
            self.perm = permute(self.letters)
        self.f_map = {} # forward map
        self.r_map = {} # reverse map
        for i in range(27):
            self.f_map[self.letters[i]] = self.perm[i]
            self.r_map[self.perm[i]] = self.letters[i]
    def scramble(self, in_str):
        s = [l for l in in_str.lower() if l in self.letters]
        return "".join([self.f_map[l] for l in s])
    def unscramble(self, in_str):
        s = [l for l in in_str.lower() if l in self.letters]
        return "".join([self.r_map[l] for l in s])
    def mutate(self, cycle):
        p = {}
        for i in range(len(cycle)):
            p[cycle[i-1]] = cycle[i]
        nextperm = "".join([p.get(l, l) for l in self.perm])
        return Cipher(nextperm)
    def rand_mutation(self):
        c = permute(self.letters)[:2]
        return self.mutate(c)
    
        
    
        
