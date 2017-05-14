from random import random


class DilemmaValues:

    cooperation = True
    defence = False

    def __init__(self, c, d, C, D):

        self.c = c
        self.d = d
        self.C = C
        self.D = D

    def get_random_value(self):

        return self.cooperation if random() <= 0.5 else self.defence

    def compare(self, a, b):

        if a == b:
            return (self.C, self.C) if a is self.cooperation else (self.d, self.d)
        else:
            return (self.c, self.D) if a is self.cooperation else (self.D, self.c)
