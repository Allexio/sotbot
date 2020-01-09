import sot_interaction as inter

def parser(command):
    if command.startswith(" "):
        command = command[1:]
    if "where is" in command:
        return inter.object_searcher(command.replace("where is ", ""))
    
    if "where can I find" in command:
        command = command.replace(" a "," ").replace(" an ", " ").replace("snek", "snake")
        if " near " in command and "-" in command:
            coordinates = command.split(" near ")[1]
            return inter.animal_searcher(command.replace("where can I find ", ""), coordinates)
        else:
            return inter.animal_searcher(command.replace("where can I find ", ""))

    if "add " in command:
        command = command.replace("add ", "")
        if " to " in command:
            args = command.split(" to ")
            return inter.add_info_to_island(args[1], args[0])
        else:
            return inter.add_island(command)
    return "couldn't recognise your command. :skull:"