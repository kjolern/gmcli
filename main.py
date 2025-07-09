import diceroller
import flora

def main():
    while True:
        print("******************************************************")
        print("Welcome to gmcli, the cli tool for dnd 5e game masters")
        print("******************************************************")
        print("") 
        print("Menu")
        print("")
        print("1.Dice roller")
        print("2.Flora")
        print("3.Exit")
        print("")
        
        menuchoice = input("What would you like to access? Select a number from the list. ")
        if menuchoice == "1":
            diceroller.roller()
        
        elif menuchoice == "2":
            flora.menu()

        elif menuchoice == "3":
            print("Thank you for using gmcli.")
            exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
