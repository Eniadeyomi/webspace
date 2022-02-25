# the client interface
from Vehicle import *


# creating a class client
class Client(Vehicle_Interface):

    def __init__(self, ref=None, make=None, model=None, km=None, numPassenger=None, number_doors=None, num_beds=None,
                 plate_number=None, daily_cost=None, weekly_cost=None, weekend_cost=None, available=None, car=None,
                 van=None, caravan=None):
        super().__init__(ref=ref, make=make, model=model, km=km, numPassenger=numPassenger, number_doors=number_doors,
                         num_beds=num_beds, plate_number=plate_number, daily_cost=daily_cost, weekly_cost=weekly_cost,
                         weekend_cost=weekend_cost, available=available, car=car, van=van, caravan=caravan)

    # to display cars in the database
    def display_car(self):
        return super().display_car()

    # to display vans in the database
    def display_van(self):
        return super().display_van()

    # to display the caravan
    def display_caravan(self):
        return super().display_caravan()

    #Calculating cost
    def display_cost(self):
        return super().display_cost()

    def calculate_cost(self, request=None):
        return super().calculate_cost(request=request)

    def available_car(self, request=None):
        return super().available_car(request=request)

    def unavailable_car(self, request=None):
        return super().unavailable_car(request=request)


if __name__ == '__main__':

    while True:

        User = Client()

        print('*************************************')
        print('*** Welcome to E & A Automobile ***')
        print('*************************************')
        try:
            user_choice = int(input('Choose any number to continue: \n\n\
                1 - View all Cars available.\n\
                2 - View all Vans available.\n\
                3 - View all Caravans available.\n\
                4 - View all vehicle cost. \n\
                5 - Calculate cost of a vehicle type. \n\
                6 - Make reservation or cancel reservation.\n\
                7 - Exit\n\n\
                \n\n\
                Users choice: '))

            if user_choice == 1:
                User.display_car()
            if user_choice == 2:
                User.display_van()
            if user_choice == 3:
                User.display_caravan()
            if user_choice == 4:
                User.display_cost()
            if user_choice == 5:
                while True:
                    try:
                        make = int(input('Which vehicle will you like to calculate(e.g: car, van, caravan)?\n\
                            1 - car. \n\
                            2 - vans. \n\
                            3 - caravan.\n\
                            4 - Return to Menu\n\n\
                            User choice(1 0r 2..): '))
                        if make == 1:
                            User.calculate_cost(request=make)
                        if make == 2:
                            User.calculate_cost(request=make)
                        if make == 3:
                            User.calculate_cost(request=make)
                        if make == 4:
                            break
                    except ValueError:
                        print('Invalid Input. Try Again.....')
            if user_choice == 6:
                while True:
                    try:
                        MC = int(input(
                            '1 - Make a reservation.\n2 - Cancel a reservation.\n3 Go back..\n\nUsers choice(1 or 2): '))

                        if MC == 1:
                            try:
                                make = int(input('Which vehicle do you wish to RESERVE?(e.g: car, van, '
                                                 'caravan)?\n\ 1 - car. \n\ 2 - vans. \n\ 3 - caravan. \n\ 4 - Return '
                                                 '\n\n\ User choice(1 or 2....: '))

                                if make == 1:
                                    User.available_car(make)
                                if make == 2:
                                    User.available_car(make)
                                if make == 3:
                                    User.available_car(make)
                                if make == 4:
                                    break
                            except ValueError:
                                print('Invalid Input. Try Again.....')
                        if MC == 2:
                            try:
                                make = int(input('Which vehicle type will you like to cancel reservation?(e.g: car, van, caravan)?\n\
                                1 - car. \n\
                                2 - vans. \n\
                                3 - caravan.\n\n\
                                User choice: '))

                                if make == 1:
                                    User.unavailable_car(make)
                                if make == 2:
                                    User.unavailable_car(make)
                                if make == 3:
                                    User.unavailable_car(make)
                                if make == 4:
                                    break
                            except ValueError:
                                print('Invalid Input. Try Again.....')
                        if MC == 3:
                            break
                    except ValueError:
                        print('Invalid Input. Please Try Again.....')
            if user_choice == 5:
                print('Thank you. Have a lovely day.')
                break
        except ValueError:
            print('Invalid Input. Please Try Again.....')
