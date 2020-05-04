class RobotInfo:

    def __init__(self):
        print("ROBOT INFORMATION")
    def setName(self, robotName):
        self.robotName = robotName
    
    def introduceRobot(self):
        print("My name is "+self.robotName)


class OwnerInfo:
    def __init__(self):
        print("OWNER INFORMATION")

    def setOwnerName(self,ownerName):
        self.ownerName = ownerName

    def setRobotOwned(self, robot):
        self.robot = robot
    
    def introduceOwner(self):
        print("My name is "+self.ownerName+ ",I owned "+self.robot+" the robot")

r = RobotInfo()

r.setName("Charles")
r.introduceRobot()

p = OwnerInfo()

p.setOwnerName("Pedro")
p.setRobotOwned(r.robotName)

p.introduceOwner()