import ast

def object_searcher(object_name):
    pass

def animal_searcher(animal, coordinates=None):
    print(animal)
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
            


def add_island(island_name, region_name=None):
    fort_types = ["fort", "fortress", "keep", "stronghold", "watchtower", "camp"]
    seapost_types = ["store", "emporium", "bazaar", "spoils", "traders", "trading post", "seapost"]
    for fort_type in fort_types:
        if fort_type in island_name:
            return add_fort(island_name)
    for seapost_type in seapost_types:
        if seapost_type in island_name:
            return add_seapost(island_name)
    if "outpost" in island_name:
        return add_outpost(island_name)    
    pass

def add_outpost(island_name):
    pass
def add_seapost(island_name):
    pass
def add_fort(island_name):
    pass

def add_info_to_island(island_name, info):
    pass

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