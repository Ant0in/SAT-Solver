


class Literal:

    def __init__(self, literal_name: str, apply_not: bool = False) -> None:
        
        self._literal_name: str = literal_name
        self._apply_NOT: bool = apply_not

    @property
    def name(self) -> str:
        return self._literal_name
    
    @property
    def apply_not(self) -> bool:
        return self._apply_NOT
    
    def set_apply_not(self, boolvar: bool) -> None:
        self._apply_NOT = boolvar

    def split_expression(self) -> 'Literal':
        return [[self]]
    
    def __repr__(self) -> str:
        return f"{'¬' if self.apply_not else ''}{self.name}"
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return isinstance(other, Literal) and self.name == other.name
    
