
import sys
tissues=50

print ("Do you want to open the tissue box?")
voice1=input()
if voice1 == "yes":
    print("You opened the tissue box.")
    print("----------")
else:
    if voice1 == "no":
        print("You never dared to open the box, who knows, maybe you will regret it, maybe it is for the better.")
        sys.exit()

while tissues>0:
    print ("Do you want to take a tissue?")
    voice=input()
    if voice == "yes":
        tissues-=1
        print("----------")
        print("You took a tissue.")
        print("There are currently",tissues,"tissues.")
        print("----------")

    if voice == "no" and tissues == 50:
        print("You found your old opened tissue box, so you opened it for nothing.")
        sys.exit()
    if voice == "no" and tissues == 49:
        print("You've caused WW3.")
        sys.exit()
    if voice == "no" and tissues == 48:
        print("You got alergy to water.")
        sys.exit()
    if voice == "no" and tissues == 47:
        print("You've cured cancer.")
        sys.exit()
    if voice == "no" and tissues == 46:
        print("You started feeling hungry.")
        sys.exit()
    if voice == "no" and tissues == 45:
        print("You got a lightsaber.")
        sys.exit()
    if voice == "no" and tissues == 44:
        print("You became blind.")
        sys.exit()
    if voice == "no" and tissues == 43:
        print("ThE VoIcEs FiNaLy DisSaPeArEd.")
        sys.exit()
    if voice == "no" and tissues == 42:
        print("huh nothing happened, is this the good ending?")
        sys.exit()
    if voice == "no" and tissues == 41:
        print("You died alone.")
        sys.exit()
    if voice == "no" and tissues == 40:
        print("The exploded, that is.. interesting.")
        sys.exit()
    if voice == "no" and tissues == 39:
        print("89 more lines to go (You broke the fourth wall).")
        sys.exit()
    if voice == "no" and tissues == 38:
        print("You fell off your chair.")
        sys.exit()
    if voice == "no" and tissues == 37:
        print("You didn't fell of your chair.")
        sys.exit()
    if voice == "no" and tissues == 36:
        print("You got cancer (unfortunate).")
        sys.exit()
    if voice == "no" and tissues == 35:
        print("You started feeling hungry.")
        sys.exit()
    if voice == "no" and tissues == 34:
        print("You changed timeline where forsen never beat and never will beat the childrens' game. D R E A D")
        sys.exit()
    if voice == "no" and tissues == 33:
        print("You got cure for future a disease, but it never even started.")
        sys.exit()
    if voice == "no" and tissues == 32:
        print("hi.")
        sys.exit()
    if voice == "no" and tissues == 31:
        print("You became invisible for 2 seconds.")
        sys.exit()
    if voice == "no" and tissues == 30:
        print("You can shoot small water stream from your fingers.")
        sys.exit()
    if voice == "no" and tissues == 29:
        print("You get to watch your favorite movie for the first time again.")
        sys.exit()
    if voice == "no" and tissues == 28:
        print("You get to learn to play one musical instrument you want.")
        sys.exit()
    if voice == "no" and tissues == 27:
        print("You blinked.")
        sys.exit()
    if voice == "no" and tissues == 26:
        print("You win an eating constest, but then you die of hearth attack.")
        sys.exit()
    if voice == "no" and tissues == 25:
        print("You find the perfect girl, but then you hear an alarm.")
        sys.exit()
    if voice == "no" and tissues == 24:
        print("...")
        sys.exit()
    if voice == "no" and tissues == 23:
        print("You can eat glass without any consequences.")
        sys.exit()
    if voice == "no" and tissues == 22:
        print("Your hair grew by 1 day.")
        sys.exit()
    if voice == "no" and tissues == 21:
        print("You found a dollar on the ground, but.. nothing happened.")
        sys.exit()
    if voice == "no" and tissues == 20:
        print("You get bored.")
        sys.exit()
    if voice == "no" and tissues == 19:
        print("Did you expected something?.")
        sys.exit()
    if voice == "no" and tissues == 18:
        print("You can charge devices with your tongue.")
        sys.exit()
    if voice == "no" and tissues == 17:
        print("You never smell bad again.")
        sys.exit()
    if voice == "no" and tissues == 16:
        print("Number 65 is interesting.")
        sys.exit()
    if voice == "no" and tissues == 15:
        print("There isn't anything actually interesting here.")
        sys.exit()
    if voice == "no" and tissues == 14:
        print("Number 65 is interesting.")
        sys.exit()
    if voice == "no" and tissues == 13:
        print("You turned blue")
        sys.exit()
    if voice == "no" and tissues == 12:
        print("You are the best dancer, but can't stand people watching you.")
        sys.exit()
    if voice == "no" and tissues == 11:
        print("Your hair rotated by 180 degrees, weird...")
        sys.exit()
    if voice == "no" and tissues == 10:
        print("You teleported to the place you were at 30 minutes ago .")
        sys.exit()
    if voice == "no" and tissues == 9:
        print("You get hyped up.")
        sys.exit()
    if voice == "no" and tissues == 8:
        print("You can stay at home today.")
        sys.exit()
    if voice == "no" and tissues == 7:
        print("You can change your nationaity once.")
        sys.exit()
    if voice == "no" and tissues == 6:
        print("Nothing to see here.")
        sys.exit()
    if voice == "no" and tissues == 5:
        print("Number 65 is interesting.")
        sys.exit()
    if voice == "no" and tissues == 4:
        print("You can travel to the worst place on Earth for free.")
        sys.exit()
    if voice == "no" and tissues == 3:
        print("You die the day before the release of GTA VI.")
        sys.exit()
    if voice == "no" and tissues == 2:
        print("You talk like a gangster for 12 hours.")
        sys.exit()
    if voice == "no" and tissues == 1:
        print("You stand up on you own.")
        sys.exit()
    if tissues == 0:
        print("You used the whole box... what now.")
        sys.exit()