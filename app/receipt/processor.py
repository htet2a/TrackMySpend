from pathlib import Path


SUPPORTED_FORMATS = {
    "jpg",
    "jpeg",
    "png",
    "pdf",
}


def inspect_receipt_file(file_path: str) -> dict:
    """
    Inspect a receipt file.

    Returns basic file information.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Receipt file not found: {file_path}"
        )

    extension = path.suffix.lower().replace(".", "")

    if extension not in SUPPORTED_FORMATS:
        raise ValueError(
            f"Unsupported receipt format: {extension}"
        )

    return {
        "filename": path.name,
        "extension": extension,
        "size_bytes": path.stat().st_size,
    }