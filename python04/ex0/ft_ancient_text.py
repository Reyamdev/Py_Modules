import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        archive: typing.IO[str] = open(filename, "r", encoding="utf-8")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return

    try:
        try:
            content = archive.read()
        finally:
            archive.close()
    except (OSError, UnicodeError) as error:
        print(f"Error reading or closing file '{filename}': {error}")
        return

    print("---\n")
    print(content, end="")
    if content and not content.endswith("\n"):
        print()
    print("\n---")
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
