

from core.literal import Literal


class Expression:

    def __init__(self, first:'Expression | Literal', second: 'Expression | Literal' = None) -> None:
        
        self._first: Expression | Literal = first
        self._second: Expression | Literal = second

    @property
    def first(self) -> 'Expression | Literal':
        return self._first
    
    @property
    def second(self) -> 'Expression | Literal':
        return self._second
