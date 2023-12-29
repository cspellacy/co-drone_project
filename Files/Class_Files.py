from codrone_edu.drone import *


class movement_commands:
    def mv_pre_keyhole(self: Drone):
        self.move_forward(100, "cm", 0.50)

    def mv_Go_Through_Keyhole(self: Drone):
        self.move_forward(150, "cm", 0.50)

    def up(self: Drone):
        self.set_throttle(50)
        self.move(1.8)

    def up2(self: Drone):
        self.set_throttle(50)
        self.move(1)

    def hvr(self: Drone):
        self.hover(2)

    def dwn(self: Drone):
        self.set_throttle(-0.50)
        self.move(1)

    def bck(self: Drone):
        self.move_backward(100, "cm", 0.50)
        print("Turning Black")

class clr:
    def red(self: Drone):
        self.set_drone_LED(255, 0, 0, 100)
        print("Turning Red")

    def grn(self: Drone):
        self.set_drone_LED(0, 255, 0, 100)
        print("Turning Green")

    def blu(self: Drone):
        self.set_drone_LED(0, 0, 255, 100)
        print("Turning Blue")

    def wht(self: Drone):
        self.set_drone_LED(250, 250, 250, 100)
        print("Turning White")

    def blck(self: Drone):
        self.set_drone_LED(0, 0, 0, 100)
        print("Turning Black")

class segment:
    def takeoff(self: Drone):
        clr.wht(self)
        self.takeoff()
        movement_commands.hvr(self)

    def throughArch(self: Drone):
        clr.red(self)
        movement_commands.mv_Go_Through_Keyhole(self)
        time.sleep(5)
        clr.grn(self)
        movement_commands.hvr(self)

    def preKeyhole(self: Drone):
        movement_commands.up(self)
        movement_commands.hvr(self)
        clr.blu(self)

    def returnToTakeoff(self: Drone):
        movement_commands.hvr(self)
        movement_commands.bck(self)
        clr.wht(self)
        movement_commands.hvr(self)

    def land(self: Drone):
        self.land()
        clr.blck(self)

    def keyhole(self: Drone):
        movement_commands.mv_pre_keyhole(self)
        movement_commands.hvr(self)
        # time.sleep(2)

        # movement_commands.up2(drone)

        movement_commands.dwn(self)

        movement_commands.bck(self)
        self.land()
