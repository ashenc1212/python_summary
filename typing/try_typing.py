import typing
from typing import List
from typing import NewType
from typing import Callable

# the comment has effect
lst = [] # type: List[int]
lst.append(1.2)

# type declaration in a function
def func(x: int) -> int:
    print(x)
    return 1
func(1.2)

# type alias
Vector = List[float]
myvec: Vector = []
myvec.append('hello')

# new type
UserId = NewType('UserId', int)
def foo(someone: UserId) -> UserId:
    return someone
foo(121)

# Callable
def to_be_called(s: str):
    print("I'm called with %s"%s)
def call_other(func: Callable[[int], None]) -> None:
    print("calling others")
call_other(to_be_called)