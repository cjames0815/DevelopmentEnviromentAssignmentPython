from tv import *

def main():
    tv1 = tv(1,1, False)
    print(tv1)
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)
    print(tv1)

    tv2 = tv(1, 1, False)
    print(tv2)
    tv2.turnOn()
    tv2.channelUp()
    tv2.channelUp()
    tv2.channelUp()
    tv2.channelDown()
    tv2.volumeUp() 
    tv2.volumeUp() 
    tv2.volumeUp()
    tv2.volumeDown()
    print(tv2)
    tv2.turnOff()
    print(tv2)

    channel = input("Please enter a channel (between 1 -120):")
    volume = input("Please enter a volume(betwenn 1 and 7):")
    tv3 = tv(int(channel), int(volume), True)
    print(tv3) 


if __name__ == "__main__":
    main()