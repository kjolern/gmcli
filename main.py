import diceroller

def main():
    print("******************************************************")
    print("Welcome to gmcli, the cli tool for dnd 5e game masters")
    print("******************************************************")
    print("") 
    print("Menu")
    print("")
    print("1.Dice roller")
    print("")
    
    menuchoice = input("What would you like to access? Select a number from the list. ")
    if menuchoice == "1":
        diceroller.roller()
    else:
        main()
    

if __name__ == "__main__":
    main()
