cookbook = {
    'sandwich' : {
            'ingredients' : {'ham', 'bread', 'cheese', 'tomato'},
            'meal' : 'lunch',
            'prep_time' : '10'
            },
    'cake' : {
            'ingredients' : {'flour', 'sugar', 'eggs'},
            'meal' : 'desert',
            'prep_time' : '60'
            },
    'salad' : {
            'ingredients' : {'avocado', 'arugula', 'tomatoes', 'spinach'},
            'meal' : 'lunch',
            'prep_time' : '15'
            }
        }

while True:
    print("please select an option by typing the corresponding number:")
    print("1 : Add a recipe")
    print("2 : Delete a recipe")
    print("3 : Print a recipe")
    print("4 : Print the cookbook")
    print("5 : Quit")
    a = input(">>>")
    if a == '5':
        print('\n')
        print("cookbook closed.")
        break
    elif a == '4':
        print("list of recipe\n")
        for key, val in cookbook.items():
            print("{:-^20}".format(key))
    elif a == '3':
        print("Wich recipe?")
        recipe = input(">>>")
        for key, val in cookbook.items():
            if key == recipe:
                print("Recipe for:", key, end="\n")
                print("ingredient liste : {}\nTo be eaten for {}\nTakes {} min of cooking.".format(*val))
    elif a == '2':
        print("Wich reciped do you want to delete?")
        recipe = input(">>>")
        if recipe in cookbook
            del cookbook[recipe]
        else:
            print("\nThis recipe doesn't existe\n")

    elif a == '1':
        print("wich recipe do you want to create?")
        recipe_name = input(">>>")
        ingredients = []
        while True:
            ingredient = input("ingredient to add (type 1 to stop adding ingredient) : ")
            if ingredient.isdigit() and int(ingredient) == 1:
                break
            elif len(ingredient) is 0:
                print("Cannot add if ingredient is empty")
                continue
            ingredients.append(ingredient)
        print("When do you want to eat it?")
        meal = input(">>>")
        print("How long does it takes to cook it (in minutes)")
        prep_time = input(">>>")
        cookbook[recipe_name] = {'ingredients' : ingredients, 'meal' :meal, 'prep_time' : prep_time}
        print(cookbook[recipe_name])
    else:
        print("It's simple no, I juste ask you tu type a number between 1 and 5, please try again")
