"""
Contains parsing functionality for API controllers
"""


class SortArg:
    """
    Represents parsed sort string passed via API
    """
    def __init__(self, order, attr, clz_sortable_attrs):
        if not (order in ["+", "-"]): raise ValueError(f"Invalid operator (\"{order}\")")
        self._asc = order == "+"

        if not attr or not (attr in clz_sortable_attrs): raise ValueError(f"Unsortable attribute (\"{attr}\")")
        self._attribute = attr

    def __repr__(self):
        return "%s('%s', '%s')" % (SortArg.__name__, "+" if self.asc else "-", self.attribute)

    def __eq__(self, other):
        return self.attribute == other.attribute

    def __hash__(self):                 # Required for duplicate check (using `set`)
        return hash(self.attribute)

    @property
    def asc(self):
        return self._asc

    @property
    def attribute(self):
        return self._attribute

    @classmethod
    def from_str(cls, sort_str, clz_sortable_attrs):
        """
        Creates list of parsed `SortArg`s from string

        Assumed "encoding": <order><property1>[,<order><property2>,...] whereas
            - order may be '+' for asc or '-' for desc
        """
        sort_args = [cls(attr_str[0], attr_str[1:], clz_sortable_attrs) for attr_str in sort_str.split(",") if attr_str]
        if len(set(sort_args)) != len(sort_args): raise ValueError("Duplicate attributes")
        return sort_args
