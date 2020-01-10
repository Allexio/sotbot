import ast

def object_searcher(object_name):
    pass

def animal_searcher(animal, coordinates=None):
    if animal not in ["pig", "snake", "chicken"]:
        return "Did not recognise animal. :skull:"
    data = load_data()
    search_results = {}
    for island in data:
        if island["type"] == "wild":
            if island["animals"][animal]:
                search_results[island["name"]] = island["location"]["coordinates"]
    if coordinates is None:
        return "You can find " + animal + "s on " + clean_list(search_results.keys())
    return search_results
            
def island_searcher(island_name):
    """ returns all available info about the island given as arg """
    data = load_data()
    for island in data:
        if island["name"].upper() == island_name.upper():
            island_type = island["type"]
            coordinates = island["location"]["coordinates"]
            region = island["location"]["region"]
            NPCs = island["NPCs"]
            if island_type == "wild":
                pigs = island["animals"]["pig"]
                chicken = island["animals"]["chicken"]
                snake = island["animals"]["snake"]
            type_pronoun = "a "
            if island_type == "outpost":
                type_pronoun = "an "
            if island_type == "wild": island_type = "wild island"
            pretty = island["name"] + " is " + type_pronoun + island_type
            if region is not None:
                pretty += " in " + region
            if coordinates is not None:
                pretty += " located at " + coordinates
            pretty += "."
            if island_type == "wild island":
                pretty += "\n"
                if pigs or snake or chicken:
                    pretty += "You can find "
                    animal_list = []
                    if pigs:
                        animal_list.append("pigs")
                    if snake:
                        animal_list.append("snakes")
                    if chicken:
                        animal_list.append("chicken")
                    pretty += clean_list(animal_list).replace(".", " on this island.")
                else:
                    pretty += "There are no animals on this island."
            return pretty
    return "Couldn't find matching island."


def add_island(island_name):
    """ adds given island to database with proper type based on name suffix """
    if "Couldn't" in island_searcher(island_name):
        return "The island you are trying to add already exists. :skull:"
    fort_types = ["fort", "fortress", "keep", "stronghold", "watchtower", "camp"]
    seapost_types = ["store", "emporium", "bazaar", "Spoils", "traders", "trading post", "seapost"]
    suffix = island_name.split()
    if suffix[len(suffix)-1] in fort_types:
        island_type = "fort"
    elif suffix[len(suffix)-1] in seapost_types:
        island_type = "seapost"
    elif "outpost" in island_name:
        island_type = "outpost"
    else:
        island_type = "wild"
    data = load_data()

    if island_type != "wild":
        data.append({
            "name": island_name,
            "location":{
                "region": None,
                "coordinates": None,
            },
            "NPCs": [],
            "type": island_type,
            "is_charted": True,
        })
    else:
        data.append({
            "name":island_name,
            "location":{
                "region":None,
                "coordinates":None,
            },
            "NPCs": [],
            "animals":{
                "snake": False,
                "chicken": False,
                "pig": False,
            },
            "type": "wild",
            "is_charted": True,
        },)
    write_data(data)
    return island_type + " island added!"

def add_info_to_island(island_name, info):
    data = load_data()
    if "-" in info:
        for index, island in enumerate(data):
            if island["name"] == island_name:
                data[index]["location"]["coordinates"] = info
                write_data(data)
                return "data updated successfully!"
        return "The island mentioned could not be found."
    elif info in ["pig", "snake", "chicken"]:
        for index, island in enumerate(data):
            if island["name"] == island_name:
                if island["type"] != "wild":
                    return "There are no animals on " + island["type"]+"s."
                data[index]["animals"][info] = True
                write_data(data)
                return "data updated successfully!"
        return "The island mentioned could not be found."
    return "Couldn't add that info to an island."



def load_data():
    with open("data/sot_island_data", "r") as file:
        raw_data = file.read()
    return ast.literal_eval(raw_data)

def clean_list(python_list):
    clean_list = ""
    for index, item in enumerate(python_list):
        if index == len(python_list)-1:
            clean_list += item + "."
        elif index == len(python_list)-2:
            clean_list += item + " and "
        else:
            clean_list += item + ", "
    return clean_list

def write_data(data):
    with open("data/sot_island_data", "w") as file:
        file.write(str(data))