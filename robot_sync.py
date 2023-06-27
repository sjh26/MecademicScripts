import mecademicpy.robot as mdr
robot = mdr.Robot()
robot.Connect(address='192.168.0.100', enable_synchronous_mode=True)
robot.ActivateAndHome()

robot.MoveJoints(0, 0, 0, 0, 0, 0)
robot.MoveJoints(0, -60, 60, 0, 0, 0)

# The returned robot position will be (0, -60, 60, 0, 0, 0), because this line will only be executed once MoveJoints(0, -60, 60, 0, 0, 0) has completed.
print(robot.GetJoints())

robot.DeactivateRobot()
robot.Disconnect()