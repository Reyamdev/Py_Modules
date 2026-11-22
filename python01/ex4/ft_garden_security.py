class Plant:
    def __init__(self, name: str, height: float, age_d: int) -> None:
        self.name = name
        self._height = 0.0
        self._age_d = 0
        self.set_height(height)
        self.set_age(age_d)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height

    def set_age(self, age_d: int) -> None:
        if age_d < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age_d = age_d

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_d

    def grow(self, amount: float) -> None:
        self.set_height(self.get_height() + amount)

    def age(self) -> None:
        self.set_age(self.get_age() + 1)

    def show(self) -> None:
        print(
            f"{self.name}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    rose.set_height(25.0)
    print(f"Height updated: {rose.get_height():g}cm")

    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")
    print()

    rose.set_height(-5.0)
    rose.set_age(-10)
    print()

    print("Current state: ", end="")
    rose.show()
