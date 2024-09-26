


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
 
    def __repr__(self) -> str:
        return f"{'¬' if self.apply_not else ''}{self.name}"
