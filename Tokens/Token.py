# Token -- Base class for Token objects

from Tokens import TokenType

class Token:
    def __init__(self, t):
        self.tt = t

    def getType(self):
        return self.tt

if __name__ == "__main__":
    tok = Token(TokenType.DOT)
    print(tok.getType())
