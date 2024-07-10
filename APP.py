# 1. The drivers that the company has, their worker ID, their name, and their start city.
# 2. The cities that the company delivers to and where the driver can go from that city.

drivers = {
        "ID001" : {
            "name" : "Max Verstappen",
            "city" : "Akkar"
        },
        "ID002" : {
            "name" : "Charles Leclerc,",
            "city" : "Saida"
        },
        "ID003" : {
            "name" : "Linus",
            "city" : "Jbeil"
        }
    }




class WeDeliver:
    def __init__(self, user_input ,drivers):
        self.user_input = user_input
        print(user_input)

    
    if user_input == 1:
        x = drivers.items("name")
        print(x)


def print_display():
    print("1. To go to the drivers’ menu \n2. To go to the cities’ menu\n3. To exit the system")



print_display()
user_input = int(input(""))

WeDeliver(user_input)



