# utility functions

import random as rnd

def _execute(userin, object_list, recipe_list)
    # pattern match to decide dispatch
    
    match userin:
        case "g": # create a recipe list
            generate_list(recipe_list, object_list)
        
        case "s": # generate an ingredient list
            shopping_list(recipe_list, object_list)

        case "b": # generate a book
            collate_recipes(recipe_list, object_list)

def generate_list(recipe_list, object_list)
    # takes an empty recipe list object and user prompts 

    # needs index of recipes, amount of recipes, and scaling

    nrecipes = input("How many recipes are needed? Input: ")

    selection = input("How would you like to select? Options rand/chosen: ")

    match selection:
        case: "rand"
           inds = rnd.sample(range(len(object_list)), selection) 
        case: "chosen"
            # display indexes
            inds = input()

    scaling = input("Scale the recipe by an integer? Default 1: ")
    if scaling == '':
        scaling = 1


    pull_scale(recipe_list, object_list, inds, scaling)

    return None

def pull_scale(recipe_list, object_list, inds, scaling)
    # takes the indices and available recipes and scales them

    for i in inds:
        new_object = deepcopy(object_list[i])
        for (keys, vals) in new_object.ingredients:
            new_object.ingredients[keys] = scaling * vals
        recipe_list.append(new_object)
