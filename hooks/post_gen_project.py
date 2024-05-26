import sys
import shutil
from pathlib import Path


package_name = "{{cookiecutter.package_name}}"
root_path = Path(".").absolute()
package_path = root_path / "src" / package_name
test_path = root_path / "tests"
use_clean_architecture = "{{cookiecutter.use_clean_architecture}}"
add_fastapi_application = "{{cookiecutter.add_fastapi_application}}"
add_repository_and_sqlalchemy = "{{cookiecutter.add_repository_and_sqlalchemy}}"


def remove_clean_architecture():
    """Remove files related to clean architecture."""
    print("Removing clean architecture files from project...")
    paths_to_remove = {
        package_path: ["domain", "application", "infrastructure", "presentation"],
        test_path:  [
            "unit/domain", "unit/application", "unit/infrastructure", "unit/presentation",
            "integration/domain", "integration/application", "integration/infrastructure",
            "integration/presentation",
        ],
    }
    remove_paths(paths_to_remove)
    print("Remotion of clean architecture files completed.")


def remove_sample_files():
    """Remove sample module and unit test."""
    print("Removing sample files from project...")
    paths_to_remove = {
        package_path: ["sum.py"],
        test_path: ["unit/test_sum.py"],
    }
    remove_paths(paths_to_remove)
    print("Remotion of sample files completed.")


def remove_fastapi():
    """Remove fastapi code."""
    print("Removing FastAPI files from project...")
    paths_to_remove = {
        package_path: [ "infrastructure/server", "presentation/be_server.sh"],
    }
    remove_paths(paths_to_remove)
    print("Remotion of FastAPI files completed.")


def remove_repository_and_sqlalchemy():
    """Remove repository and sqlalchemy code."""
    print("Removing Repository and SQLAlchemy files from project...")
    paths_to_remove = {
        package_path: [
            "application/interfaces/db",
            "domain/todo.py",
            "domain/todolist.py",
            "infrastructure/adapters/alchemy",
            "tests/unit/domain/todo.py",
            "tests/unit/domain/todolist.py",
            "tests/integration/adapters/alchemy",
        ],
    }
    remove_paths(paths_to_remove)
    print("Remotion of repository and SQLAlchemy files completed.")


def remove_paths(paths_to_remove: dict[Path, list[str]]) -> None:
    """Remove items in paths.

    Args:
        paths_to_remove: Dict with path prefixes and list of items to remove.
    """
    for base_path, item_list in paths_to_remove.items():
        for item in item_list:
            item_path = base_path / item
            try:
                if item_path.is_file():
                    item_path.unlink()
                else:
                    shutil.rmtree(item_path)
            except FileNotFoundError:
                pass


def main():
    """Cookiecutter post-hook."""
    if not use_clean_architecture:
        remove_clean_architecture()
    else:
        remove_sample_files()
    if not add_fastapi_application:
        remove_fastapi()
    if not add_repository_and_sqlalchemy:
        remove_repository_and_sqlalchemy()
    sys.exit(0)


if __name__ == "__main__":
    main()
