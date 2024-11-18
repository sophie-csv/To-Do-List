import json

def set_up():

    init_db = {

        "tasks": []
    }

    f = open('database.json', 'w')
    json.dump(init_db, f)
    f.close()

def write_to_db(data):
    f = open('database.json', 'r')
    json.dump(data, f)
    f.close()

def get_db_as_dict():
    f = open('database.json', 'r')
    data = json.load(f)
    f.close()
    return data

