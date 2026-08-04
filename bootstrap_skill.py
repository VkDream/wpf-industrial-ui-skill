from __future__ import annotations

import base64
import io
import shutil
import zipfile
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    chunk_dir = root / ".bootstrap_payload"
    payload = "".join(path.read_text(encoding="ascii") for path in sorted(chunk_dir.glob("chunk_*")))
    if not payload:
        raise RuntimeError("bootstrap payload is missing")

    data = base64.b64decode(payload)
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        archive.extractall(root)

    shutil.rmtree(chunk_dir, ignore_errors=True)
    for relative in ["bootstrap_skill.py", ".github/workflows/bootstrap.yml"]:
        path = root / relative
        if path.exists():
            path.unlink()


if __name__ == "__main__":
    main()
