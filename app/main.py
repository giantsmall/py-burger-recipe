from __future__ import annotations
from abc import ABC


class Validator(ABC):
    def __set_name__(self, owner: any, name: str) -> None:
        self.protected_name = "_" + name
        print(f"validator: name = {self.protected_name}")

    def __get__(self) -> int:
        return self._value

    def __set__(self, value: int, third: any = 0) -> None:
        self.validate(value)
        self._value = value

    value = property(__get__, __set__)

    def validate(self) -> None:
        pass


class Number(Validator):
    def __init__(self, min_value: int, max_value: int) -> None:
        self.min_value = min_value
        self.max_value = max_value
        self._value = 5

    def validate(self, value: any) -> None:
        if not isinstance(value, int):
            raise TypeError("Quantity should be integer")
        elif self.min_value > self._value or self.max_value < self._value:
            raise ValueError(f"Quantity should not be less than \
                             {self.min_value} \
                             and greater than {self.max_value}")


class OneOf(Validator):
    def __init__(self, options: list) -> None:
        self.options = options

    def validate(self, value: str) -> None:
        if value not in self.options:
            raise ValueError(f"Expected {value} to be one of {self.options}")


class BurgerRecipe:
    def __init__(self,
                 buns: int,
                 cheese: int,
                 tomatoes: int,
                 cutlest: int,
                 eggs: int,
                 sauce: str) -> None:
        self.buns = buns
        self.cheese = cheese
        self.tomatoes = tomatoes
        self.cutlets = cutlest
        self.eggs = eggs
        self.sauce = sauce

    buns = Number(2, 3)
    cheese = Number(0, 2)
    tomatoes = Number(0, 3)
    cutlets = Number(1, 3)
    eggs = Number(0, 2)
    sauce = OneOf(["ketchup", "mayo", "burger"])
