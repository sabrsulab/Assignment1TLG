import csv
def getPokeNum():
    pokenum=input(">")
    repeat = True
    while repeat == True:
        with open("pokedex.txt", "r") as pokedata:
            print(pokedata)
            for x in csv.DictReader(pokedata):
                pokedict = dict(x)
                if pokedict["#"]==pokenum:
                    print(f"\tName: {pokedict['Name']}\n\tType: {pokedict['Type 1']}\n\tStats:\n\t-------\n\tHP: {pokedict['HP']}\n\tATK: {pokedict['Attack']}\n\tDEF: {pokedict['Defense']}\n\tSP.DF.: {pokedict['Sp. Def']}\n\tSPD: {pokedict['Speed']}\n\t-------")
                    Response = input("Would you like to check for another pokemon?\t")
                    if Response in ["y","Y","Yes","yes"]:
                        pokenum=input(">")
                        repeat = True
                    else:
                        repeat = False
                        main()
                    
def getPokeGen():
    pokeGen=input(">")
    repeat = True
    while repeat == True:
        with open("pokedex.txt", "r") as pokedata:
            print(f"Generation {pokeGen}.")
            for x in csv.DictReader(pokedata):
                pokedict = dict(x)
                if pokedict["Generation"] == pokeGen:
                    print(f"{pokedict['#']}.\t{pokedict['Name']}.")
            Response = input("Would you like to get a list for another generation?\t")
            if Response in ["y","Y","Yes","yes"]:
                pokenum=input(">")
                repeat = True
            else:
                repeat = False
                main()
def getLegoPoke():
    with open("pokedex.txt", "r") as pokedata:
        for x in csv.DictReader(pokedata):
            pokedict = dict(x)
            if pokedict["Legendary"] == "True":
                print(f"{pokedict['#']}\t{pokedict['Name']}")
        Response = input("Would you like to recheck for legendaries?\t")
        if Response in ["y","Y","Yes","yes"]:
            
            getLegoPoke()
        else:
            main()
def main():
    print("Please select from the following options:")

    selection = int(input("\n\t> 1. Get Pokemon by Number.\n\t> 2. Get Pokemon by generation.\n\t> 3. Get only legendary pokemon."))
    if selection in [1,2,3]:
        if selection == 1:
            getPokeNum()
        elif selection == 2:
            getPokeGen()
        elif selection == 3:
            getLegoPoke()
        else:
            print("Thanks for playing")
main()
