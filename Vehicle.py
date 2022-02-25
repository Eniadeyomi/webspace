# Vehicle rental database
# Creating a class Vehicle interface
# A dictionary will be created to handle the vehicle types and their attributes
class Vehicle_Interface:

    def __init__(self, ref=None, make=None, model=None, km=None, numPassenger=None, number_doors=None, num_beds=None,
                 plate_number=None, daily_cost=None, weekly_cost=None, weekend_cost=None, available=None, car=None,
                 van=None, caravan=None):
        self.ref = ref
        self.make = make
        self.model = model
        self.km = km
        self.numPassenger = numPassenger
        self.number_doors = number_doors
        self.num_beds = num_beds
        self.plate_number = plate_number
        self.daily_cost = daily_cost
        self.weekly_cost = weekly_cost
        self.weekend_cost = weekend_cost
        self.available = available
        self.car = {'Reference': [1, 2, 3, 4, 5],
                    'Make': ['Audi', 'Ford', 'Toyota', 'Ford', 'Renault'],
                    'Model': ['A5', 'Fiesta', 'Corolla', 'Focus', 'Clio'],
                    'Km': [10, 20, 15, 15, 20],
                    'numPassenger': [5, 5, 5, 5, 5],
                    'number_doors': [4, 3, 5, 5, 3],
                    'plate_number': ["171-D-128", "12-D-564", "152-C-854", "141-WW-965", "12-G-741"],
                    'daily_cost (€)': [20, 12, 15, 15, 12],
                    'weekly_cost (€)': [120, 85, 95, 65],
                    'weekend_cost (€)': [150, 45, 50, 50, 45],
                    'available': ['Available', 'Available', 'Available', 'Available', 'Available']
                    }
        self.van = {
            'Reference': [1, 2, 3, 4, 5],
            'Make': ['Renault', 'Citroen', 'Peugot', 'Citroen'],
            'Model': ['Other', 'Berlingo', 'Partner', 'Berlingo'],
            'Km': [10, 15, 8, 15],
            'Num_passenger': [2, 3, 4, 3],
            'plate_number': ["151-D-874", "12-D-965", "12-C-758", "142-G-511"],
            'daily_cost (€)': [45, 45, 50, 45],
            'weekly_cost (€)': [260, 165, 185, 165],
            'weekend_cost (€)': [220, 85, 85, 85],
            'available': ['Available', 'Unavailable', 'Available', 'Available']
        }
        self.caravan = {
            'Reference': [1, 2, 3, 4],
            'Make': ['Renault', 'Citroen', 'Peugot', 'Citroen'],
            'Model': ['C', 'B', 'P', 'B'],
            'Km': [12, 20, 11, 15],
            'number_beds': [4, 6, 4, 2],
            'plate_number': ["11-D-146", "10-D-965", "12-C-143", "131-G-111"],
            'daily_cost (€)': [50, 50, 50, 50],
            'weekly_cost (€)': [350, 365, 350, 255],
            'weekend_cost (€)': [215, 285, 200, 185],
            'available': ['Available', 'Available', 'Available', 'Available']
        }

    # Displaying the vehicle by type in a row
    def display_car(self):
        print('***** Cars Available *****')
        for row in zip(*([key] + value for key, value in sorted(self.car.items()))):
            print(*row)

    def display_van(self):
        print('***** Vans Available *****')
        for row in zip(*([key] + value for key, value in sorted(self.van.items()))):
            print(*row)

    def display_caravan(self):
        print('***** Caravans Available *****')
        for row in zip(*([key] + value for key, value in sorted(self.caravan.items()))):
            print(*row)
            break

    # Displaying the cost associated to each vehicle type
    def display_cost(self):
        print('***** Vehicle Available By Cost *****')
        for row in zip(*([key] + value for key, value in sorted(self.car.items()))):
            print(*row)
        for row in zip(*([key] + value for key, value in sorted(self.van.items()))):
            print(*row)
        for row in zip(*([key] + value for key, value in sorted(self.caravan.items()))):
            print(*row)

    # Calculating cost associated with renting a vehicle from the database
    def calculate_cost(self, request=None):
        print('\n\n\n\n\n\n')
        while True:
            try:
                # The user wants to calculate for Car
                if request == 1:
                    print('***** Cars Available *****')
                    for row in zip(*([key] + value for key, value in sorted(self.car.items()))):
                        print(*row)
                    # User is allowed to calculate using the car model
                    model = str(input('Enter the Model of Car you want to calculate.'))
                    if model in self.car['Model']:
                        index = self.car['Model'].index(model)
                        # User is allowed to input the number of days or weeks or weekends for the rental
                        day = int(input('Enter the number of days: '))
                        weekly = int(input('Enter the number of weeks: '))
                        weekend = int(input('Enter the number of weekends: '))
                        print(
                            f"The {self.car[ 'Make' ][ index ]} with model {model} will cost €{day * self.car[ 'daily_cost (€)' ][ index ]} . ")
                        print(
                            f"The {self.car[ 'Make' ][ index ]} with model {model} will cost €{weekly * self.car[ 'weekly_cost (€)' ][ index ]} . ")
                        print(
                            f"The {self.car[ 'Make' ][ index ]} with model {model} will cost €{weekend * self.car[ 'weekend_cost (€)' ][ index ]} . ")
                        break
                    else:
                        print(f'{model} is not in the database. Try again')
                        break
                # The user wants to calculate for a Van
                if request == 2:
                    print('***** Van Available *****')
                    for row in zip(*([key] + value for key, value in sorted(self.van.items()))):
                        print(*row)
                    # User is allowed to input the model of Van
                    model = str(input('Enter the Model of Van you want to calculate.'))
                    if model in self.van['Model']:
                        index = self.van['Model'].index(model)
                        # User is allowed to input the number of days or weeks or weekend for the Van rental
                        day = int(input('Enter the number of days: '))
                        weekly = int(input('Enter the number of weeks: '))
                        weekend = int(input('Enter the number of weekends: '))
                        print(
                            f"The {self.van[ 'Make' ][ index ]} with model {model} will cost €{day * self.van[ 'daily_cost (€)' ][ index ]} . ")
                        print(
                            f"The {self.van[ 'Make' ][ index ]} with model {model} will cost €{weekly * self.van[ 'weekly_cost (€)' ][ index ]} . ")
                        print(
                            f"The {self.van[ 'Make' ][ index ]} with model {model} will cost €{weekend * self.van[ 'weekend_cost (€)' ][ index ]} . ")
                        break
                    else:
                        print(f'{model} is not in the database. Try again...')
                        break
                # Calculating for Caravan
                if request == 3:
                    print('***** Van Available *****')
                    for row in zip(*([key] + value for key, value in sorted(self.van.items()))):
                        print(*row)
                    # User input the model of caravan
                    model = str(input('Enter the Model of Caravan you want to calculate.'))
                    if model in self.caravan['Model']:
                        index = self.caravan['Model'].index(model)
                        # User input the number of days or weeks or weekends for the rental
                        day = int(input('Enter the number of days: '))
                        weekly = int(input('Enter the number of weeks: '))
                        weekend = int(input('Enter the number of weekends: '))
                        print(
                            f"The {self.caravan[ 'Make' ][ index ]} with model {model} will cost €{day * self.caravan[ 'daily_cost (€)' ][ index ]} . ")
                        print(
                            f"The {self.caravan[ 'Make' ][ index ]} with model {model} will cost €{weekly * self.caravan[ 'weekly_cost (€)' ][ index ]} . ")
                        print(
                            f"The {self.caravan[ 'Make' ][ index ]} with model {model} will cost €{weekend * self.caravan[ 'weekend_cost (€)' ][ index ]} . ")
                        break
                    else:
                        print(f'{model} is not in the database. Try again')
                        break
                if request is None:
                    break
            except:
                print('Invalid Input. Try Again')

    # Reservation System
    def available_car(self, request=None):
        while True:
            try:
                # User is allowed to select Reservation or cancellation of reservation
                # For reservation, user is allowed to make reservation by Vehicle type
                # To reserve a car
                if request == 1:
                    print('***** Vehicle Available *****')
                    for row in zip(*([key] + value for key, value in sorted(self.car.items()))):
                        print(*row)

                    # user enter the car model that will be reserved
                    index = 0
                    choice = input('Enter the Model you want to Reserve: ')
                    if choice in self.car['Model']:
                        index + self.car['Model'].index(choice)
                    else:
                        print('Wrong Choice of Model\n\n\n\n')
                        break

                    # Data update in the database
                    print('***** Update Data Available *****')
                    for i in self.car['available']:
                        self.car['available'][index] = 'Unavailable'
                    print('\n\n\n\nYour reservation as been made, Thank you.\n\n\n\n')
                    break

                # To reserve a Van
                if request == 2:
                    print('***** Van Available *****')
                    for row in zip(*([key] + value for key, value in sorted(self.van.items()))):
                        print(*row)

                    # User enters the model of van
                    index = 0
                    choice = input('Enter the Model you want to Reserve: ')
                    if choice in self.van['Model']:
                        index + self.van['Model'].index(choice)
                    else:
                        print('Wrong Choice of Model')
                        break

                    # Data Update in the database
                    print('***** Update Data Available *****')
                    for i in self.van['available']:
                        self.van['available'][index] = 'Unavailable'
                    print('\n\n\n\nYour reservation as been made, Thank you.\n\n\n\n')

                    for row in zip(*([key] + value for key, value in sorted(self.van.items()))):
                        print(*row)

                # To reserve a Caravan
                if request == 3:
                    print('***** Caravan Available *****')
                    for row in zip(*([key] + value for key, value in sorted(self.caravan.items()))):
                        print(*row)

                    # make reservation
                    index = 0
                    choice = input('Enter the Model you want to Reserve: ')
                    if choice in self.caravan['Model']:
                        index + self.caravan['Model'].index(choice)
                    else:
                        print('Wrong Choice of Model')
                        break

                    print('***** Update Data Available *****')
                    for i in self.caravan['available']:
                        self.caravan['available'][index] = 'Unavailable'
                    print('\n\n\n\nYour reservation as been made, Thank you.\n\n\n\n')

                    for row in zip(*([key] + value for key, value in sorted(self.caravan.items()))) :
                        print(*row)
            except ValueError:
                print('Invalid Request, Try again............')

    # Cancelling a reservation
    # User is allowed to select Reservation or cancellation of reservation
    # For cancellation, user is allowed to cancel by Vehicle type
    # To cancel a car reservation
    def unavailable_car(self, request=None):
        while True:
            try:
                if request == 1:
                    print('***** Data Available *****')
                    for row in zip(*([key] + value for key, value in sorted(self.car.items()))):
                        print(*row)

                    # Entering the model of the car to be cancelled
                    index = 0
                    choice = input('Enter the Car model you wish to  cancel : ')
                    if choice in self.car['Model']:
                        index + self.car['Model'].index(choice)
                    else:
                        print('Wrong Choice of Model\n\n\n\n')
                        break

                    print('***** Update Data Available *****')
                    for i in self.car['available']:
                        self.car['available'][index] = 'Unavailable'
                    print('\n\n\n\nYour reservation cancellation request is successful, Thank you.\n\n\n\n')

                    for row in zip(*([key] + value for key, value in sorted(self.car.items()))):
                        print(*row)
                        break

                # To cancel a van reservation
                if request == 2:
                    print('***** Data Available *****')
                    for row in zip(*([key] + value for key, value in sorted(self.van.items()))):
                        print(*row)

                    # Enter the model of van to be cancelled
                    index = 0
                    choice = input('Enter the Model you want to Cancel: ')
                    if choice in self.van['Model']:
                        index + self.van['Model'].index(choice)
                    else:
                        print('Wrong Choice of Model\n\n\n\n')
                        break

                    print('***** Update Data Available *****')
                    for i in self.van['available']:
                        self.van['available'][index] = 'Available'
                    print('\n\n\n\nYour reservation cancellation request is successful, Thank you.\n\n\n\n')

                    for row in zip(*([key] + value for key, value in sorted(self.van.items()))):
                        print(*row)
                        break

                # To cancel a Caravan reservation
                if request == 3:
                    print('***** Data Available *****')
                    for row in zip(*([key] + value for key, value in sorted(self.caravan.items()))):
                        print(*row)

                    # Enter the model to be cancelled
                    index = 0
                    choice = input('Enter the Model you want to Reserve: ')
                    if choice in self.caravan['Model']:
                        index + self.caravan['Model'].index(choice)
                    else:
                        print('Wrong Choice of Model\n\n\n\n')
                        break

                    print('***** Update Data Available *****')
                    for i in self.caravan['available']:
                        self.caravan['available'][index] = 'Available'
                    print('\n\n\n\nYour cancellation as been made, Thank you.\n\n\n\n')

                    for row in zip(*([key] + value for key, value in sorted(self.caravan.items()))) :
                        print(*row)
                        break

            except ValueError:
                print('Invalid Input, Try again...')


# Creating classes for different vehicles
# creating a class car
class Car(Vehicle_Interface):

    def __init__(self, ref=None, make=None, model=None, km=None, numPassenger=None, number_doors=None, num_beds=None,
                 plate_number=None, daily_cost=None, weekly_cost=None, weekend_cost=None, available=None, car=None,
                 van=None, caravan=None):
        super().__init__(ref=ref, make=make, model=model, km=km, numPassenger=numPassenger, number_doors=number_doors,
                         num_beds=num_beds, plate_number=plate_number, daily_cost=daily_cost, weekly_cost=weekly_cost,
                         weekend_cost=weekend_cost, available=available, car=None, van=None, caravan=None)

    # Adding a car to the database with the attributes
    def add(self):
        self.car['Reference'] = int(input('Reference No: '))
        self.car['Make'] = input('Make: ')
        self.car['Model'] = input('Model: ')
        self.car['Km'] = int(input('Km/h: '))
        self.car['numPassenger'] = int(input('Passengers: '))
        self.car['number_doors'] = int(input('Doors: '))
        self.car['plate_number'] = input('Plate No: ')
        self.car['daily_cost'] = int(input('Daily cost: '))
        self.car['weekly_cost'] = int(input('Weekly cost: '))
        self.car['weekend_cost'] = int(input('Weekend cost: '))
        self.car['available'] = input('Is the car available: ')
        print('The New Vehicle as been added successfully to the database')
        for i in self.car:
            print(i, self.car[i])

    # deleting a car from the database
    def remove(self):
        print('***** Data Available *****')
        for row in zip(*([key] + value for key, value in sorted(self.car.items()))):
            print(*row)

        # User deletes with the car model
        index = 0
        choice = input('Enter the Model you want to delete: ')
        if choice in self.car['Model']:
            index += self.car['Model'].index(choice)

        # Displaying the data update
        print('***** Data Available *****')
        for row in self.car.values():
            row.pop(index)

        for row in zip(*([key] + value for key, value in sorted(self.car.items()))):
            print(*row)


# Creating a class for Van
class Van(Vehicle_Interface):

    def __init__(self, ref=None, make=None, model=None, km=None, numPassenger=None, number_doors=None, num_beds=None,
                 plate_number=None, daily_cost=None, weekly_cost=None, weekend_cost=None, car=None, van=None,
                 caravan=None):
        super().__init__(ref=ref, make=make, model=model, km=km, numPassenger=numPassenger, number_doors=number_doors,
                         num_beds=num_beds, plate_number=plate_number, daily_cost=daily_cost, weekly_cost=weekly_cost,
                         weekend_cost=weekend_cost, available=None, car=None, van=None, caravan=None)

    # noinspection PyTypedDict
    # to add a van to the database
    def add(self):
        self.van['Reference'] = int(input('Reference No: '))
        self.van['Make'] = input('Make: ')
        self.van['Model'] = input('Model: ')
        self.van['Km'] = int(input('Km/h: '))
        self.van['numPassenger'] = int(input('Passengers: '))
        self.van['plate_number'] = input('Plate No: ')
        self.van['daily_cost'] = int(input('Daily cost: '))
        self.van['weekly_cost'] = int(input('Weekly cost: '))
        self.van['weekend_cost'] = int(input('Weekend cost: '))
        self.van['available'] = input('Is the car available: ')
        print('The new van as been added successfully to the database')
        for i in self.van:
            print(i, self.van[i])

    # to delete a van from the database
    def remove(self):
        print('***** Data Available *****')
        for row in zip(*([key] + value for key, value in sorted(self.van.items()))):
            print(*row)

        # user enter the model to delete
        index = 0
        choice = input('Enter the Model you want to delete: ')
        if choice in self.van['Model']:
            index += self.van['Model'].index(choice)

        # data update after deleting
        print('***** Data Available *****')
        for row in self.van.values():
            row.pop(index)

        for row in zip(*([key] + value for key, value in sorted(self.van.items()))):
            print(*row)


# Creating a class caravan
class Caravan(Vehicle_Interface):

    def __init__(self, ref=None, make=None, model=None, km=None, numPassenger=None, number_doors=None, num_beds=None,
                 plate_number=None, daily_cost=None, weekly_cost=None, weekend_cost=None, available=None,
                 car=None, van=None, caravan=None):
        super().__init__(ref=ref, make=make, model=model, km=km, numPassenger=numPassenger, number_doors=number_doors,
                         num_beds=num_beds, plate_number=plate_number, daily_cost=daily_cost, weekly_cost=weekly_cost,
                         weekend_cost=weekend_cost, available=available, car=None, van=None, caravan=None)

    # To add a caravan to the database
    def add(self):
        self.caravan['Reference'] = int(input('Reference No: '))
        self.caravan['Make'] = input('Make: ')
        self.caravan['Model'] = input('Model: ')
        self.caravan['Km'] = int(input('Km/h: '))
        self.caravan['num_bed'] = int(input('Num_bed: '))
        self.caravan['plate_number'] = input('Plate No: ')
        self.caravan['daily_cost'] = int(input('Daily cost: '))
        self.caravan['weekly_cost'] = int(input('Weekly cost: '))
        self.caravan['weekend_cost'] = int(input('Weekend cost: '))
        self.caravan['available'] = input('Is the car available: ')
        print('The caravan as been added successfully to the database')
        for i in self.caravan:
            print(i, self.caravan[i])

    # to delete a caravan from the database
    def remove(self):
        print('***** Data Available *****')
        for row in zip(*([key] + value for key, value in sorted(self.caravan.items()))):
            print(*row)

        # entering the model of caravan that user want to delete
        index = 0
        choice = input('Enter the Model you want to delete: ')
        if choice in self.caravan['Model']:
            index += self.caravan['Model'].index(choice)

        print('***** Data Available *****')
        for row in self.caravan.values():
            row.pop(index)

        for row in zip(*([key] + value for key, value in sorted(self.caravan.items()))):
            print(*row)


# Users login for the company view
def login():
    # Company Login Details
    print('Welcome to E and A Rental Services')
    # instance created
    username = 'adeyomi'
    while True:
        try:
            login = input('Enter username to login: ')
            if username != login.lower():
                print('Incorrect Username')
            else:
                break
        except TypeError:
            print('Invalid username')


def access():
    pass


if __name__ == '__main__':

    VI = Vehicle_Interface()
    Cars = Car()
    Vans = Van()
    Caravans = Caravan()

    login()
    while True:
        try:
            # To carry out a function on the database
            print('Choice 1: Add Vehicle to Database')
            print('Choice 2: Delete Vehicle from Database')
            print('Choice 3: Logout from the Database')

            choice = input("Please enter your choice: ")
            if choice == "1":
                while True:
                    try:
                        choice_1 = int(input(
                            'Which of the Vehicle would you like to add: \n 1. Car \n 2. Van \n 3. Caravan \n4. Return '
                            'to Menu\n\n\nNote: kindly choose within these numbers(1,2,3,4):'))
                        if choice_1 == 1:
                            Cars.add()
                        if choice_1 == 2:
                            Vans.add()
                        if choice_1 == 3:
                            Caravans.add()
                        if choice_1 == 4:
                            break
                    except ValueError:
                        print('Invalid Input, Try again')

            if choice == "2":
                while True:
                    try:
                        choice_2 = int(input(
                            'Which of the Vehicle would you like to remove: \n 1. Car \n 2. van \n 3. caravan \n4.Return '
                            ' to Menu \n\n\nNote: kindly choose within these numbers(1,2,3,):'))
                        if choice_2 == 1:
                            Cars.remove()
                        if choice_2 == 2:
                            Vans.remove()
                        if choice_2 == 3:
                            Caravans.remove()
                        if choice == 4:
                            break
                    except ValueError:
                        print('Invalid Input, Try Again...')

            if choice == '3':
                print('Thank you for your time.')
                break
        except ValueError:
            print('Invalid Input, Try Again...')
