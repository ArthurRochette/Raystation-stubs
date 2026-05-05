# Raystation-stubs
> **Disclaimer:** This project is not affiliated with, endorsed by, or associated with **RaySearch Laboratories**.

Type stubs (type hints) for the **RayStation** API, meant to improve:
- auto-completion,
- inline documentation (docstrings/signatures), in IDEs (PyCharm, VS Code/Pylance, etc.).



## Requirements

- Python installed (your IDE/tooling version; typically Python 3.9+ is fine)
- RayStation is required to *run* scripts, but **not required** just to benefit from IDE type hints.

## Installation (from a local path)

Install the repository from a local folder with `pip`:

```bash
pip install "C:/<path>/Raystation-stubs"
```

Notes:
- On Windows, quoting the path is recommended.
- Use the folder that contains `pyproject.toml` or `setup.py` (depending on the project structure).

## Using it in your IDE

Once installed, your IDE should pick up the stubs and provide:
- types,
- call signatures,
- documentation.

## Limitations

- These stubs describe the RayStation API **for typing/documentation purposes** and may be incomplete or differ across RayStation versions.
- Stubs provide **no runtime behavior** and do not add functionality.

## Contributing

Contributions are welcome:
- fix types/signatures,
- add missing classes/methods,
- improve docstrings.

Helpful additions:
- document which RayStation version(s) are targeted,
- add minimal examples (IDE-focused) to illustrate usage.
