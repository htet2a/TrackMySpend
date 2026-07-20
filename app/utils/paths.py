from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def get_project_path(relative_path: str) -> Path:
    """
    Convert a project-relative path into an absolute path.
    """

    return PROJECT_ROOT / relative_path