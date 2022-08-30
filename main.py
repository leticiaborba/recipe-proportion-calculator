from recipe_manager import NewRecipe, ReadRecipe
from art import art
import os


def clear():
    os.system("cls")
    # os.system("clear") # change if not running from pc


def proportion_calculator(base_quantity, user_quantity):
    proportion = user_quantity / base_quantity
    return proportion


def recipe_calculator(recipe, proportion, ingredients_list, base_ingredient):
    for ingredient in ingredients_list:
        if ingredient != base_ingredient:
            ingredient_row = recipe.recipe_data().loc[recipe.recipe_data()["Ingredient"] == ingredient]
            ingredient_quantity = round(float(ingredient_row["Quantity"]) * proportion, 2)
            ingredient_unit = ingredient_row["Unit"].to_string(index=False).strip()
            print(f"  {ingredient}: {ingredient_quantity} {ingredient_unit}")


def main():
    clear()
    print(art)
    print("\n  This is a recipe proportion calculator, welcome.\n"
          "\n  Here you can create a new recipe,\n"
          "  save it for future use\n"
          "  or read an existing file.\n")
    while True:
        starter_input = input("  Do you want to fill in the ingredients\n"
                        "  or load a csv file? (use 'fill' or 'load')\n  ").lower()
        if starter_input == "fill":
            clear()
            recipe = NewRecipe()
            clear()
            break
        elif starter_input == "load":
            clear()
            recipe = ReadRecipe()
            clear()
            break
        else:
            print("        -- Invalid option, please try again. --\n")

    print("\n  From which ingredient do you want to base the proportion on?")
    ingredients = recipe.recipe_data()["Ingredient"].to_list()
    while True:
        base_ingredient = input(f"  {ingredients}: ").capitalize()
        if base_ingredient in ingredients:
            ingredient_row = recipe.recipe_data().loc[recipe.recipe_data()["Ingredient"] == base_ingredient]
            base_quantity = float(ingredient_row["Quantity"])
            base_unit = ingredient_row["Unit"].to_string(index=False).strip()
            break
        else:
            print("        -- Invalid ingredient, please try again. --")

    while True:
        try:
            user_quantity = float(input(f"\n  How much (in '{base_unit}') do you have of {base_ingredient}? "))
            break
        except ValueError:
            print("        -- Invalid quantity, please try again. --")

    proportion = proportion_calculator(base_quantity, user_quantity)
    print(f"\n  For {user_quantity} {base_unit} of {base_ingredient},\n  you'll need:")
    recipe_calculator(recipe, proportion, ingredients, base_ingredient)

    input("\n  Press enter to exit.")


main()