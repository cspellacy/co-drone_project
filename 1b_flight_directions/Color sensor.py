from codrone_edu.drone import *
drone = Drone()
Drone.pair()
#Importing library codrone_edu and the module drone!

drone.start_drone_buzzer(Note.A1, 1000)
drone.sleep(500)
drone.start_drone_buzzer(Note.B1, 1000)
drone.sleep(500)
drone.start_drone_buzzer(Note.C1, 1000)

drone.print(PUGSloveCheatos)
drone.disconnect()