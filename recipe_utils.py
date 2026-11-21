"""Utility functions for the Recipe & Meal Planner."""

import json


def load_config(filename):
    """Load application configuration from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def load_recipes(filename):
    """Load recipe data from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def search_by_name(recipes, search_term):
    """Return recipes whose names contain the search term."""
    search_term = search_term.lower()
    return [
        recipe
        for recipe in recipes
        if search_term in recipe["name"].lower()
    ]

def search_by_ingredient(recipes, search_term):
    """Return recipes whose ingredients contain the search term."""
    search_term = search_term.lower()
    return [
        recipe
        for recipe in recipes
            if any(search_term in ingredient["name"].lower()
                for ingredient in recipe["ingredients"])
    ]

def filter_by_category(recipes, category):
    """Return recipes that match the requested category."""
    category = category.lower()
    return [
        recipe
        for recipe in recipes
        if recipe["category"].lower() == category
    ]


def scale_recipe(recipe, new_servings):
    """Return a copy of the recipe with ingredient quantities scaled to new_servings.

    Quantities are rounded to 2 decimal places. The original recipe is not changed.
    """
    scale_factor = new_servings / recipe["servings"]
    scaled_ingredients = [
        {**ingredient, "quantity": round(ingredient["quantity"] * scale_factor, 2)}
        for ingredient in recipe["ingredients"]
    ]
    return {**recipe, "servings": new_servings, "ingredients": scaled_ingredients}
