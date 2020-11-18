# TokenType -- Enumeration constants for identifying tokens

from enum import Enum

class TokenType(Enum):
    QUOTE = 1
    LPAREN = 2
    RPAREN = 3
    DOT = 4
    TRUE = 5
    FALSE = 6
    INT = 7
    STR = 8
    IDENT = 9

if __name__ == "__main__":
    print(TokenType.IDENT)
