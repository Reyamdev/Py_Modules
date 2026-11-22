class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown watering error") -> None:
        super().__init__(message)


def raise_plant_err() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_err() -> None:
    raise WaterError("Not enough water in the tank!")


def test_error_types() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        raise_plant_err()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting WaterError...")
    try:
        raise_water_err()
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting catching all garden errors...")
    try:
        raise_plant_err()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    try:
        raise_water_err()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_error_types()
