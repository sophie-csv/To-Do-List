import json

def set_up():

    init_db = {

        "tasks": []
    }

    f = open('database/tasklist_DB.json', 'w')
    json.dump(init_db, f)
    f.close()


def write_to_db(data):
    f = open('database/tasklist_DB.json', 'w')
    json.dump(data, f)
    f.close()


def get_db_as_dict():
    f = open('database/tasklist_DB.json', 'r')
    data = json.load(f)
    f.close()
    return data


def add_task(user, task):
    data = get_db_as_dict()
    data[user]['tasks'].append(task)
    write_to_db(data)
def get_tasks(user):
    data = get_db_as_dict()
    return data[user]['tasks']

def remove_task(user, task):
    data = get_db_as_dict()
    data[user]['tasks'].remove(task)
    write_to_db(data)

def get_users_as_list():
    data = get_db_as_dict()
    return list(data)
