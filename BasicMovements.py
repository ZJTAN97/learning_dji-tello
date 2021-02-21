from djitellopy import tello
from time import sleep

drone = tello.Tello()
# Connect to the drone
drone.connect()
print(f'Battery:{drone.get_battery()}%')

# Always take off first
drone.takeoff()
# Set velocities
drone.send_rc_control(0, 5, 0, 0) # Move forward with speed 5 for 2 seconds
sleep(2) 
drone.send_rc_control(0, 0, 0, 0) 
drone.land()
