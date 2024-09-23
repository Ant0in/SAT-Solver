

from core.expression import Expression
from core.and_expression import AND_Expression
from core.or_expression import OR_Expression
from core.literal import Literal


class NOT_Expression(Expression):

    def __init__(self, first: Expression | Literal) -> None:
        super().__init__(first, None)

    def split_expression(self) -> list[list[Expression | Literal]]:
        
        ft: Expression | Literal = type(self.first)
        
        if isinstance(ft, Literal):
            self.first.set_apply_not(boolvar=(not self.first.apply_not))
            return [[self.first]]

        # Morgan's rules
        elif isinstance(ft, AND_Expression): return [[NOT_Expression(first=self.first)], [NOT_Expression(first=self.second)]]
        elif isinstance(ft, OR_Expression): return [[NOT_Expression(first=self.first), NOT_Expression(first=self.second)]]
        else: raise NotImplementedError(f'?{ft}')