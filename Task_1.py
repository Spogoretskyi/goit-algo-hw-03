import argparse
from pathlib import Path
import shutil


def recursive_copy(src: Path, dest: Path, dest_extended: Path = None):
    if not src.exists:
        print(f"Source directory {src} not exists.")
    if not dest.exists:
        print(f"Destination directory {dest} not exists.")

    try:
        for child in src.iterdir():
            if child.is_dir():
                recursive_copy(child, dest, dest / child.name)
            else:
                extension = child.suffix[1:]
                destination_path = dest / extension / child.name
                destination_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(child, dest / child.suffix[1:] / child.name)
    except PermissionError as ex:
        print(f"Permission error: {ex}")
    except FileNotFoundError as ex:
        print(f"File not found error: {ex}")
    except Exception as ex:
        print(f"An error occurred: {ex}")


def main():
    try:
        parser = argparse.ArgumentParser(
            description="Recursive copying and sorted files by their extension."
        )
        parser.add_argument(
            "source_directory", type=Path, help="The path to the source directory."
        )
        parser.add_argument(
            "destination_directory",
            type=Path,
            nargs="?",
            default=Path("dist"),
            help="Path to destination directory (default: 'dist').",
        )
        args = parser.parse_args()

        recursive_copy(args.source_directory, args.destination_directory)

        print("Files copied and sorted successfully.")
    except KeyboardInterrupt:
        print("Operation canceled by user.")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")


if __name__ == "__main__":
    main()
