# CustomClass

Github repo: https://github.com/EltZ36/CustomClass

CLASS DOCUMENTATION

The class is a class based on a fish and it has some traits such as being able to swim back, swim forward, and being able to eat another fish. The attributes are the name, the number of fins, if it is alive, can it swim, the position of the fish, the speed of the fish, and the size of the fish. The name is a requirement for the fish class when you are making an instance of the class. 

Class/Data attributes: 

Constructor: 
self.__name  The name of the fish and it is taken when you create an instance of a class 
self.__fin  The number of fins on the fish and helps determine the speed of the fish
self.__alive  Boolean that is either True or False and is used to make whether or not a fish can do certain methods such as eating or swimming 
self.__swim  Boolean that is either True or False and determines whether or not a fish can swim 
self.__position The position (int) of the fish at the given time
self.__speed  The speed of the fish and is determined by the user, fins, and the size of the fish
self.__size  The size of the fish and is used to see if a fish can eat another fish 

swim_forward & swim_back method:
self.__distance stores the distance between self.__position and self.__speed and for swim_forward, adds self.__position and self.__speed together while swim_back subtracts the position and the speed. 

consume method:
self.__incsize stores the sum of the size of the food fish and the current fish that is trying to eat the food. It is then used to set the size of the current fish or the food fish depending on which fish is bigger. Example: The current fish is a size of 5 while the food fish is 2. self.__incsize will be 7 and set the current fish size to 7. 

Methods:

get/set methods:

*since this is oop, you don't need to put self in the parameter when calling these methods 

set_name(self, name) takes in a string and sets self.__name to that string 
returns/prints nothing

get_name(self) returns the name of the fish class as a string. Requires no arguments to work. 

set_fin(self, num_fins) takes in an int and sets self.__fin equal to num_fins 
returns/prints nothing

get_fin(self) returns the number of fins the fish has as an int. Requires no arguments to work. 


set_size(self, size) takes in an int and sets self.__size equal to size and the size must be greater than zero or else a ValueError is raised. 

get_size(self) takes in no arguments and returns the size of the fish as an int. 

set_position(self, new_pos) takes in an int and sets self.__position equal to new_pos 
raises valueError if the new_pos is less than zero
prints out an f string saying that you can't move a dead fish if the fish is dead 

get_position(self) returns the position of the fish as an int and requires no arguments to work.

set_speed(self, speed) takes in an int and sets self.__speed to speed plus the size of the fish along with the fins of the fish. Raises a ValueError if the speed is less than zero. 

get_speed(self) takes in no arguments and returns the speed of the fish as an int 

set_status(self, status) takes in a bool (True or False) and sets self.__alive to it.

get_status(self) takes in no arguments and returns self.__alive (bool) 

set_swim(self, status) takes in a bool (True or False) and sets self.__swim to it. 

get_swim(self) take sin no agruments and returns self.__swim (bool)


OTHER METHODS:

swim_forward(self, num_secs): 
Checks if the fish is alive and able to swim first. After that, it counts up to num_secs via time.sleep in a for loop. It will add the position of the fish with the speed until the for loop stops and it returns an f string with the position of the fish. The number of seconds in printed out in the for loop to make it easier to see. A valueError will be raised if the position of the fish is less than zero. 

If the fish is not able to swim but is alive, then an f string saying the fish can't swim will be returned. 

Otherwise, the fish is dead and an f string that says the fish is dead is returned.  

For example, swim_forward(3) will count to 3 seconds and print out the seconds. The position of the fish will be returned in the function and must be printed in order to get the result.

swim_back(self, num_secs):
Checks if the fish is alive and able to swim first. After that, it counts up to num_secs via time.sleep in a for loop. It will subtract the position of the fish with the speed until the for loop stops and it returns an f string with the position of the fish. The number of seconds in printed out in the for loop to make it easier to see. A valueError will be raised if the position of the fish is less than zero. 

If the fish is not able to swim but is alive, then an f string saying the fish can't swim will be returned. 

Otherwise, the fish is dead and an f string that says the fish is dead is returned.  

For example, swim_forward(5) will count to 5 seconds and print out the seconds. The position of the fish will be returned in the function and must be printed in order to get the result.

consume(self, food): 
Takes in another fish object as a parameter and uses get.size() to compare it to the current fishes' size. Returns a different f string depending on the cases detailed below:

Case 1:
If the size of the food fish is smaller, than the current fish will then eat the fish with the size of the food fish and the current fish being added together. The size of the current fish will be set to the new sum with set_size(). The size of the food fish will turn to 0, the status of the fish will become false, and the swim of the fish will become false. 
It will then return a f string that says that the fish was successful in eating the food fish and it displays the current size of the fish. 

Case 2:
If the size of the food fish is the same, then both fish will survive and a f string is returned saying that the current fish is unalbe to eat the other fish as it is the same size. 

Case 3:
If the fish is dead, then it cannot eat other fish and a f string is returned saying that the fish is unable to eat the food fish as it is dead. 

Case 4:
Otherwise, the food fish will eat the current fish as the size is bigger. The size of the current fish will be 0, the status of the current fish will be false, and the swim of the fish will become false. The size of the fish will be added together and the new size will be set via set_size() with the sum. A f string will be returned where it says that the current fish was eaten by the food fish and it will display the size of the food fish.

DEMO PROGRAM DOCUMENTATION:
What happens in the demo program is that it prints out the results of the class methods and some of the test cases where the fish is dead or is trying to eat a fish that is a bigger size than it. It will wait in real time to display the results of the fish going forward and you should expect to wait 3 seconds for the results in the terminal.

HOW TO RUN PROGRAM: 
Requires Python 3.0 or higher. Run the .py file on windows powershell or an idle like Pycharm or Repl.it. There is no need to pip install the time module as it is already built in.
