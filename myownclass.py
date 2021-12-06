#Mason Hall
#Assignment 10.1: Your Own Class
#The point of this assignment is to create your own class and have methods to help create it.
#I used StackOverflow for help.

'''
So the goal of this assignment for me,
is to create a bird watching system where 
the user enters a bird that they encountered on a trip
in a specific species (i.e. owl, eagle, hawk, woodpecker)
and after this discussion, the user must identify the breed 
that the species is (i.e. snowy owl, screech owl, barn owl)
and the system will return it. 
'''

#Class BirdDesciption
class BirdDescription:
    #Define __init__ with numerous variables while keeping them private.
    def __init__(self, __species, size,  color, appearance):
        self.__species = __species #private
        self.__size = size #private
        self.__color = color #private
        self.__appearance = appearance #private
        self.__size(size)
        self.__color(color)
        self.__appearance(appearance)
    # getter method
    def get_species(self):
        return self.__species
    # setter method
    def set_species(self, grax):
        #Prompt user for input
        grax = input("What species did you see? ")
        #Owl input
        if grax == "owl" or "owl":
            return
        #Eagle input
        elif grax == "eagle" or "Eagle":
            return
        #Songbird input
        elif grax == "songbird" or "Songbird":
            return
        #If not any, return this
        else:
            print("That is not one of the birds in question. Please try again.")
        #Return species
        self.__species = grax
    #Sets the species
    def SpeciesFinder(self, __species):
        self.set_species(self, __species)


class OwlQuiz(BirdDescription):
    #Define __init__ with numerous variables while keeping them private.
    def __init__(self, size, color, appearance):
        self.__size = size
        self.__color = color
        self.__appearance = appearance
        self.__size(size)
        self.__color(color)
        self.__appearance(appearance)
    #Set species Owl version
    def set_speciesOWL(self, grax):
        self.set_species()
        grax = input("What species did you see? ")
        #If statement for owl
        if grax == "owl" or "Owl":
            #Returns text
            print("You saw an owl? Those are so cool!")
            #Asks question
            size = input("Would you say it was big or small? ")
            #great horned owl = 3.2 lbs, great gray owl = 2.5lbs
            if size == "big" or size == "Big":
                #Color if statement as second question
                color = input("Okay, what color was it? ")
                if color == "brown" or "Brown":
                    #Tell them its Great Horned Owl
                    print("The owl you spotted was a Great Horned Owl! Gosh, I wish I'd seen it!")
                elif color == "gray" or "Gray":
                    #Tell them its Great Gray Owl
                    print("The owl that you saw was a Great Gray Owl! Those are magnificient!")
                else:
                    #Incorrect input
                    print("That's what I asked for, please try again.")
            #barred owl = 1.6 lbs, spotted owl = 1.5 lbs,  barn owl = 1.4 lbs, western screech owl = 0.4 lbs, and northern pygmy owl = 0.15 lbs
            elif size == "small" or size == "Small":
                #Barred Owl == white, Spotted Owl, and Northern Pygmy Owl == brown, Barn Owl == tan, Western Screech Owl = gray 
                color = input("Okay, what color was it? ")
                #If statement for owl
                if color == "white" or color == "White":
                    print("The owl you saw was a Barred Owl.")
                #If statement for owl
                if color == "brown" or color == "Brown":
                    print("Okay, one last question.")
                    print("Did it have yellow or black eyes?")
                    #Spotted Owl = black eyes, and Northern Pygmy Owl = yellow eyes
                    appearance = input("Just answer with the color please: ")
                    if appearance == "yellow" or "Yellow":
                        #Northern Pygmy Owl
                        print("The owl you saw was a Northern Pygmy Owl!")
                    elif appearance == "black" or "Black":
                        #Spotted Owl
                        print("The owl that you saw was a Spotted Owl!")
                    else:
                        #Else statement
                        print("That is not what I asked for, please try again.")
                #Tan color
                elif color == "tan" or "Tan":
                    print("The owl you saw was a Barn Owl! Those are so cute!")
                #Gray color
                elif color == "gray" or "Gray":
                    print("The owl you saw was a Western Screech Owl! So pretty!")
                else:
                    print("That's not what I asked for, please try again.")
            else:
                print("That's not what I asked, please try again.")
        else:
            return
    
class EagleQuiz(BirdDescription):
    #Define __init__ with numerous variables while keeping them private.
    def __init__(self, size, color, appearance):
        self.__size = size
        self.__color = color
        self.__appearance = appearance
        self.__size(size)
        self.__color(color)
        self.__appearance(appearance)
    #Set species Eagle version
    def set_speciesEAGLE(self, grax):
        #Set_species
        self.set_species()
        #Question input
        grax = input("What species did you see? ")
        #If statement
        if grax == "eagle" or "Eagle":
            #Eagle statement
            print("You saw an eagle? Those are scary!")
            size = input("Would you say it was big or small? ")
            #White-tailed eagle == 8ft, Golden eagle == 7.7ft, Bald eagle == 7.5ft, Phillipine eagle == 7.3ft
            if size == "Big" or "big":
                print("Okay, next question.")
                color = input("What color were its tail feathers? Brown or white?")
                #Golden eagle, Phillipine eagle = brown
                if color == "brown" or "Brown":
                    print("Okay, final question.")
                    print("")
                #White-tailed eagle, Bald eagle == white
                elif color == "white" or "White":
                    print("Okay, final question.")
                    appearance = input("What was the color of its head? Brown or white: ")
                    #white-tailed eagle == brown
                    if appearance == "brown" or "Brown":
                        print("The eagle that you saw was a White-tailed eagle!")
                    #bald eagle == white
                    elif appearance == "white" or "White":
                        print("The eagle that you saw was a bald eagle! Those are so rare!")
                    else:
                        print("That's not what I asked, please try again.")
                else:
                    print("That's not what I asked, please try again.")
            #Black kite == 5ft, Red-tailed hawk == 4.8ft
            elif size == "Small" or "small":
                color = input("Okay, what color was its tail? Red or brown? ")
                #red-tailed hawk == red
                if color == "red" or "Red":
                    print("The eagle you saw was a Red-Tailed Hawk! They are still considered to be eagles though.")
                elif color == "brown" or "Brown":
                    print("The eagle you saw was a Black Kite! Those are super cool!")
            else:
                print("That's not what I asked, please try again.")
        else:
            return

class SongbirdQuiz(BirdDescription):
    #Define __init__ with numerous variables while keeping them private.
    def __init__(self, size, color, appearance):
            self.__size = size
            self.__color = color
            self.__appearance = appearance
            self.__size(size)
            self.__color(color)
            self.__appearance(appearance)
    #Songbird function
    def set_speciesSONGBIRD(self, grax):
        #Set species
        self.set_species()
        #Input
        grax = input("What species did you see? ")
        if grax == "sonbid" or "Songbird":
            #Statemnt
            print("Okay, you saw a songbird? That's great!")
            size = input("Would you say it was big or small? ")
            #Blue jay == 3.8 oz, Common starling == 3.6 oz, American robin == 2.7 oz, Northern mockingbird == 1.8 oz, Northern cardinal == 1.5 oz, Eastern bluebird == 1.2 oz 
            if size == "Big" or "big":
                print("Okay, next question. What was the color?")
                color = input("Was it red, blue, gray, or black? ")
                #Northern Cardinal == red
                if color == "red" or "Red":
                    print("The songbird that you saw was the Northern Cardinal! Those are the prettiest birds I've ever seen!")
                #Blue jay, Eastern bluebird == blue
                elif color == "blue" or "Blue":
                    print("Okay, final question.")
                    print("What was the color of its belly?")
                    appearance = input("Orange or white? ")
                    #Blue jay = white
                    if appearance == "white" or "White":
                        print("The songbird that you saw was a Blue Jay! So cool!")
                    #Eastern bluebird == orange
                    elif appearance == "Orange" or "orange":
                        print("The songbird that you saw was an Eastern bluebird! They are so magnificient!")
                    else:
                        print("That is not what I asked, please try again.")
                #Northern mockingbird == gray
                elif color == "gray" or "Gray":
                    print("The songbird that you saw was a Northern Mockingbird.")
                #Common starling, American robin == black
                elif color == "black" or "Black":
                    print("Okay, final question.")
                    print("What was the color of its belly?")
                    appearance = input("Orange or black? ")
                    #American robin == Orange
                    if appearance == "Orange" or "orange":
                        print("The songbird that you saw was the American Robin!")
                    #Common starling == Black
                    elif appearance == "black" or "Black":
                        print("The songbird that you saw was the Common Starling!")
                    else:
                        print("That is not what I asked, please try again.")
                else:
                    print("That is not what I asked, please try again.")
            #Common nightingale == 0.69 oz, American Goldfinch == 0.48 oz, American yellow warbler == 0.36 oz, Eurasian blue tit == 0.36 oz, Eurasian wren = 0.32 oz
            elif size == "Small" or "small":
                print("Okay, next question. What was the color?")
                color = input("Was it brown, yellow, or blue? ")
                #Common nightingale, Eurasian wren == brown
                if color == "Brown" or "brown":
                    print("Okay, final question.")
                    appearance = input("Was it ball shaped? Yes or no: ")
                    #Eurasian wren == yes
                    if appearance == "yes" or "Yes":
                        print("The songbird you saw was an Eurasian Wren!")
                    #Common nightingale == no
                    elif appearance == "No" or "no":
                        print("The songbird you saw was a Common Nightingale!")
                    else:
                        print("That is not what I asked, please try again.")
                #American Goldfinch, American yellow warbler == yellow
                elif color == "Yellow" or "yellow":
                    print("Okay, final question.")
                    appearance = input("Was it ball shaped? Yes or no: ")
                    #American yellow warbler == yes
                    if appearance == "yes" or "Yes":
                        print("The songbird you saw was an American Yellow Warbler!")
                    #American Goldfinch == no
                    elif appearance == "No" or "no":
                        print("The songbird you saw was an American Goldfinch! So cute!")
                    else:
                        print("That is not what I asked, please try again.")           
                #Eurasian blue tit == blue
                elif color == "Blue" or "blue":
                    print("The bird that you saw was the Eurasian Blue Tit! They are so cute!")
                else:
                    print("That's not what I asked, please try again.")
            else:
                print("That's not what I asked, please try again.")
        else:
                return

#Main function
def main():
    #Main function story
    print("\nToday, you and I are going to go bird watching. Could you tell me your name before we continue?\n")
    #Input username
    username = input("")
    print(f"\n{username}... I like the ring of it! What birds are you wanting to see? Wait, don't tell me. We'll find out.")
    print("\nWe are traversing through a thick forest, it's noon, so we will have a lot of time to see some birds! I'm so excited!")
    print("\nOkay, let me get my notepad out... it'll be just one second...\n")
    print("\nWHOOOSH!!!!\n\n")
    print("Wait... did a bird just fly overhead? I was just getting my notepad too!\n")
    print(f"Wait, {username}! You saw the bird right? Could you tell me what it was?\n")
    print("It doesn't matter if you don't know what specific breed it is, just tell me what it looks like! I'm an expert!\n")
    print("Alright so first thing's first. Was the bird an owl, eagle, or songbird? Those are the only birds that inhabit this area.\n")
    print("Please make sure to tell me one or the other, nothing else!")
    #Set species function through Class
    BirdDescription.set_species()
    #Get species function through Class
    BirdDescription.get_species()
    #Set_species function through Owl Class
    OwlQuiz.set_speciesOWL()
    #Set_species function through Eagle Class
    EagleQuiz.set_speciesEAGLE()
    #Set_species function through Songbird Class
    SongbirdQuiz.set_speciesSONGBIRD()
    #Last statement
    print(f"Okay, {username}, that was a lot of fun!")

#If name == main
if __name__ == "__main__":
    main()