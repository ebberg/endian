#!/usr/bin/env python3

class Profession():
    pass

class Bard(Profession):
    def __init__(self, level):
        if super().law_vs_chaos() == 'Lawful':
            raise TypeError("Bards cannot be Lawful")
        self.level = level
