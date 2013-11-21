import language as lang
import size


class Race(lang.Common):
    def literacy(self):
        return True

class Elf(lang.Elvish):
    pass

class Dwarf(lang.Dwarven):
    pass

class Gnome(lang.Gnemic):
    pass

class HalfElf(lang.Elvish):
    pass

class HalfOrc(lang.Orcish):
    pass

class Human():
    pass

class Halfling(size.Small):
    pass
