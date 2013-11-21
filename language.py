#!/usr/bin/env python3

class Language():
    def languages(self):
        return []

class Common(Language):
    def languages(self):
        return super().languages() + ['Common']

class Dwarven(Language):
    def languages(self):
        return super().languages() + ['Dwarven']

class Elvish(Language):
    def languages(self):
        return super().languages() + ['Elvish']

class Gnemic(Language):
    def languages(self):
        return super().languages() + ['Gnemic']

class Gobbeldygook(Language):
    def languages(self):
        return super().languages() + ['Gobbeldygook']

class Orcish(Language):
    def languages(self):
        return super().languages() + ['Orcish']

class Infernal(Language):
    def languages(self):
        return super().languages() + ['Infernal']

class Abyssal(Language):
    def languages(self):
        return super().languages() + ['Abyssal']

class Draconic(Language):
    def languages(self):
        return super().languages() + ['Draconic']

class Sylvan(Language):
    def languages(self):
        return super().languages() + ['Sylvan']

class Celestial(Language):
    def languages(self):
        return super().languages() + ['Celestial']
