import mecademicpy.robot as mdr
import time

robot = mdr.Robot()
robot.Connect(address='192.168.0.100', enable_synchronous_mode=False)
robot.ActivateAndHome()


robot.MoveJoints(0, 0, 0, 0, 0, 0)
robot.MoveJoints(0, -60, 60, 0, 0, 0)

for _ in range(100):
    print(robot.GetJoints())
    time.sleep(0.05)

robot.WaitIdle()
robot.DeactivateRobot()
robot.Disconnect()