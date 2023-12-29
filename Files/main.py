from codrone_edu.drone import *
from Files import color_Main

drone = Drone()
drone.pair()

while True:
    color_Main.play(drone)
