import main
import random

#placeholder tbales, will change.
flora_tables = {
    "arctic": [
        ("Oak Tree", (1, 30)),
        ("Blueberry Bush", (31, 50)),
        ("Fern", (51, 75)),
        ("Mushroom", (76, 100))
    ],
    "coastal": [
        ("Willow Tree", (1, 20)),
        ("Reed", (21, 50)),
        ("Water Lily", (51, 75)),
        ("Moss", (76, 100))
    ],
    "desert": [
        ("Cactus", (1, 40)),
        ("Sagebrush", (41, 70)),
        ("Aloe Vera", (71, 90)),
        ("Desert Grass", (91, 100))
    ],
    "forest": [
        ("Cactus", (1, 40)),
        ("Sagebrush", (41, 70)),
        ("Aloe Vera", (71, 90)),
        ("Desert Grass", (91, 100))
    ],"grassland": [
        ("Cactus", (1, 40)),
        ("Sagebrush", (41, 70)),
        ("Aloe Vera", (71, 90)),
        ("Desert Grass", (91, 100))
    ],"mountain": [
        ("Cactus", (1, 40)),
        ("Sagebrush", (41, 70)),
        ("Aloe Vera", (71, 90)),
        ("Desert Grass", (91, 100))
    ],"swamp": [
        ("Cactus", (1, 40)),
        ("Sagebrush", (41, 70)),
        ("Aloe Vera", (71, 90)),
        ("Desert Grass", (91, 100))
    ],"underground": [
        ("Cactus", (1, 40)),
        ("Sagebrush", (41, 70)),
        ("Aloe Vera", (71, 90)),
        ("Desert Grass", (91, 100))
    ]
}

def list_flora(biotope):
    if biotope not in flora_tables:
        print("Invalid biotope.")
        return
    print(f"Available flora in {biotope}:")
    for flora, rng in flora_tables[biotope]:
        print(f"- {flora} (roll {rng[0]}-{rng[1]})")

def roll_flora(biotope):
    if biotope not in flora_tables:
        print("Invalid biotope.")
        return
    roll = random.randint(1, 20)
    for flora, rng in flora_tables[biotope]:
        if rng[0] <= roll <= rng[1]:
            print(f"You rolled {roll}: {flora}")
            return
    print("No flora found for this roll.")

def menu():
    while True:
        print("******************************")
        print("Menu")
        print("1. Roll for flora in a biotope")
        print("2. List available flora in a biotope")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            print("Available biotopes:", ", ".join(flora_tables.keys()))
            biotope = input("Enter biotope: ").lower()
            roll_flora(biotope)
        elif choice == "2":
            print("Available biotopes:", ", ".join(flora_tables.keys()))
            biotope = input("Enter biotope: ").lower()
            list_flora(biotope)
        elif choice == "3":
            print("Exiting.")
            main.main()
        else:
            print("Invalid choice.")
