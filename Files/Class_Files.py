from codrone_edu.drone import *


class movement_commands:
    def mv(drone: Drone):
        drone.move_forward(100, "cm", 0.50)

    def mv2(drone: Drone):
        drone.move_forward(150, "cm", 0.50)

    def up(drone: Drone):
        drone.set_throttle(50)
        drone.move(1.8)

    def up2(drone: Drone):
        drone.set_throttle(50)
        drone.move(1)

    def hvr(drone: Drone):
        drone.hover(2)

    def dwn(drone: Drone):
        drone.set_throttle(-0.50)
        drone.move(1)

    def bck(drone: Drone):
        drone.move_backward(100, "cm", 0.50)
        print("Turning Black")


class clr:
    def red(drone: Drone):
        drone.set_drone_LED(255, 0, 0, 100)
        print("Turning Red")

    def grn(drone: Drone):
        drone.set_drone_LED(0, 255, 0, 100)
        print("Turning Green")

    def blu(drone: Drone):
        drone.set_drone_LED(0, 0, 255, 100)
        print("Turning Blue")

    def wht(drone: Drone):
        drone.set_drone_LED(250, 250, 250, 100)
        print("Turning White")

    def blck(drone: Drone):
        drone.set_drone_LED(0, 0, 0, 100)
        print("Turning Black")


class segment:
    def takeoff(drone: Drone):
        clr.wht(drone)
        drone.takeoff()
        movement_commands.hvr(drone)

    def throughArch(drone: Drone):
        clr.red(drone)
        movement_commands.mv2(drone)
        time.sleep(5)
        clr.grn(drone)
        movement_commands.hvr(drone)

    def preKeyhole(drone: Drone):
        movement_commands.up(drone)
        movement_commands.hvr(drone)
        clr.blu(drone)

    def returnToTakeoff(drone: Drone):
        movement_commands.hvr(drone)
        movement_commands.bck(drone)
        clr.wht(drone)
        movement_commands.hvr(drone)

    def land(drone: Drone):
        drone.land()
        clr.blck(drone)

    def keyhole(drone: Drone):
        movement_commands.mv(drone)
        movement_commands.hvr(drone)
        # time.sleep(2)

        # movement_commands.up2(drone)

        movement_commands.dwn(drone)

        movement_commands.bck(drone)
        drone.land()
