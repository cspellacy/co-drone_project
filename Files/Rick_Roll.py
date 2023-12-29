from codrone_edu.drone import *

class NoteLength:
    dot_half = 1250
    half     = 1000
    dot_qtr  = 750
    qtr      = 500
    dot_8th  = 375
    eighth   = 250
    sxtnth   = 125

def dada(drone: Drone):
    drone.drone_buzzer(Note.D4, NoteLength.sxtnth)
    drone.drone_buzzer(Note.E4, NoteLength.sxtnth)
    drone.drone_buzzer(Note.G4, NoteLength.sxtnth)
    drone.drone_buzzer(Note.E4, NoteLength.sxtnth)

def play(drone: Drone):
    # first measure
    drone.drone_buzzer(Note.G4, NoteLength.dot_qtr)
    drone.drone_buzzer(Note.A4, NoteLength.dot_qtr)
    drone.drone_buzzer(Note.D4, NoteLength.qtr)

    # second measure
    drone.drone_buzzer(Note.A4, NoteLength.dot_qtr)
    drone.drone_buzzer(Note.B4, NoteLength.dot_qtr)
    drone.drone_buzzer(Note.D5, NoteLength.sxtnth)
    drone.drone_buzzer(Note.C5, NoteLength.sxtnth)
    drone.drone_buzzer(Note.B4, NoteLength.sxtnth)
    drone.drone_buzzer(Note.A4, NoteLength.sxtnth)

    #third measure
    drone.drone_buzzer(Note.G4, NoteLength.dot_qtr)
    drone.drone_buzzer(Note.A4, NoteLength.dot_qtr)
    drone.drone_buzzer(Note.D4, NoteLength.dot_half)
    time.sleep(.75)
    dada(drone)

    #fourth and fifth measure
    drone.drone_buzzer(Note.B4, NoteLength.dot_8th)
    drone.drone_buzzer(Note.B4, NoteLength.dot_8th)
    drone.drone_buzzer(Note.A4, NoteLength.dot_qtr)
    dada(drone)

    #sixth measure
    drone.drone_buzzer(Note.A4, NoteLength.dot_8th)
    drone.drone_buzzer(Note.A4, NoteLength.dot_8th)
    drone.drone_buzzer(Note.G4, NoteLength.dot_8th)
    drone.drone_buzzer(Note.FS4, NoteLength.sxtnth)
    drone.drone_buzzer(Note.E4, NoteLength.dot_8th)
    dada(drone)

    #seventh measure
    drone.drone_buzzer(Note.G4, NoteLength.qtr)
    drone.drone_buzzer(Note.A4, NoteLength.eighth)
    drone.drone_buzzer(Note.FS4, NoteLength.dot_8th)
    drone.drone_buzzer(Note.E4, NoteLength.sxtnth)
    drone.drone_buzzer(Note.D4, NoteLength.qtr)
    drone.drone_buzzer(Note.D4, NoteLength.eighth)

    #eigth measure
    drone.drone_buzzer(Note.A4, NoteLength.qtr)
    drone.drone_buzzer(Note.G4, NoteLength.half)
    dada(drone)

    #ninth measure
    drone.drone_buzzer(Note.B4, NoteLength.dot_8th)
    drone.drone_buzzer(Note.B4, NoteLength.dot_8th)
    drone.drone_buzzer(Note.A4, NoteLength.dot_qtr)
    dada(drone)

    #tenth measure
    drone.drone_buzzer(Note.D5, NoteLength.qtr)
    drone.drone_buzzer(Note.FS4, NoteLength.eighth)
    drone.drone_buzzer(Note.G4, NoteLength.dot_8th)
    drone.drone_buzzer(Note.FS4, NoteLength.sxtnth)
    drone.drone_buzzer(Note.E4, NoteLength.eighth)
    dada(drone)

    #eleventh measure
    drone.drone_buzzer(Note.G4, NoteLength.qtr)
    drone.drone_buzzer(Note.A4, NoteLength.eighth)
    drone.drone_buzzer(Note.FS4, NoteLength.dot_8th)
    drone.drone_buzzer(Note.E4, NoteLength.sxtnth)
    drone.drone_buzzer(Note.D4, NoteLength.qtr)
    drone.drone_buzzer(Note.D4, NoteLength.eighth)

    #12th measure
    drone.drone_buzzer(Note.A4, NoteLength.qtr)
    drone.drone_buzzer(Note.G4, NoteLength.half)