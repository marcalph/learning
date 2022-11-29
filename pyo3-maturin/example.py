import pyo3_maturin as rust
import timeit
print(rust.__all__)

def get_fib_py(number: int) -> int:
    """Get the nth Fibonacci number."""
    if number == 1:
        return 1
    elif number == 2:
        return 2

    total = 0
    last = 0
    current = 1
    for _ in range(1, number):
        total = last + current
        last = current
        current = total
    return total

rust_struct = rust.RustStruct(data="some data", vector=[255, 255, 255])
rust_struct.extend_vector([1, 1, 1, 1])
rust_struct.printer()

from pydantic import BaseModel

class Human(BaseModel):
    name: str
    age: int

jan = Human(name="Jan", age=6)
print(jan.json())
rust.human_says_hi(jan.json())

if __name__ == '__main__':
    print(timeit.timeit("get_fib_py(100)", setup="from __main__ import get_fib_py"))
    print(timeit.timeit("get_fib_rs(100)", setup="from pyo3_maturin import get_fib_rs"))


