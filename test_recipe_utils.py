"""Tests for the starter Recipe & Meal Planner."""

import json

import pytest

from recipe_utils import (
    filter_by_category,
    load_config,
    load_recipes,
    search_by_ingredient,
    search_by_name,
)

CHICKEN = {
    "name": "Chicken Alfredo",
    "category": "Dinner",
    "ingredients": [
        {"name": "chicken breast"},
        {"name": "fettuccine"},
        {"name": "parmesan cheese"},
    ],
}
SMOOTHIE = {
    "name": "Berry Smoothie",
    "category": "Snack",
    "ingredients": [
        {"name": "strawberries"},
        {"name": "banana"},
        {"name": "yogurt"},
    ],
}
PASTA = {
    "name": "Tomato Pasta",
    "category": "Dinner",
    "ingredients": [
        {"name": "spaghetti"},
        {"name": "tomato sauce"},
        {"name": "mozzarella cheese"},
        {"name": "parmesan cheese"},
    ],
}


@pytest.fixture
def recipes():
    return [CHICKEN, SMOOTHIE, PASTA]


@pytest.mark.parametrize(
    "term, expected",
    [
        ("chicken", [CHICKEN]),
        ("SMOOTHIE", [SMOOTHIE]),
        ("pizza", []),
    ],
    ids=["partial_match", "case_insensitive", "no_match"],
)
def test_search_by_name(recipes, term, expected):
    assert search_by_name(recipes, term) == expected


@pytest.mark.parametrize("category", ["Dinner", "dinner"], ids=["exact", "case_insensitive"])
def test_filter_by_category(recipes, category):
    assert filter_by_category(recipes, category) == [CHICKEN, PASTA]


@pytest.mark.parametrize(
    "term, expected",
    [
        ("fettuccine", [CHICKEN]),
        ("straw", [SMOOTHIE]),
        ("BANANA", [SMOOTHIE]),
        ("pizza dough", []),
        ("cheese", [CHICKEN, PASTA]),
    ],
    ids=["full_name", "partial_match", "case_insensitive", "no_match", "no_duplicates"],
)
def test_search_by_ingredient(recipes, term, expected):
    assert search_by_ingredient(recipes, term) == expected


def test_search_by_ingredient_handles_empty_ingredients():
    recipes = [{"name": "Plain Water", "category": "Drink", "ingredients": []}]
    assert search_by_ingredient(recipes, "water") == []


def test_load_config_reads_json(tmp_path):
    config_file = tmp_path / "config.json"
    config_file.write_text(
        json.dumps(
            {
                "app_title": "Test Planner",
                "recipe_file": "recipes.json",
                "default_servings": 2,
            }
        ),
        encoding="utf-8",
    )
    result = load_config(config_file)
    assert result["app_title"] == "Test Planner"
    assert result["default_servings"] == 2


def test_load_recipes_reads_json(tmp_path):
    recipe_file = tmp_path / "recipes.json"
    sample = [
        {
            "name": "Test Recipe",
            "category": "Lunch",
            "servings": 2,
            "prep_time": 5,
            "cook_time": 10,
            "ingredients": [],
        }
    ]
    recipe_file.write_text(json.dumps(sample), encoding="utf-8")
    assert load_recipes(recipe_file) == sample
