class Recipe:
    def __init__(self, name, lvl, time, ingredients, description, rtype):
        try:
            self.name = str(name)
            self.cooking_lvl = int(lvl)
            self.cooking_time = int(time)
            self.ingredients = list(ingredients)
            self.description = str(description)
            self.recipe_type = str(rtype)
        except ValueError as ve:
            print(f"Invalid integer: {ve.args[0][ve.args[0].find(': ')+2: ]}")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "Recipe name is {0}\nThe cooking level is {1}\nIt take {2} minutes to cook\nThe ingredients is {3}\nDescription: {4}\nIt's a {5}\n".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type)
        return txt

