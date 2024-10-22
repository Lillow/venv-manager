import os
import msvcrt


def clean_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def wait_for_keypress() -> None:
    print("\nPress any key to continue...")

    try:
        msvcrt.getch()
    except Exception as e:
        print(f"Error waiting for key press: {e}")


def pause_and_clear() -> None:
    wait_for_keypress()
    clean_screen()


def print_line(str_list: list[str]) -> None:
    for item in str_list:
        print(item)
