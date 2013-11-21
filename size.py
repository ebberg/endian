#!/usr/bin/env python3
import creature as c

class Size(c.Creature):
    def speed(self):
        return 0
    def speed_desc(self):
        return "%s feet per round" % self.speed()

class Medium(Size):
    def speed(self):
        return 30

class Small(Size):
    def speed(self):
        return 20
    def ac(self):
        return super().ac() + 1
