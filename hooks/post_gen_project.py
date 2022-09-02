import sys
import shutil
from pathlib import Path


package_name = "{{cookiecutter.package_name}}"
use_clean_architecture = "{{cookiecutter.use_clean_architecture}}".lower() == "y"
package_path = Path("src") / package_name


def remove_clean_architecture():
    """Remove files related to clean architecture."""
    print("Removing clean architecture files from project...")
    for folder in ["domain", "application", "infrastructure", "presentation"]:
        folder_path = package_path / folder
        shutil.rmtree(folder_path)
    print("Removing of clean architecture files completed.")


def remove_sample_files():
    """Remove sample module and unit test."""
    print("Removing sample files from project...")
    test_path = Path("tests")
    sample_file_paths = [package_path / "sum.py", test_path / "unit" / "test_sum.py"]
    for file_path in sample_file_paths:
        file_path.unlink()
    print("Removing of sample files completed.")


def main():
    """Cookiecutter post-hook."""
    if not use_clean_architecture:
        remove_clean_architecture()
    else:
        remove_sample_files()
    sys.exit(0)


if __name__ == "__main__":
    main()
