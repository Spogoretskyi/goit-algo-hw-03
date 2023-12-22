import argparse
from pathlib import Path
import shutil


COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"


def display_tree(path: Path, indent: str = "", prefix: str = "") -> None:
    if path.is_dir():
        print(indent + prefix + COLOR_BLUE + str(path.name) + COLOR_RESET)
        indent += "    " if prefix else ""

        children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))

        for index, child in enumerate(children):
            is_last = index == len(children) - 1
            display_tree(child, indent, "└── " if is_last else "├── ")
    else:
        print(indent + prefix + str(path.name))


def recursive_copy(src: Path, dest: Path):
    dest.mkdir(parents=True, exist_ok=True)

    for child in src.iterdir():
        if child.is_dir():
            recursive_copy(child, dest / child.name)
        else:
            extension = child.suffix[1:]
            destination_path = dest / extension / child.name
            destination_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(child, dest / child.suffix[1:] / child.name)

display_tree(Path("C:\Test"))

recursive_copy(Path("C:\Test"), Path('C:\Test_dist'))


def main():
    parser = argparse.ArgumentParser(
        description="Рекурсивно хкопійовані та відсортовані файли за їх розширенням."
    )
    parser.add_argument(
        "source_directory", type=Path, help="Шлях до вихідної директорії "
    )
    parser.add_argument(
        "destination_directory",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="Шлях до дирикторії призначення (default: 'dist')",
    )
    args = parser.parse_args()

    display_tree(args.source_directory)

    recursive_copy(args.source_directory, args.destination_directory)

    print("Файли зкопійовані та відсортовані успішно!")


if __name__ == "__main__":
    main()
