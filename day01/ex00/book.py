class Book:
    def __init__(self, name, lst_update, cre_date, r_lst):
        self.name = name
        self.last_update = lst_update
        self.creation_date = cre_date
        self.recipes_list = r_lst

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for key, val in self.recipes_list.items():
            for rkey, rname in val.items():
                if name == rkey:
                    print(str(rname))
                    return
        print("No {0} recipe\n".format(name))

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for key, val in self.recipes_list.items():
            if key == recipe_type:
                for key1, val1 in val.items():
                    print(str(val1))
                    return
        print("No recipe of this type")

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        for key, val in self.recipes_list.items():
            if key == recipe.recipe_type:
                self.recipes_list[key][recipe.name] = recipe
