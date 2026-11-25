def secure_archive(
    filename: str,
    action: str = "r",
    content: str = "",
) -> tuple[bool, str]:
    if action not in ("r", "w"):
        return (False, "Invalid action: use 'r' to read or 'w' to write")

    try:
        with open(filename, action, encoding="utf-8") as archive:
            if action == "r":
                result = archive.read()
            else:
                archive.write(content)
                result = "Content successfully written to file"
        return (True, result)
    except (OSError, UnicodeError, ValueError) as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("does_not_exist.txt"))

    # Run chmod 000 denied_fragment.txt before testing this case.
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("denied_fragment.txt"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    success, content = secure_archive("ancient_fragment.txt")
    print((success, content))

    if success:
        print("\nUsing 'secure_archive' to write previous content "
              "to a new file:")
        print(secure_archive("recovered_fragment.txt", "w", content))


if __name__ == "__main__":
    main()
