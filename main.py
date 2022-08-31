from recipe_manager import NewRecipe, ReadRecipe
from art import art
import os
from prettytable import PrettyTable


def clear():
    os.system("cls")
    # os.system("clear") # <- change to this if not running from pc


def proportion_calculator(base_quantity, user_quantity):
    proportion = user_quantity / base_quantity
    return proportion


def recipe_calculator(recipe, proportion, ingredients_list, base_ingredient):
    output_data = []
    for ingredient in ingredients_list:
        if ingredient != base_ingredient:
            ingredient_row = recipe.recipe_data().loc[recipe.recipe_data()["Ingredient"] == ingredient]
            ingredient_quantity = round(float(ingredient_row["Quantity"]) * proportion, 2)
            ingredient_unit = ingredient_row["Unit"].to_string(index=False).strip()
            output_data.append([ingredient, ingredient_quantity, ingredient_unit])
    return output_data


def prettify_recipe(recipe_name, base_ingredient, final_quantity, base_unit, output_recipe):
    pretty_recipe = PrettyTable()
    pretty_recipe.padding_width = 1
    pretty_recipe.title = f'"{recipe_name}"'
    pretty_recipe.align = "r"
    pretty_recipe.field_names = ["Ingredient", "Quantity", "Unit"]
    pretty_recipe.align["Ingredient"] = "l"
    pretty_recipe.add_row([base_ingredient, final_quantity, base_unit])
    for ingredient in output_recipe:
        pretty_recipe.add_row(ingredient)
    for row in pretty_recipe.get_string().splitlines():
        print("  " + row)


def main():
    is_calc_running = True
    while is_calc_running:
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

        print("\n  What is the ingredient that you want to base the proportion on?")
        ingredients = recipe.recipe_data()["Ingredient"].to_list()
        while True:
            base_ingredient = input(f"  {ingredients}: ").capitalize()
            if base_ingredient in ingredients:
                ingredient_row = recipe.recipe_data().loc[recipe.recipe_data()["Ingredient"] == base_ingredient]
                base_quantity = float(ingredient_row["Quantity"])
                base_unit = ingredient_row["Unit"].to_string(index=False).strip()
                break
            else:
                print("        -- Invalid ingredient, please try again. --\n")

        while True:
            try:
                user_quantity = float(input(f"\n  How much (in '{base_unit}') do you have of {base_ingredient}? "))
                break
            except ValueError:
                print("        -- Invalid quantity, please try again. --")

        proportion = proportion_calculator(base_quantity, user_quantity)
        output_recipe = recipe_calculator(recipe, proportion, ingredients, base_ingredient)
        print(f"\n  Thank you, here it is:")
        prettify_recipe(recipe.name, base_ingredient, user_quantity, base_unit, output_recipe)

        while True:
            continue_input = input("\n  Enjoy your recipe!"
                                "\n  Do you want to try another one? (y/n) ").lower()
            if continue_input == "y":
                break
            elif continue_input == "n":
                is_calc_running = False
                break
            else:
                print("        -- Invalid option, please try again. --")


main()