# WeDeliver
Project : WE deliver


In your system, you should keep track of two things:
1. The drivers that the company has, their worker ID, their name, and their start city.
2. The cities that the company delivers to and where the driver can go from that city.

There are three main menus in the system. When the user runs the program, they are welcomed with
the first one which displays:
Hello! Please enter:
1. To go to the drivers’ menu
2. To go to the cities’ menu
3. To exit the system
Based on the user input, your system will either redirect them to the next menu, or exit.


DRIVERS’ MENU
In that menu, the user is greeted with the following options:
Enter:
1. To view all the drivers
2. To add a driver
3. To go back to main menu
View all drivers
A list of all the drivers and their detail is printed to the users
i.e.:
ID001, Max Verstappen, Akkar
ID002, Charles Leclerc, Saida
ID002, Lando Norris, Jbeil

Add a driver
The user is asked to enter the name and start city of the driver, the driver is then saved to the system.
The user does not input the ID of the driver, it is automatically generated by the system

The user might input an invalid start city, make sure that the start city is already available in the
database. If the city is not available, ask the user if they want to add it to the database, if yes,
you should do so.
Go back
This option takes the user back to the previous main menu.
CITIES’ MENU
In that menu, the user is given the following choices:
1. Show cities
2. Print neighboring cities
3. Print Drivers delivering to city
Show cities
Print a list with the name of all the cities in the program.
Print neighboring cities
Asks the user for a city name, and then prints all cities that can be reached from the user input.
Print Drivers delivering to city
Asks the users for a city name, and then prints all drivers that are delivering to this city. Drivers might
not have this city as their starting city, but they can reach it by going through different cities.

For example, if the user inputs Beirut, Both Max and Charles will be printed. But if the user inputs
Zahle, only Lando will be printed.

Hint:
There are functions called “Breadth First Search (BFS)” and “Depth First Search (DFS)”, you can look
them up and use them here. But you don’t have to.
Good luck and remember to divide and conquer :)