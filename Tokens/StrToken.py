# StrToken -- Token object for representing string constants

from Tokens import TokenType
from Tokens import Token

class StrToken(Token):
    def __init__(self, s):
        super().__init__(TokenType.STR)
        self.strVal = s

    def getStrVal(self):
        return self.strVal

if __name__ == "__main__":
    tok = StrToken("hello")
    print(tok.getType())
    print(tok.getStrVal())
