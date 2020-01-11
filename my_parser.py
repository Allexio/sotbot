import sot_interaction as inter

def parser(command):
    if command.startswith(" "):
        command = command[1:]
    if "where is" in command:
        return inter.object_searcher(command.replace("where is ", ""))
    
    elif "where can I find" in command:
        command = command.replace(" a "," ").replace(" an ", " ").replace("snek", "snake")
        if " near " in command and "-" in command:
            coordinates = command.split(" near ")[1]
            return inter.animal_searcher(command.replace("where can I find ", ""), coordinates)
        else:
            return inter.animal_searcher(command.replace("where can I find ", ""))

    elif "add " in command:
        command = command.replace("add ", "")
        if " to " in command:
            args = command.split(" to ")
            return inter.add_info_to_island(args[1], args[0])
        else:
            return inter.add_island(command)
    
    elif command == "help":
        return help_print()

    elif command == "map":
        return inter.map_printer()

    elif command == "about":
        return about_print()

    return inter.island_searcher(command)

def help_print():
    help_message = """
    Sotbot is designed to help people chart their own maps of sea of thieves.
The database starts empty and as you go along, you can add more information to complete it.
    ```add [island name]```
        Adds a new island to the database
    ```add [pig/snake/chicken] to [island name]```
        Adds an animal type to an island already present in the database.
    ```add [coordinates] to [island name]```
        Adds coordinates to an island already present in the database.
    ```[island name]```
        Prints information about a specific island.
    ```map```
        Displays a map of currently discovered islands.
        O = Outpost/S = Seapost/F = Skeleton Fort/W = Wild island (everything else)\n
    """
    return help_message

def about_print():
    about_message = """
    This bot was made by Allexio#0001 in python 3. Feel free to request features or give (constructive) feedback @ x.allexio@gmail.com"""
    return about_message