import PiTraffic
import time

SouthRed = PiTraffic.Traffic("SOUTH", "RED")
SouthYellow = PiTraffic.Traffic("SOUTH", "YELLOW")
SouthGreen = PiTraffic.Traffic("SOUTH", "GREEN")


EastRed = PiTraffic.Traffic("EAST", "RED")
EastYellow = PiTraffic.Traffic("EAST", "YELLOW")
EastGreen = PiTraffic.Traffic("EAST", "GREEN")

NorthRed = PiTraffic.Traffic("NORTH", "RED")
NorthYellow = PiTraffic.Traffic("NORTH", "YELLOW")
NorthGreen = PiTraffic.Traffic("NORTH", "GREEN")


WestRed = PiTraffic.Traffic("WEST", "RED")
WestYellow = PiTraffic.Traffic("WEST", "YELLOW")
WestGreen = PiTraffic.Traffic("WEST", "GREEN")

Buzz = PiTraffic.Buzzer()

# All direction RED LED ON
def AllRed():
    SouthRed.on()
    EastRed.on()
    NorthRed.on()
    WestRed.on()

AllRed()
       

try:
    while True:
        Buzz.on()
        time.sleep(0.2)
        Buzz.off()

        EastRed.off()
        EastYellow.on()
        time.sleep(1)
        EastYellow.off()
        EastGreen.on()
        time.sleep(2)
        EastGreen.off()
        EastRed.on()
        time.sleep(1)
 
        WestRed.off()
        WestYellow.on()
        time.sleep(1)
        WestYellow.off()
        WestGreen.on()
        time.sleep(2)
        WestGreen.off()
        WestRed.on()
        time.sleep(1)

        NorthRed.off()
        NorthYellow.on()
        time.sleep(1)
        NorthYellow.off()
        NorthGreen.on()
        time.sleep(2)
        NorthGreen.off()
        NorthRed.on()
        time.sleep(1)

        SouthRed.off()
        SouthYellow.on()
        time.sleep(1)
        SouthYellow.off()
        SouthGreen.on()
        time.sleep(2)
        SouthGreen.off()
        SouthRed.on()
        time.sleep(1)

except KeyboardInterrupt:
    PiTraffic.closeGPIO()
    
    
 
