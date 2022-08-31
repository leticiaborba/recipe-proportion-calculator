from ingredients import Ingredient
import pandas


class NewRecipe:

    def __init__(self):
        self.name = self.name_input()
        self.number_of_ingredients = int(input("  How many ingredients? "))
        print(f"\n  Now for each ingredient of {self.name}\n"
                "  fill in it's name, quantity and unit of measure:")
        self.ingredients_list = self.ingredients()
        self.recipe_data()
        self.save()

    def name_input(self):
        recipe_name = input("\n  What is the name of your recipe? ").title()
        return recipe_name

    def ingredients(self):
        ingredients_list = []
        for i in range(self.number_of_ingredients):
            ingredient = Ingredient()
            name = ingredient.name
            quantity = ingredient.quantity
            unit = ingredient.unit
            ingredients_list.append((name, quantity, unit))
        return ingredients_list

    def recipe_data(self):
        recipe = pandas.DataFrame(self.ingredients_list, columns=["Ingredient", "Quantity", "Unit"])
        return recipe

    def save(self):
        save_recipe = input("\n  Do you want to save this recipe? (y/n) ").lower()
        if save_recipe == "y":
            recipe = self.recipe_data()
            recipe.to_csv(f"{self.name}.csv")
            print(f"        -- Recipe saved to your path as {self.name}.csv --")
            input("  Press enter to continue.")
        else:
            pass


class ReadRecipe:

    def __init__(self):
        while True:
            try:
                self.recipe_path = input("\n  What is the path to your file? ")
                self.recipe_data()
                break
            except pandas.errors.EmptyDataError:
                print("        -- Recipe is empty, please try another file. --")
            except (FileNotFoundError, pandas.errors.ParserError, ValueError):
                print("        -- Recipe not found, please try again. --")

    def recipe_data(self):
        recipe = pandas.read_csv(f"{self.recipe_path}")
        return recipe




