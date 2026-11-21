"""Tests for the starter Recipe & Meal Planner."""

import json

import pytest

from recipe_utils import (
    filter_by_category,
    load_config,
    load_recipes,
    scale_recipe,
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


@pytest.fixture
def alfredo():
    return {
        "name": "Chicken Alfredo",
        "category": "Dinner",
        "servings": 4,
        "ingredients": [
            {"name": "chicken breast", "quantity": 1.5, "unit": "lb"},
            {"name": "fettuccine", "quantity": 12, "unit": "oz"},
            {"name": "heavy cream", "quantity": 2, "unit": "cups"},
        ],
    }


@pytest.mark.parametrize(
    "new_servings, expected_quantities",
    [
        (8, [3.0, 24.0, 4.0]),
        (2, [0.75, 6.0, 1.0]),
        (6, [2.25, 18.0, 3.0]),
        (4, [1.5, 12.0, 2.0]),
    ],
    ids=["scale_up", "scale_down", "decimal_factor", "same_size"],
)
def test_scale_recipe_quantities(alfredo, new_servings, expected_quantities):
    scaled = scale_recipe(alfredo, new_servings)
    assert [ingredient["quantity"] for ingredient in scaled["ingredients"]] == expected_quantities


def test_scale_recipe_updates_servings_and_keeps_other_fields(alfredo):
    scaled = scale_recipe(alfredo, 2)
    assert scaled["servings"] == 2
    assert scaled["name"] == "Chicken Alfredo"
    assert [ingredient["unit"] for ingredient in scaled["ingredients"]] == ["lb", "oz", "cups"]


def test_scale_recipe_rounds_to_two_decimals():
    recipe = {"name": "Rice", "servings": 3, "ingredients": [{"name": "rice", "quantity": 1, "unit": "cup"}]}
    scaled = scale_recipe(recipe, 2)
    assert scaled["ingredients"][0]["quantity"] == 0.67


def test_scale_recipe_does_not_change_original(alfredo):
    scale_recipe(alfredo, 8)
    assert alfredo["servings"] == 4
    assert [ingredient["quantity"] for ingredient in alfredo["ingredients"]] == [1.5, 12, 2]


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
