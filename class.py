#Assignment 10.1 Create your own class
#By Elton Zeng
#The goal of the assignment is to create your own class and some methods of that class
class Fish():
    def __init__(self):
        #setting private data attributes
        self.__fin = 0
        #the fish should always be assumed to be alive and able to swim unless eaten 
        self.__alive = True
        self.__swim = True  
        self.__position = 0
        self.__speed = 0
        self.__size = 0
    #getters and setters
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
        else:
            self.__position = new_pos
    def get_position(self):
        return self.__position
    #set the number of fins for speed
    def set_fin(self, num_fins):
        self.__fin = num_fins 
    def get_fin(self):
        return self.__fin
    #set speed of fish
    def set_speed(self):
        #speed of the fish is based on the size and the number of fins
        self.__speed = self.get_size() + self.__speed + self.get_fin()  
    def get_speed(self):
        return self.__speed
    #set the status of the fish 
    def set_status(self, status):
        if status == True or status == False:
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
    def swim_forward(self):
        if self.getswim() == True and self.get_status() == True:
            self.__distance= self.get_position() + self.get_speed()
            self.set_position(self.__distance)
        else:
            print("The fish can't swim. Quite ironic.")
    def consume(self, food):
        #size value make it equal to zero and subtract the value 
        if self.get_size() > food.get_size(): 
            self.__incsize = self.get_size() + food.get_size()
            food.set_size(0)
            #the other fish is dead
            food.set_status(False)
            self.set_size(self.__incsize)
            print("The other fish was consumed.")
        else:
            food.set_size(self.get_size() + food.get_size())
            self.set_size(0)
            self.set_status(False)
        print(self.get_size())