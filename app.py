"""CPS 310 Recipe & Meal Planner starter application."""

from recipe_utils import (
    filter_by_category,
    load_config,
    load_recipes,
    scale_recipe,
    search_by_ingredient,
    search_by_name,
)


def display_recipe(recipe):
    """Display one recipe in a readable format."""
    print(f"\n{recipe['name']}")
    print("-" * len(recipe["name"]))
    print(f"Category: {recipe['category']}")
    print(f"Servings: {recipe['servings']}")
    print(f"Prep time: {recipe['prep_time']} minutes")
    print(f"Cook time: {recipe['cook_time']} minutes")
    print("Ingredients:")
    for ingredient in recipe["ingredients"]:
        print(f"- {ingredient['quantity']} {ingredient['unit']} {ingredient['name']}")


def list_recipes(recipes):
    """Display a numbered list of recipe names."""
    if not recipes:
        print("\nNo recipes found.")
        return

    print("\nRecipes")
    print("-------")
    for index, recipe in enumerate(recipes, start=1):
        print(f"{index}. {recipe['name']} ({recipe['category']})")


def select_recipe(recipes):
    """Prompt the user to pick a recipe. Return it, or None if the selection is invalid."""
    list_recipes(recipes)
    if not recipes:
        return None

    try:
        selection = int(input("\nEnter recipe number: "))
    except ValueError:
        print("Invalid selection.")
        return None

    if selection < 1 or selection > len(recipes):
        print("Invalid selection.")
        return None

    return recipes[selection - 1]


def choose_recipe(recipes):
    """Prompt the user to select and view a recipe."""
    recipe = select_recipe(recipes)
    if recipe is not None:
        display_recipe(recipe)


def scale_selected_recipe(recipes):
    """Prompt the user to pick a recipe and a new serving size, then show the scaled recipe."""
    recipe = select_recipe(recipes)
    if recipe is None:
        return

    try:
        new_servings = int(input(f"Enter new number of servings (currently {recipe['servings']}): "))
    except ValueError:
        print("Invalid servings. Please enter a whole number.")
        return

    if new_servings <= 0:
        print("Invalid servings. Please enter a number greater than 0.")
        return

    display_recipe(scale_recipe(recipe, new_servings))


def main():
    """Run the starter Recipe & Meal Planner."""
    config = load_config("config.json")
    recipes = load_recipes(config["recipe_file"])

    while True:
        print(f"\n{config['app_title']}")
        print("=" * len(config["app_title"]))
        print("1. List all recipes")
        print("2. Search recipes by name")
        print("3. Search recipes by ingredients")
        print("4. Filter recipes by category")
        print("5. View recipe details")
        print("6. Scale recipe servings")
        print("7. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            list_recipes(recipes)
        elif choice == "2":
            term = input("Enter recipe name: ").strip()
            list_recipes(search_by_name(recipes, term))
        elif choice == "3":
            term = input("Enter ingredient name: ").strip()
            list_recipes(search_by_ingredient(recipes, term))
        elif choice == "4":
            category = input("Enter category: ").strip()
            list_recipes(filter_by_category(recipes, category))
        elif choice == "5":
            choose_recipe(recipes)
        elif choice == "6":
            scale_selected_recipe(recipes)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-7.")


if __name__ == "__main__":
    main()
