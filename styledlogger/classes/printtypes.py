class PrintType:
    def __init__(self):
        self.display = None

class Debug(PrintType):
    display = "DEBU"

class Info(PrintType):
    display = "INFO"

class Warn(PrintType):
    display = "WARN"

class Error(PrintType):
    display = "ERRO"

class Fatal(PrintType):
    display = "FATL"

class System(PrintType):
    display = "SYST"