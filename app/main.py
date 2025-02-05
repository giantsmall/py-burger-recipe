from __future__ import annotations
from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, owner: any, name: str) -> None:
        self.protected_name = "_" + name

    def __get__(self) -> any:
        return self._value

    def __set__(self, owner: any, value: int) -> None:
        self.validate(value)
        self._value = value
    
    _value = property(__get__, __set__)

    @abstractmethod
    def validate(self, value) -> None:
        pass


class Number(Validator):
    def __init__(self, min_value: int, max_value: int) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Quantity should be integer.")
        elif self.min_value > value or self.max_value < value:
            print(f"Validating {value}")
            raise ValueError(f"Quantity should not be less than attribute minvalue and greater than attribute maxvalue.")


class OneOf(Validator):
    def __init__(self, options: list) -> None:
        self.options = options

    def validate(self, value: str) -> None:
        if not value in self.options:
            raise ValueError(f"Expected {value} to be one of {self.options}")


class BurgerRecipe:
    def __init__(self,
                 buns: int,
                 cheese: int,
                 tomatoes: int,
                 cutlet: int,
                 eggs: int,
                 sauce: str) -> None:
        self.buns = buns
        self.cheese = cheese
        self.tomatoes = tomatoes
        self.cutlets = cutlet
        self.eggs = eggs
        self.sauce = sauce

    @staticmethod
    def __dict__() -> dict:
        return {"1": 2}

    buns = Number(2, 3)
    cheese = Number(0, 2)
    tomatoes = Number(0, 3)
    cutlets = Number(1, 3)
    eggs = Number(0, 2)
    sauce = OneOf(["ketchup", "mayo", "burger"])

burger = BurgerRecipe(2,2,2,2,2, "ketchup")
