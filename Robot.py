import json

class RobotDB(object):
    def __init__(self, RobotDBtxt):
        self.file = RobotDBtxt

    def load_db(self):
        with open(self.file, "r") as f:
            return json.dumps(json.load(f))


if __name__=="__main__":
    robot = RobotDB("Robot_DB.txt")
    robot_db = robot.load_db()
    print(robot_db)

