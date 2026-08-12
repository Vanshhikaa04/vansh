"""Read a file lazily in fixed-size chunks, useful for large files."""
from collections.abc import Iterator


def read_in_chunks(file_path: str, chunk_size: int = 8192) -> Iterator[str]:
    with open(file_path, "r", encoding="utf-8") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            yield chunk
