# IntToken -- Token object for representing integer constants

from Tokens import TokenType
from Tokens import Token

class IntToken(Token):
    def __init__(self, i):
        super().__init__(TokenType.INT)
        self.intVal = i

    def getIntVal(self):
        return self.intVal

if __name__ == "__main__":
    tok = IntToken(42)
    print(tok.getType())
    print(tok.getIntVal())
