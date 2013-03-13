import random
from random import randint

class ErnieDict():
    phrases = {}

    def __init__(self):
        self.phrases[1] = " and junk."
        self.phrases[2] = " or something."
        self.phrases[3] = " I guess."
        self.phrases[4] = " and stuff."
        self.phrases[5] = " well maybe."
        
    def getPhrase(self):
        i = random.randint(1, 5)
        return self.phrases[i]        
