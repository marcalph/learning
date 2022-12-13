import hypothesis.strategies as st
from hypothesis import given, assume, example

def naive_write_csv_row(fields):
    return ",".join(f'"{field}"' for field in fields)

def naive_read_csv_row(row):
    return [field[1:-1] for field in row.split(",")]    

import string
def generate_westernized_name(min_size=2):
    return (st.text(alphabet=string.ascii_letters, min_size=min_size)
            .map(lambda name: name.capitalize()))


@given(fields=st.lists(st.text().filter(lambda t: t.isalnum()), min_size=1, max_size=10))
# @example([","]) # when you find a good hypothesiss, to ensure to test use example 
def test_write_read_csv(fields):
    # fields = ["Hello", "World"]
    formatted_row = naive_write_csv_row(fields)
    parsed_row = naive_read_csv_row(formatted_row)
    assert fields == parsed_row


@st.composite
def generate_full_name(draw):
    first_name = draw(generate_westernized_name())
    last_name = draw(generate_westernized_name())
    assume(first_name != last_name)
    return (last_name, first_name)


for _ in range(10):
    print(generate_full_name().example())


SYMBOLS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

import operator
def to_roman(number: int):
    numerals = []
    g = operator.itemgetter(1)
    ordered_numerals = sorted(
        (SYMBOLS | SUBTRACTIVE_SYMBOLS).items(),
        key=g,
        reverse=True,
    )
    while number >= 1:
        for symbol, value in ordered_numerals:
            if value <= number:
                numerals.append(symbol)
                number -= value
                break
    return "".join(numerals)


@given(numeral_value=st.sampled_from(tuple(SYMBOLS.items())))
def test_to_roman_numeral_sampled(numeral_value):
    numeral, value = numeral_value
    assert to_roman(value) == numeral

@given(number=st.integers(min_value=1, max_value=5000))
def test_to_roman_numeral_simple(number):
    numeral = to_roman(number)
    assert set(numeral) and set(numeral) <= set(SYMBOLS.keys())



def from_roman(numeral: str):
    carry = 0
    numerals = list(numeral)
    while numerals:
        symbol = numerals.pop(0)
        value = SYMBOLS[symbol]
        try:
            value = SUBTRACTIVE_SYMBOLS[symbol + numerals[0]]
            numerals.pop(0)
        except (IndexError, KeyError):
            pass
        carry += value
    return carry


@given(number=st.integers(min_value=1, max_value=5000))
def test_roman_numeral(number):
    numeral = to_roman(number)
    value = from_roman(numeral)
    assert number == value


SUBTRACTIVE_SYMBOLS = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}


@given(numeral_value=st.sampled_from(tuple(SUBTRACTIVE_SYMBOLS.items())))
def test_roman_subtractive_rule(numeral_value):
    numeral, value = numeral_value
    assert from_roman(numeral) == value
    assert to_roman(value) == numeral

if __name__ == "__main__":
    for _ in range(10):
        print(generate_full_name().example())