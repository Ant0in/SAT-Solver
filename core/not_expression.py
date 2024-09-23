

from core.expression import Expression
from core.and_expression import AND_Expression
from core.or_expression import OR_Expression
from core.literal import Literal


class NOT_Expression(Expression):

    def __init__(self, first: Expression | Literal) -> None:
        super().__init__(first, None)

    def split_expression(self) -> list[list[Expression | Literal]]:
        
        ft: Expression | Literal = self.first
        
        if isinstance(ft, Literal):
            self.first.set_apply_not(not self.first.apply_not)
            return [[self.first]]

        elif isinstance(ft, AND_Expression):
            # Applique la loi de De Morgan : ¬(A ∧ B) = ¬A ∨ ¬B
            return [[NOT_Expression(ft.first)], [NOT_Expression(ft.second)]]

        elif isinstance(ft, OR_Expression):
            # Applique la loi de De Morgan : ¬(A ∨ B) = ¬A ∧ ¬B
            return [[NOT_Expression(ft.first), NOT_Expression(ft.second)]]

        else:
            raise NotImplementedError(f'Unsupported type: {type(ft)}')

    def __repr__(self) -> str:
        return f'(¬{self.first})'