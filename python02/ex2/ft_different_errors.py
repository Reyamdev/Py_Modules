def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        print(10 / 0)
    elif operation_number == 2:
        with open("/non/existent/file"):
            pass
    elif operation_number == 3:
        # Intentionally invalid to demonstrate TypeError.
        print("Plants: " + 5)  # type: ignore[operator]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for operation_number in (0, 1, 2, 3, 4):
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")
        else:
            print("Operation completed successfully")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
