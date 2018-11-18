import nltk
from nltk.corpus import brown

class TriGram:
    def __init__(self):
        self.tri_map = {}
        self.tri = ""
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        print("About to ingest brown corpus")
        for w in brown.words():
            self.ingest(w)
    def ingest(self, w):
        for l in w.lower():
            if not l in self.letters:
                continue
            self.tri = self.tri + l
            self.tri = self.tri[-3:]
            if len(self.tri) > 2:
                self.tri_map[self.tri] = self.tri_map.get(self.tri, 0) + 1
    def lookup(self, tri):
        return self.tri_map.get(tri,0)
    def freqs(self, in_str, prior=0.1):
        s = ''.join([l for l in in_str.lower() if l in self.letters])
        n = len(s) - 2
        tris = [s[i:][:3] for i in range(n)]
        return [self.tri_map.get(tri, 0) + prior for tri in tris]
    
