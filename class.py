#Assignment 10.1 Create your own class
#By Elton Zeng
#The goal of the assignment is to create your own class and some methods of that class
#import time for timer
import time 
class Fish():
    def __init__(self,name):
        #setting private data attributes
        self.__name = name 
        self.__fin = 0
        #the fish should always be assumed to be alive and able to swim unless eaten 
        self.__alive = True
        self.__swim = True  
        self.__position = 0
        self.__speed = 0
        self.__size = 0
    #getters and setters
    #set a new name if you want
    def set_name(self, new_name):
        self.__name = new_name
    #return the name of the fish 
    def get_name(self):
        return self.__name
    def set_size(self, new_size):
        #size cannot be negative 
        if new_size < 0:
            raise ValueError("Size cannot be less than zero")
        else:
            self.__size = new_size
    def get_size(self):
        return self.__size 
    #set the position and get the position
    def set_position(self, new_pos):
        #position cannot be negative 
        if new_pos < 0:
            raise ValueError("Position cannot be less than zero")
        elif self.get_status() == False:
            #return an f string that says you can't move the dead fish 
            print(f"Unable to move dead fish {self.get_name()}.")
        else:
            self.__position = new_pos
    def get_position(self):
        return self.__position
    #set the number of fins for speed
    def set_fin(self, num_fins):
        if num_fins < 0:
            raise ValueError("Fins cannot be less than zero")
        else:
            self.__fin = num_fins 
    def get_fin(self):
        return self.__fin
    #set speed of fish
    def set_speed(self,speed):
        if speed < 0:
            raise ValueError("Speed cannot be less than zero")
        else:
            #speed of the fish is based on the size and the number of fins
            self.__speed = self.get_size() + speed + self.get_fin()  
    def get_speed(self):
        return self.__speed
    #set the status of the fish 
    def set_status(self, status):
        if status == True or status == False:
            #if it is true, then the fish is alive, otherwise, it is dead
            self.__alive = status 
    def get_status(self):
        return self.__alive
    #make sure that the fish can swim 
    def set_swim(self, status):
        if status == True or status == False:
            self.__swim = status
    def get_swim(self):
        return self.__swim
    #other functions 
    def swim_forward(self, num_secs):
        #if it can swim and the fish is alive then move forward
        if self.get_swim() == True and self.get_status() == True:
            #make the for loop start the count from 1 instead of 0 
            for i in range(1, num_secs+1):
                #use time.sleep to stall the program and count out the seconds
                time.sleep(i)
                #Add together the position of the fish with the speed of the fsih
                self.__distance = self.get_position() + self.get_speed()
                #set the position of the fish to the newer distance
                self.set_position(self.__distance)
                #print out the seconds
                print(f'{i} seconds')
            #return the f string with the results of the end of moving and the name of the fish
            return f'The current position of {self.get_name()} is {self.get_position()}.'
        #otherwise, just say the fish can't swim
        elif self.get_swim() == False and self.get_status() == True:
            return f"{self.get_name()} can't swim. Quite ironic."
        #and if the get_status is false, the fish is dead and can't do anything
        else:
            return f"Unable to swim as {self.get_name()} is dead. :("

    def swim_back(self, num_secs):
        #if it can swim and the fish is alive then move forward
        if self.get_swim() == True and self.get_status() == True:
            for i in range(1, num_secs+1):
                time.sleep(i)
                #subtract the distance by the speed
                self.__distance = self.get_position() - self.get_speed()
                #set the position and make sure that it isn't negative
                self.set_position(self.__distance)
                 #print out the seconds
                print(f'{i} seconds')
            #return an f string with the position of the fish and the name of it 
            return f'The current position of {self.get_name()} is {self.get_position()}.'
        #otherwise, just say the fish can't swim
        elif self.get_swim() == False and self.get_status() == True:
            return f"{self.get_name()} can't swim. Quite ironic."
        #and if the get_status is false, the fish is dead and can't do anything
        else:
            return f"Unable to swim as {self.get_name()} is dead. :("

    #pass through another fish object into this method 
    def consume(self, food):
        #if the size of the fish is greater than the size of the other fish (food), then eat it
        if self.get_size() > food.get_size() and self.get_status() == True: 
            #add the size of the fish and the one it is eating together
            self.__incsize = self.get_size() + food.get_size()
            #the size of the food fish is 0 cuz it just got eaten
            food.set_size(0)
            #the other fish is dead
            food.set_status(False)
            self.set_size(self.__incsize)
            #return the f string saying that this fish ate the food and the size of the fish now
            return f'{self.get_name()} has successfully eaten {food.get_name()} and the size of {self.get_name()} is now {self.get_size()}.'
        #if the size of the fish is equal, then it will be unsuccessful and both fish will still be alive
        elif self.get_size() == food.get_size() and self.set_status() == True:
            return f'{self.get_name()} is unable to eat {food.get_name} as it is the same size.'
        #in case the user tries to get a dead fish to eat some other fish.
        elif self.get_status() == False:
            return f'{self.get_name()} is dead and cannot eat {food.get_name()}.'
        #otherwise, the food will eat the other fish due to size difference
        else:
            #add the size of the food fish to the fish that first tried to eat it
            food.set_size(self.get_size() + food.get_size())
            #this fish got eaten and is now dead
            self.set_size(0)
            #this fish is now dead
            self.set_status(False)
            self.set_swim(False)
            #return the f string saying that the food ate the other fish and the size of the food fish now
            return f'Oh no, {food.get_name()} has eaten {self.get_name()} and size of {food.get_name()} is now {food.get_size()}.'
    
    #displays all the info of the fish 
    def display(self):
        print(f'Name: {self.get_name()}')
        print(f'Size: {self.get_size()}')
        print(f'Number of fin(s): {self.get_fin()}')
        print(f'Speed: {self.get_speed()}')
        if self.get_status() == True:
            print("Status: Alive")
        else:
            print("Status: Dead")
        if self.get_swim() == True:
            print("Can Swim")
        else:
            print("Can't Swim")
        print(f'Position: {self.get_position()}')

def main():
    #testing code 
    fish1 = Fish("Clownfish")
    fish2 = Fish('Robert')
    fish3 = Fish("Barracuda")
    fish4 = Fish("Tuna")
    #setting the stats of fish1 
    fish1.set_size(10)
    fish1.set_fin(2)
    fish1.set_speed(3)
    fish1.set_status(True)
    print(fish1.swim_forward(1))
    #set the stats of the second fish that will be eaten 
    fish2.set_size(5)
    #show the results of fish1 eating fish2
    print(fish1.consume(fish2))
    #show that fish2 can't go forward because it is dead
    print(fish2.swim_forward(3))
    #display the info of fish1
    fish1.display()
    #show what happens when the food fish eats the one that wants to eat it
    #set up the size of the fish
    fish3.set_size(50)
    fish4.set_size(90)
    print(fish3.consume(fish4))
    #print out the case where a dead fish tries to eat something
    print(fish3.consume(fish2))
    print(fish3.set_position(3))
    

if __name__ == "__main__":
    main()