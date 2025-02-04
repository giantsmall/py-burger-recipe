from __future__ import annotations
from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, owner: any, name: str) -> None:
        self.protected_name = "_" + name

    def __get__(self, value: any, value2: any) -> int:
        return self._value

    def __set__(self, value: int, third: any = 0) -> None:
        try:
            self.validate(value)
            self._value = value
        except TypeError as error:
            print(error)
        except ValueError as error:
            print(error)

    value = property(__get__, __set__)

    @abstractmethod
    def validate(self) -> None:
        pass


class Number(Validator):
    def __init__(self, min_value: int, max_value: int) -> None:
        self.min_value = min_value
        self.max_value = max_value
        self._value = 5

    def validate(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Quantity should be integer: {type(value)}")
        elif self.min_value > self._value or self.max_value < self._value:
            raise ValueError(f"Quantity should not be less than \
                             attribute minvalue \
                             and greater than attribute maxvalue.")


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
                 cutlest: int,
                 eggs: int,
                 sauce: str) -> None:
        print(type(buns))
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

burger = BurgerRecipe(1, 2, 2, 2, 2, "ketchup")