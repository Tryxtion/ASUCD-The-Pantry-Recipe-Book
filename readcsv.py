import csv, re

def processInput(rawUserInput): # process the raw user input (a string) to get the ingredients list they want
    userInputList = []
    for ingr in rawUserInput.strip().split():
        if ingr[-1].isalpha():
            userInputList.append(ingr.lower())
        else:
            userInputList.append(ingr[:-1].lower())
    return userInputList

def fullList():
    full=[]
    with open('Pantry Recipes Spreadsheet Data - Sheet1.csv', mode='r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            full.append(row["Recipe "])
    return full

def containsIngredient(userIngr, recipeIngr):
    # userIngr is a string, recipeIngr is a string
    # Checks whether an ingredient is in a recipe

    # get rid of plurality
    if userIngr[len(userIngr)-1]=='s':
        userIngr = userIngr[:len(userIngr)-1]
        if userIngr[len(userIngr)-1]=='e':
            userIngr = userIngr[:len(userIngr)-1]

    
    if userIngr.lower() in recipeIngr.lower():
        return True

def getRecipes(rawUserInput): 
    # Accepts a string, parses into a list, and returns available recipes
    # parse user input into a list
    userInput = processInput(rawUserInput)

    # parse csv
    with open('Pantry Recipes Spreadsheet Data - Sheet1.csv', mode='r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        headers = csv_reader.fieldnames # Get headers of the columns

        for i in range(len(headers)): # clean up headers
            headers[i]=headers[i].strip()
        
        availableRecipes = []
        for row in csv_reader:
            ingredients = []
            for item in userInput:
                if containsIngredient(item, row["Ingredient(s) at The Pantry"]):
                    ingredients.append(item)
            
            if ingredients!=[]:           
                availableRecipes.append(row['Recipe'])
    return availableRecipes


def getData(recipeName, dataName):
    # Takes in the name of the recipe and the data that is wanted. Either "Ingredients" or "Preparation"
    # Returns a list of either the ingredients or the step by step instructions depending on what was requested
    with open('Pantry Recipes Spreadsheet Data - Sheet1.csv', mode='r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        headers = csv_reader.fieldnames # Get headers of the columns

        for i in range(len(headers)): # clean up headers
            headers[i]=headers[i].strip()
        for row in csv_reader:
            if row['Recipe']==recipeName:
                data = row[dataName]
                data = row[dataName]
    
    data = data.split("\n")
    for i in range(len(data)):
        data[i] = data[i].strip()
    data = [s for s in data if s]
    print(data)
    return data
