# CPS 310 Final Project
## Recipe & Meal Planner

A command-line app for browsing, searching, filtering, and scaling recipes stored in JSON.

## Features

- loading recipe data from JSON
- listing all recipes
- searching recipes by name
- searching recipes by ingredient
- filtering recipes by category
- viewing recipe details
- scaling a recipe to a new number of servings
- loading basic configuration from `config.json`

## Setup

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py
```

## Usage

When you run the app, it shows this menu:

```
1. List all recipes
2. Search recipes by name
3. Search recipes by ingredients
4. Filter recipes by category
5. View recipe details
6. Scale recipe servings
7. Exit
```

## Run Tests

### Windows

```powershell
python -m pytest -v
```

### macOS

```bash
python3 -m pytest -v
```

Tests run automatically on every push and pull request through GitHub Actions.
