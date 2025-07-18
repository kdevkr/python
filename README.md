# Python

## Install python

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

uv pyhton install 3.12
```

## Lock and sync project

```powershell
uv lock
uv sync
uv run
```

## Generate requirements.txt

```powershell
# uv pip freeze > requirements.txt
uv export --no-hashes --format requirements-txt > requirements.txt
```