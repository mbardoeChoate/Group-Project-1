from drivetrain import Drivetrain
from shooter import Shooter
from odometry import Odometry


class Robot:

    def __init__(self):
        self.subsystems=[]

    def robotInit(self):
        self.drivetrain = Drivetrain(0.127, )
        self.shooter = Shooter()
        self.odometry = Odometry()
        self.subsystems.append(self.drivetrain)
        self.subsystems.append(self.shooter)
        self.subsystems.append(self.odometry)



    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def update(self):
        for subsystem in self.subsystems:
            subsystem.update()
