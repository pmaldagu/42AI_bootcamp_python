import datetime
from book import Book
from recipe import Recipe

a = Recipe("haha", "1", "10",["salad", "soup"], "disgusting thing", "lunch")

b = Recipe("lol", "2", "15", ["pain", "canard"], "thing machin", "lunch")

r_lst = {
        'starter': {},
        'lunch': {'haha': a},
        'dessert': {}
        }

#to_print = str(a)
#print(to_print)

book = Book("book", datetime.date, datetime.date, r_lst)
book.get_recipe_by_name("lo")
book.get_recipes_by_types("lunch")
book.add_recipe(b)
book.get_recipe_by_name("lol")
