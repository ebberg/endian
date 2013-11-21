#!/usr/bin/env python3

class Alignment():
    def alignment(self):
        return ""

    def good_vs_evil(self):
        alignment = self.alignment()
        if type(alignment) != str:
            raise TypeError("alignment must be a string")
        try:
            _, morals = alignment.split()
        except ValueError:
            morals = alignment.split()[0]
        finally:
            return morals

    def law_vs_chaos(self):
        alignment = self.alignment()
        if type(alignment) != str:
            raise TypeError("alignment must be a string")
        try:
            balance, _ = alignment.split()
        except ValueError:
            balance = alignment.split()[0]
        finally:
            return balance 

class Neutral(Alignment):
    def alignment(self):
        return "Neutral"

class NeutralGood(Alignment):
    def alignment(self):
        return "Neutral Good"
