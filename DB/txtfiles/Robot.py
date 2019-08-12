import json

class DB(object):
    def __init__(self):
        pass

    def load_db(self, file):
        with open(file, "r") as f:
            return json.dumps(json.load(f))

if __name__=="__main__":
    database = DB()
    robot_db = database.load_db("DB/txtfiles/Robot_DB.txt")
    print(robot_db)

    map_db = database.load_db("DB/txtfiles/map.txt")
    print(map_db)