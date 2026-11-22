class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def show(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    # below is existing, above is added statistics class

    def __init__(self, name: str, height: float, age_d: int) -> None:
        self.name = name
        self._height = 0.0
        self._age_d = 0
        self.set_height(height)
        self.set_age(age_d)
        self._stats = self.Statistics()

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
        self._stats.record_grow()
        self.set_height(self.get_height() + amount)

    def age(self, days: int = 1) -> None:
        self._stats.record_age()
        self.set_age(self.get_age() + days)

    # staticmethod receives neither self nor cls. It uses only the age you pass
    @staticmethod
    def is_older_than_year(age_d: int) -> bool:
        return age_d > 365

    # receives the class as cls.
    # When you call Plant.create_anonymous(), cls refers to Plant,
    # so it constructs a plant with default values
    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        self._stats.record_show()
        print(
            f"{self.name}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )

    def show_statistics(self) -> None:
        self._stats.show()


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
    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def show(self) -> None:
            super().show()
            print(f" {self._shade_calls} shade")

    _stats: "Tree.Statistics"

    def __init__(self, name: str, height: float, age_d: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age_d)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self._stats.record_shade()
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

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value:g}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age_d: int,
                 color: str) -> None:
        super().__init__(name, height, age_d, color)
        self.seeds = 0

    def bloom(self, seeds: int = 42) -> None:
        super().bloom()
        self.seeds = seeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.show_statistics()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    for days in (30, 400):
        result = Plant.is_older_than_year(days)
        print(f"Is {days} days more than a year? -> {result}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom(42)
    sunflower.show()
    display_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_statistics(unknown)
