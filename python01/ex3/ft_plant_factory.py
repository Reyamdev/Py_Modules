class Plant:
    def __init__(self, name: str, height: float, age_d: int) -> None:
        self.name = name
        self.height = height
        self.age_d = age_d

    def grow(self, amount: float) -> None:
        self.height += amount

    def age(self) -> None:
        self.age_d += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm, {self.age_d} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    plants = [rose, oak, cactus, sunflower, fern]
    # end="" prevents adding a newline
    for plant in plants:
        print("Created: ", end="")
        plant.show()
