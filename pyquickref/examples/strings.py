"""String operation examples for PyQuickRef.

String manipulation, formatting, unicode, and encoding.
Docs: https://docs.python.org/3/library/stdtypes.html#string-methods
"""

from pyquickref.registry import example, show
from pyquickref.testdata import SampleData


@example(
    "Strings",
    "str vs bytes, encode/decode, UTF-8, Unicode characters",
    doc_url="https://docs.python.org/3/howto/unicode.html",
)
def unicode_bytes() -> None:
    """Demonstrate Unicode strings and bytes encoding/decoding."""
    # str is Unicode text, bytes is raw data
    text = "Hello, World!"
    encoded = text.encode("utf-8")
    show("text = 'Hello, World!'\nencoded = text.encode('utf-8')")
    print(f"str:   {text!r} (type: {type(text).__name__})")
    print(f"bytes: {encoded!r} (type: {type(encoded).__name__})")

    # Decode bytes back to str
    show("encoded.decode('utf-8')")
    print(f"decoded: {encoded.decode('utf-8')!r}")

    # Unicode characters
    show("'cafe\\u0301'  # e + combining accent\n'caf\\xe9'     # precomposed é")
    combined = "cafe\u0301"
    precomposed = "caf\xe9"
    print(f"cafe\\u0301  = {combined!r} (len={len(combined)})")
    print(f"caf\\xe9     = {precomposed!r} (len={len(precomposed)})")

    # Multi-byte encoding
    emoji = "\U0001f40d"
    show("emoji = '\\U0001f40d'  # snake emoji")
    utf8 = emoji.encode("utf-8")
    print(f"str: {emoji!r} (len={len(emoji)})")
    print(f"utf-8 bytes: {utf8!r} (len={len(utf8)})")

    # Encoding differences
    text2 = "Python"
    show("'Python'.encode('ascii')\n'Python'.encode('utf-16')")
    print(f"ascii:  {text2.encode('ascii')!r}")
    print(f"utf-16: {text2.encode('utf-16')!r}")


@example(
    "Strings",
    "Upper, lower, split, replace, f-strings, str.format()",
    doc_url="https://docs.python.org/3/library/stdtypes.html#string-methods",
    needs_test_data=True,
)
def string_operations(data: SampleData) -> None:
    """Perform various string operations and demonstrate their usage."""
    print(f"Original string: '{data.teststring}'")

    show("teststring.upper()")
    print(f"Uppercase: '{data.teststring.upper()}'")

    show("teststring.lower()")
    print(f"Lowercase: '{data.teststring.lower()}'")

    show("teststring.split()")
    print(f"Split by space: {data.teststring.split()}")

    show("teststring.replace('awesome', 'amazing')")
    print(f"Replace: '{data.teststring.replace('awesome', 'amazing')}'")

    show("'Python' in teststring")
    print(f"Contains 'Python': {'Python' in data.teststring}")

    # String formatting
    name = "World"
    # f-strings (Python 3.6+)
    show("f'Hello, {name}!'")
    print(f"f-string: Hello, {name}!")
    # Older formatting style (still useful for templates)
    print("str.format: Hello, {}!".format(name))
    print("The {animal} is {color}".format(animal="fox", color="brown"))
