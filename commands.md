# Useful console commands

## Creating virtual environments

```powershell
python -m venv .venv
```

## Activating virtual environments

```powershell
.venv/Scripts/activate  
```

```powershell
pip freeze > requirements.txt # save dependencies
pip install -r requirements.txt # restore dependencies
```

## Git credentials

```powershell
git config user.name "..."
git config user.email "...@gmail.com"
```
