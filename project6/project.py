                       # ==== Using self ===
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.
class Student:
    def __init__(self, name, marks):
        self.name = name      # using self to initialize the name
        self.marks = marks    # using self to initialize the marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


# Example usage:
student1 = Student("Sania", 92)
student1.display()

                   #====Using cls=====
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.
class Counter:
    count = 0  # Class variable to keep track of number of objects

    def __init__(self):
        Counter.count += 1  # Increment count when a new object is created

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")


# Example usage:
c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()

Counter.display_count()
 # Output: Total objects created: 4
     
     #====Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class

class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):        # Public method
        print(f"{self.brand} car is starting...")

# Instantiate the class
my_car = Car("Toyota")

# Access public variable
print("Car Brand:", my_car.brand)

# Call public method
my_car.start()

             # === Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.
class Bank:
    bank_name = "Meezan Bank"  # Class variable (shared by all)

    def __init__(self, account_holder):
        self.account_holder = account_holder  # Instance variable (unique for each object)

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name  # Change the class variable

    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {self.bank_name}")


# Create objects
acc1 = Bank("Sania")
acc2 = Bank("Adeel")

# Show initial bank names
acc1.display()
acc2.display()

print("\nChanging bank name to 'National Bank'...\n")

# Change bank name (affects all instances)
Bank.change_bank_name("National Bank")

# Show updated bank names
acc1.display()
acc2.display()
               #  ===Static Variables and Static Methods ===
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Example usage
result = MathUtils.add(5, 7)
print("Sum:", result)

            # ==== 6. Constructors and Destructors ====
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).
class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

# Example usage
logger = Logger()

# Optionally delete the object explicitly
del logger

           # ==== 7. Access Modifiers: Public, Private, and Protected ====
# Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable (convention)
        self.__ssn = ssn          # Private variable (name mangling)

# Create object
emp = Employee("Alice", 50000, "123-45-6789")

# Accessing public variable
print("Name (public):", emp.name)

# Accessing protected variable
print("Salary (_protected):", emp._salary)

# Trying to access private variable directly
try:
    print("SSN (__private):", emp.__ssn)
except AttributeError as e:
    print("Error accessing __ssn directly:", e)

# Accessing private variable using name mangling
print("SSN (accessed via name mangling):", emp._Employee__ssn)

              # ==== 8. The super() Function ====
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.
class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call to the base class constructor
        self.subject = subject
        print("Teacher constructor called")

# Example usage
teacher = Teacher("Mr. Smith", "Mathematics")

print("Name:", teacher.name)
print("Subject:", teacher.subject)
# Output: Person constructor called
#         Teacher constructor called
#         Name: Mr. Smith
#         Subject: Mathematics




        
        






 
