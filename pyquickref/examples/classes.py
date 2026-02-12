"""Class and OOP examples for PyQuickRef.

Classes, inheritance, properties, and dunder methods.
Docs: https://docs.python.org/3/tutorial/classes.html
"""

from pyquickref.registry import example, show


@example(
    "Classes",
    "class, __init__, methods, inheritance, super(), classmethod",
    doc_url="https://docs.python.org/3/tutorial/classes.html",
)
def class_basics() -> None:
    """Demonstrate class definitions, inheritance, and class methods."""

    class Animal:
        """A basic animal with a name and sound."""

        def __init__(self, name: str, sound: str) -> None:
            self.name = name
            self.sound = sound

        def speak(self) -> str:
            """Return what the animal says."""
            return f"{self.name} says {self.sound}"

    show(Animal)
    cat = Animal("Cat", "meow")
    print(cat.speak())

    class Dog(Animal):
        """A dog that inherits from Animal."""

        def __init__(self, name: str, breed: str) -> None:
            super().__init__(name, "woof")
            self.breed = breed

        def fetch(self) -> str:
            """Return a string about fetching."""
            return f"{self.name} the {self.breed} fetches the ball!"

    show(Dog)
    dog = Dog("Rex", "Labrador")
    print(dog.speak())
    print(dog.fetch())

    class Circle:
        """A circle defined by its radius."""

        def __init__(self, radius: float) -> None:
            self.radius = radius

        @classmethod
        def from_diameter(cls, diameter: float) -> "Circle":
            return cls(diameter / 2)

        @staticmethod
        def area_formula() -> str:
            """Return the formula for circle area."""
            return "A = pi * r^2"

    show(Circle)
    c = Circle.from_diameter(10)
    print(f"Circle(diameter=10) → radius={c.radius}")
    print(f"Formula: {Circle.area_formula()}")

    class Temperature:
        """A temperature in Celsius with Fahrenheit conversion."""

        def __init__(self, celsius: float) -> None:
            self._celsius = celsius

        @property
        def fahrenheit(self) -> float:
            """Convert to Fahrenheit."""
            return self._celsius * 9 / 5 + 32

    show(Temperature)
    t = Temperature(100)
    print(f"100°C = {t.fahrenheit}°F")


@example(
    "Classes",
    "__str__, __repr__, __len__, __eq__, __lt__, __add__",
    doc_url="https://docs.python.org/3/reference/datamodel.html#special-method-names",
)
def dunder_methods() -> None:
    """Demonstrate special (dunder) methods."""

    class Vector:
        """A 2D vector with arithmetic operations."""

        def __init__(self, x: float, y: float) -> None:
            self.x = x
            self.y = y

        def __repr__(self) -> str:
            return f"Vector({self.x}, {self.y})"

        def __str__(self) -> str:
            return f"({self.x}, {self.y})"

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, Vector):
                return NotImplemented
            return self.x == other.x and self.y == other.y

        def __lt__(self, other: "Vector") -> bool:
            return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

        def __add__(self, other: "Vector") -> "Vector":
            return Vector(self.x + other.x, self.y + other.y)

        def __len__(self) -> int:
            return 2

    show(Vector)

    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    print(f"repr:  {v1!r}")
    print(f"str:   {v1}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 == Vector(1, 2)? {v1 == Vector(1, 2)}")
    print(f"v1 < v2? {v1 < v2}")
    print(f"len(v1) = {len(v1)}")
