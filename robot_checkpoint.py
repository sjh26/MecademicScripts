import mecademicpy.robot as mdr
robot = mdr.Robot()
robot.Connect(address='192.168.0.100', enable_synchronous_mode=True)
robot.ActivateAndHome()


robot.MoveJoints(0, -60, 60, 0, 0, 0)
robot.MoveJoints(0, 0, 0, 0, 0, 0)
checkpoint_1 = robot.SetCheckpoint(1)

checkpoint_1.wait(timeout=10) # A timeout of 10s is set to avoid infinite wait in case of error.
print('The MoveJoints() motions are complete.')

robot.WaitIdle()
robot.DeactivateRobot()
robot.Disconnect()