# IdentToken -- Token object for representing identifiers

from Tokens import TokenType
from Tokens import Token

class IdentToken(Token):
    def __init__(self, s):
        super().__init__(TokenType.IDENT)
        self.name = s

    def getName(self):
        return self.name

if __name__ == "__main__":
    tok = IdentToken("foo")
    print(tok.getType())
    print(tok.getName())

