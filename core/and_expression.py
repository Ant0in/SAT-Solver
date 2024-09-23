

from core.expression import Expression
from core.literal import Literal


class AND_Expression(Expression):

    def __init__(self, first: Expression | Literal, second: Expression | Literal) -> None:
        super().__init__(first, second)

    def split_expression(self) -> list[list[Expression | Literal]]:
        return [[self.first, self.second]]


