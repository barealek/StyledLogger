class PrintType:
    display = "UNKN"

    def __hash__(self):
        return hash(self.display)

    def __eq__(self, other):
        return self.display == other.display


class Debug(PrintType):
    display = "DEBU"
    level = 0


class Info(PrintType):
    display = "INFO"
    level = 1


class Warn(PrintType):
    display = "WARN"
    level = 2


class Error(PrintType):
    display = "ERRO"
    level = 3


class Fatal(PrintType):
    display = "FATL"
    level = 4


class System(PrintType):
    display = "SYST"
    level = 5
