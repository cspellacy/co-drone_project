from codrone_edu.drone import *
from Files import color_Main, Rick_Roll, Take_Off

drone = Drone()
drone.pair()

color_Main.play(drone)
Take_Off.play(drone)
time.sleep(10)
Rick_Roll.play(drone)
time.sleep(30)
drone.disconnect()
