from __future__ import annotations

import base64
import io
import shutil
import zipfile
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    chunk_dir = root / ".bootstrap_payload"
    chunks = sorted(chunk_dir.glob("chunk_*"))
    payload = "".join(path.read_text(encoding="ascii") for path in chunks)
    if not payload:
        raise RuntimeError("bootstrap payload is missing")

    data = base64.b64decode(payload, validate=True)
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        archive.testzip()
        archive.extractall(root)

    shutil.rmtree(chunk_dir, ignore_errors=True)
    for relative in [
        "bootstrap_skill.py",
        ".bootstrap-trigger",
        ".github/workflows/bootstrap.yml",
    ]:
        path = root / relative
        if path.exists():
            path.unlink()


if __name__ == "__main__":
    main()
