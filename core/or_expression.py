

from core.expression import Expression
from core.literal import Literal


class OR_Expression(Expression):

    def __init__(self, first: Expression | Literal, second: Expression | Literal) -> None:
        super().__init__(first, second)

    def __repr__(self) -> str:
        return f'({self.first} v {self.second})'