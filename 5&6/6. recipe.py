'''a program that implements a recipe management system using two classes: 'recipe' to represent 
individual recipes and 'recipebook' to manage a collection of recipes; it allows users to add new
recipes and view all recipes through a menu-driven interface.'''

# represents a single recipe with its details
class Recipe():
    def __init__(self, id, name, ingredients, description):
        self.id = id
        self.name = name
        self.ingredients = ingredients 
        self.description = description

    # prints a formatted report of the recipe's details.
    def recipe_report(self):
        print(f"\n--- recipe: {self.name} ---")
        print(f"id: {self.id}")
        print("ingredients:")
        for ingredient in self.ingredients:
            print(f"  - {ingredient}") # format each ingredient
        print("description:")
        print(f"  {self.description}") 

# manages a collection of recipe objects
class RecipeBook:
    # initializes an empty recipe book.
    def __init__(self):
        self.recipes = [] # list to store recipe objects

    # adds a new recipe object to the recipe book
    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        print(f"\nrecipe '{recipe.name}' added successfully!")

    # displays details of all recipes in the book.
    def view_all_recipes(self):
        if not self.recipes:
            print("\nyour recipe book is empty. please add a recipe first.")
            return # exit if no recipes
            
        print("\n========== your recipe book ==========")
        for recipe in self.recipes:
            recipe.recipe_report() # call recipe's report method
        print("\n======================================")

def main():
    my_recipe_book = RecipeBook() # create an instance of recipebook

    while True: # main menu loop
        print("\n--- recipe book menu ---")
        print("1. add a new recipe")
        print("2. view all recipes")
        print("3. exit")
        
        choice = input("enter your choice (1-3): ")

        if choice == '1':
            # collect new recipe details from user
            print("\nplease enter the details for the new recipe:")
            recipe_id = input("recipe id: ")
            recipe_name = input("recipe name: ")
            
            ingredients_list = [] # collect ingredients in a list
            print("enter ingredients (press enter on empty line to finish):")
            while True:
                ingredient = input("  ingredient: ")
                if not ingredient: # break loop if input is empty
                    break
                ingredients_list.append(ingredient)

            recipe_description = input("enter the recipe description: ")
            
            # create new recipe object and add to book
            new_recipe = Recipe(recipe_id, recipe_name, ingredients_list, recipe_description)
            my_recipe_book.add_recipe(new_recipe)

        elif choice == '2':
            my_recipe_book.view_all_recipes() # display all recipes

        elif choice == '3':
            print("\nhappy cooking! goodbye.")
            break # exit main loop
            
        else:
            print("\ninvalid choice. please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
