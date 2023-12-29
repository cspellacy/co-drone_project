from Class_Files import *


def play(drone: Drone):
    # This is where the drone takes off!
    print("Drone Takes Off")
    segment.takeoff(drone)
    # Drone hovers for two seconds to calibrate, drone turns red

    # Start of movement through arch, drone turns red
    print("Drone Moves Through Arch")
    segment.throughArch(drone)
    # End of movement through arch, getting ready for keyhole, drone turns green

    # Start of up movement, getting ready for keyhole, drone turns green
    print("Drone Gets up to Height for Keyhole")
    time.sleep(0.2)
    segment.preKeyhole(drone)
    # Drone at height for keyhole, drone turns blue

    segment.keyhole(drone)


""""   # Drone returns to previous takeoff spot(supposed to anyway)
   print("Drone Returns to Takeoff")
   time.sleep(0.2)
   segment.returnToTakeoff(drone)
   # End of movement, drone turns white


#Drone Lands and End of Code, drone turns black
  print("Drone Lands")
   time.sleep(0.2)
   """