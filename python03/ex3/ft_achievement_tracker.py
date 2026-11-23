import random


ACHIEVEMENTS = [
    "First Steps",
    "Master Explorer",
    "Treasure Hunter",
    "Boss Slayer",
    "Speed Runner",
    "Survivor",
    "Crafting Genius",
    "World Savior",
    "Collector Supreme",
    "Untouchable",
    "Strategist",
    "Unstoppable",
    "Hidden Path Finder",
    "Sharp Mind",
]


def gen_player_achievements() -> set[str]:
    count = random.randint(6, 9)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    players = [
        ("Alice", alice),
        ("Bob", bob),
        ("Charlie", charlie),
        ("Dylan", dylan),
    ]

    for name, achievements in players:
        print(f"Player {name}: {achievements}")

    distinct = alice.union(bob, charlie, dylan)
    common = alice.intersection(bob, charlie, dylan)
    print(f"\nAll distinct achievements: {distinct}")
    print(f"\nCommon achievements: {common}")

    print()
    for name, achievements in players:
        others: set[str] = set()
        for other_name, other_achievements in players:
            if other_name != name:
                others = others.union(other_achievements)
        unique = achievements.difference(others)
        print(f"Only {name} has: {unique}")

    print()
    all_achievements = set(ACHIEVEMENTS)
    for name, achievements in players:
        missing = all_achievements.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
