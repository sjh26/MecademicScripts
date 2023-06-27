import mecademicpy.robot as mdr
import time
robot = mdr.Robot()

def print_connected():
    print('Connected!')

callbacks = mdr.RobotCallbacks()
callbacks.on_connected = print_connected

robot.RegisterCallbacks(callbacks=callbacks, run_callbacks_in_separate_thread=True)
robot.Connect(address='192.168.0.100') # Will print 'Connected!' if successful.
time.sleep(5)