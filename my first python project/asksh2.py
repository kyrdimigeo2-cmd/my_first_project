class Person:
    """
    The Parent class represents a Person 
    
    """
    def __init__(self, name: str, age: int) -> None:
        """
        The constructor of the Parent class
        
        Args:
            name (str): The Person's name
            age (int): The Person's age
        """
        self.name = name
        self.age = age

    def get_details(self) -> None:
        """
        This function prints the Person's name and age
        """
        print(f'The Person\'s name is {self.name} and his/her age is {self.age}')

class Guest(Person):
    """
    This is a subclass of the class Person
    """
    def __init__(self, name: str, age: int, room_number: str, nights: int) -> None:
        """
        The constructor of the subclass with extra attributes
         Args:
            name (str): The Person's name
            age (int): The Person's age
            room_number(str): The guest's assigned room
            nights(int): The number of nights the guest will stay
        """
        super().__init__(name, age)
        self.room_number = room_number
        self.nights = nights

    def calculate_bill(self, rate_per_night : float = 0) -> float:
        """
        Calculates the total bill and returns the total amount based on the number of nights and a given room rate
        Args:
            rate_per_night (float): The rate per night
        Returns:
                float: The total amount
        """
        total_amount = self.nights * rate_per_night
        print(f'The total amount for the guest {self.name} is: {total_amount:.2f}')
        return total_amount

class Staff(Person):
    """
    This is a subclass of the class Person
    """
    def __init__(self, name: str, age: int, position: str, salary: float) -> None:
        """
        The constructor of the subclass with extra attributes
        Args:
            name (str): The Person's name
            age (int): The Person's age
            position (str): The job title of the staff member(for example 'Receptionist')
            salary (float): The staff member's salary
        """
        super().__init__(name, age)
        self.position = position
        if salary < 0:
            print("The salary must be above 0")
            return None
        self.salary = salary

    def give_raise(self, amount: float) -> float:
        """
        Increases the salary by a specific amount
        Args:
            amount(float): the amount by which the salary increases
        Return:
            float: The updated salary.
        """
        if amount <= 0:
            print('The amount must be above 0')
            return self.salary
        self.salary += amount
        print(f'New salary of {self.name} is: {self.salary:.2f}')
        return self.salary

class Hotel:
    """
    This class manages guests and staff
    """
    def __init__(self, name: str) -> None:
        """
        The constructor of the class Hotel
        Args:
            name (str): The hotel's name.
        """
        self.name = name
        self.guests = []
        self.staff = []

    def check_in(self, guest:Guest) -> None:
        """
        Adds a guest to the hotel
        Args:
            guest(Guest): The guest person to add
        """
        self.guests.append(guest)

    def check_out(self, guest: Guest) -> None:
        """
        Removes a guest from the hotel
        Args:
            guest(Guest): The guest person to remove
        """
        self.guests.remove(guest)

    def hire_staff(self, member: Staff) -> None:
        """
        Adds a staff member to the hotel
        Args:
            member(Staff): The staff member to add
        """
        self.staff.append(member)

    def list_guests(self) -> None:
        """
        Prints details of all guests in the hotel
        """
        for guest in self.guests:
            guest.get_details()
            print(f'Guest\'s room is: {guest.room_number} and the number of nights are: {guest.nights}')

    def list_staff(self) -> None:
        """
        Prints details of all staff members in the hotel.
        """
        for member in self.staff:
            member.get_details()
            print(f'The Person\'s position is: {member.position} and his/her salary is: {member.salary}')

guest1 = Guest("Kyriakos", 26, "120", 10)
guest2 = Guest("Dimitris", 20, "230", 6)
staff1 = Staff( "Maria", 30, "Receptionist", 1600.5)
staff2 = Staff("Anna", 25, "Houeskeeping", 1400)
hotel = Hotel("Hilton")
staff2.give_raise(120)
guest2.calculate_bill(10)
hotel.check_in(guest1)
hotel.check_in(guest2)
hotel.check_out(guest1)
hotel.hire_staff(staff1)
hotel.list_guests()
hotel.list_staff()



