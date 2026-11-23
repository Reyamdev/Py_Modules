import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            x, y, z = text.split(",")
        except ValueError:
            print("Invalid syntax")
            continue

        coordinates: list[float] = []
        try:
            for parameter in (x, y, z):
                coordinates.append(float(parameter))
        except ValueError as error:
            print(f"Error on parameter '{parameter}': {error}")
            continue

        return (coordinates[0], coordinates[1], coordinates[2])


def calculate_distance(
    first: tuple[float, float, float],
    second: tuple[float, float, float],
) -> float:
    x1, y1, z1 = first
    x2, y2, z2 = second
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    try:
        print("Get a first set of coordinates")
        first = get_player_pos()
        print(f"Got a first tuple: {first}")
        x, y, z = first
        print(f"It includes: X={x}, Y={y}, Z={z}")
        distance = calculate_distance(first, (0.0, 0.0, 0.0))
        print(f"Distance to center: {round(distance, 4)}")

        print("\nGet a second set of coordinates")
        second = get_player_pos()
        distance = calculate_distance(first, second)
        print(f"Distance between the 2 sets of coordinates: "
              f"{round(distance, 4)}")
    except (EOFError, KeyboardInterrupt):
        print("\nCoordinate input cancelled.")


if __name__ == "__main__":
    main()
