import random

class Random_Number:
    def __init__(self, num_from, num_to):
        self.num_from=num_from
        self.num_to=num_to
        self.num_randomized=0

    def switcher(self):
        if self.num_from > self.num_to:
            self.num_from, self.num_to = self.num_to, self.num_from
            print("""
            --------------------------------------------------
            ERROR: INCORRECT INPUT
            Unable to randomize if a<b.
            Don't worry though I switched the numbers for you.
            --------------------------------------------------
            """)
            
    def randomizer(self):
        self.num_randomized = random.randint (self.num_from, self.num_to)

    def __str__(self):
        return f"{self.num_randomized}"

print("Do you want to randomize a number or choose from a list?")
choice=input().lower()
if choice=="number" or choice=="numbers":
    print("What numbers do you want to randomize?")
    try:
        num_from=int(input("From:"))
        num_to=int(input("To:"))
    except ValueError:
        print("""
        --------------------------------------------------
        ERROR: STRING DETECTED
        Unable to put string when interger was expected.
        Stopped program.
        --------------------------------------------------
        """)
        exit()
    random_num=Random_Number(num_from, num_to)
    random_num.switcher()
    random_num.randomizer()
    print(random_num)

elif choice=="list" or choice=="text":
    print("poggo")
else:
    print("idiot")