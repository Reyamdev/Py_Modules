import sys


def read_archive(filename: str) -> str | None:
    try:
        archive = open(filename, "r", encoding="utf-8")
    except (OSError, ValueError) as error:
        print(f"Error opening file '{filename}': {error}")
        return None

    try:
        try:
            content = archive.read()
        finally:
            archive.close()
    except (OSError, UnicodeError) as error:
        print(f"Error reading or closing file '{filename}': {error}")
        return None

    return content


def write_archive(filename: str, content: str) -> bool:
    try:
        archive = open(filename, "w", encoding="utf-8")
    except (OSError, ValueError) as error:
        print(f"Error opening file '{filename}': {error}")
        return False

    try:
        try:
            archive.write(content)
        finally:
            archive.close()
    except (OSError, UnicodeError) as error:
        print(f"Error writing or closing file '{filename}': {error}")
        return False

    return True


def display_content(content: str) -> None:
    print("---\n")
    print(content, end="")
    if content and not content.endswith("\n"):
        print()
    print("\n---")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    content = read_archive(filename)
    if content is None:
        return

    display_content(content)
    print(f"File '{filename}' closed.")

    transformed = "".join(line + "#\n" for line in content.splitlines())
    print("\nTransform data:")
    display_content(transformed)

    try:
        new_filename = input("Enter new file name (or empty): ")
    except (EOFError, OSError, UnicodeError, KeyboardInterrupt) as error:
        print(f"Error reading input: {error}")
        print("Data not saved.")
        return

    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    if write_archive(new_filename, transformed):
        print(f"Data saved in file '{new_filename}'.")
    else:
        print("Data not saved.")


if __name__ == "__main__":
    main()
