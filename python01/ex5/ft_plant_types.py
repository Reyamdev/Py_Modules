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


class Flower(Plant):
    def __init__(self, name: str, height: float, age_d: int,
                 color: str) -> None:
        super().__init__(name, height, age_d)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age_d: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age_d)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.get_height():.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_d: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age_d)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def grow(self, amount: float) -> None:
        super().grow(amount)
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value:g}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for day in range(20):
        tomato.grow(2.1)
        tomato.age()
    tomato.show()
