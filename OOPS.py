# **Five Key Concepts of Object-Oriented Programming (OOP):**
   #- **Encapsulation**: Bundling data (attributes) and methods that operate on the data into a single unit (class).
   #- **Abstraction**: Hiding complex implementation details and showing only the essential features of an object.
   #- **Inheritance**: Mechanism where one class can inherit properties and behaviors (methods) from another class.
   #- **Polymorphism**: The ability to present the same interface for different underlying data types (objects of different classes).
   #- **Message Passing**: Objects interact with each other through methods (function calls).

### 2. **Python Class for a `Car` with Attributes and a Method to Display Information:**

class Car:
       def __init__(self, make, model, year):
           self.make = make
           self.model = model
           self.year = year

       def display_info(self):
           print(f"Car Information: {self.year} {self.make} {self.model}")

   # Example usage
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()  # Output: Car Information: 2020 Toyota Corolla   ```

### 3. **Difference Between Instance Methods and Class Methods:**
  # - **Instance Method**: Works with instance variables and requires an instance of the class to be called. Uses `self`.
   #- **Class Method**: Works with class-level data and is called on the class itself. Uses `cls` and is decorated with `@classmethod`.

   #**Example**:
   
class MyClass:
       def __init__(self, value):
           self.value = value  # Instance variable

       def instance_method(self):
           return f"Instance value: {self.value}"

       @classmethod
       def class_method(cls):
           return "This is a class method"

obj = MyClass(10)
print(obj.instance_method())  # Calls the instance method
print(MyClass.class_method())  # Calls the class method

### 4. **Method Overloading in Python:**
#   Python does not support method overloading directly (like in some other languages). Instead, you can achieve method overloading by using default arguments or by handling arguments dynamically using `*args` or `**kwargs`.

   #**Example**:

class MathOperations:
       def add(self, a, b, c=None):
           if c:
               return a + b + c
           else:
               return a + b

obj = MathOperations()
print(obj.add(3, 4))        # Output: 7
print(obj.add(3, 4, 5))     # Output: 12   

### 5. **Three Types of Access Modifiers in Python:**
 #  - **Public**: Accessible anywhere. Variables/methods without an underscore prefix (`self.var`).
  # - **Protected**: Accessible within the class and subclasses. Denoted by a single underscore (`_self.var`).
   #- **Private**: Accessible only within the class. Denoted by a double underscore (`__self.var`).


### 6. **Five Types of Inheritance in Python**:
#   - **Single Inheritance**: A class inherits from one base class.
 #  - **Multiple Inheritance**: A class inherits from multiple base classes.
# - **Multilevel Inheritance**: A class is derived from a class that is also derived from another class.
 #  - **Hierarchical Inheritance**: Multiple classes inherit from one base class.
  # - **Hybrid Inheritance**: A combination of two or more types of inheritance.

   #**Multiple Inheritance Example**:
class A:
       def method_a(self):
           print("Method A")

class B:
       def method_b(self):
           print("Method B")

class C(A, B):
       pass

obj = C()
obj.method_a()  # Output: Method A
obj.method_b()  # Output: Method B   ```

### 7. **Method Resolution Order (MRO) in Python:**
#   The MRO determines the order in which base classes are searched when executing a method. Python uses the C3 linearization algorithm to compute the MRO.

 #  **Retrieve MRO Programmatically**:
 
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

### 8. **Abstract Base Class `Shape` and Subclasses `Circle` and `Rectangle`:**

from abc import ABC, abstractmethod

class Shape(ABC):
       @abstractmethod
       def area(self):
           pass

class Circle(Shape):
       def __init__(self, radius):
           self.radius = radius

       def area(self):
           return 3.14 * self.radius ** 2

class Rectangle(Shape):
       def __init__(self, width, height):
           self.width = width
           self.height = height

       def area(self):
           return self.width * self.height

   # Example usage
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
       print(shape.area())  # Output: 78.5 and 24   ```
### 9. **Polymorphism Example for Calculating Areas:**

def print_area(shape):
       print(f"The area is: {shape.area()}")

circle = Circle(5)
rectangle = Rectangle(4, 6)

print_area(circle)     # Output: The area is: 78.5
print_area(rectangle)  # Output: The area is: 24

### 10. **Encapsulation in `BankAccount` Class:**

class BankAccount:
       def __init__(self, account_number, balance=0):
           self.__account_number = account_number  # Private attribute
           self.__balance = balance  # Private attribute

       def deposit(self, amount):
           if amount > 0:
               self.__balance += amount
           else:
               print("Invalid deposit amount.")

       def withdraw(self, amount):
           if 0 < amount <= self.__balance:
               self.__balance -= amount
           else:
               print("Invalid withdrawal amount.")

       def get_balance(self):
           return self.__balance

   # Example usage
account = BankAccount("12345")
account.deposit(1000)
print(account.get_balance())  # Output: 1000   ```

### 11. **Class That Overrides `__str__` and `__add__` Magic Methods:**

class MyClass:
       def __init__(self, value):
           self.value = value

       def __str__(self):
           return f"MyClass with value {self.value}"

       def __add__(self, other):
           return MyClass(self.value + other.value)

obj1 = MyClass(10)
obj2 = MyClass(20)

print(str(obj1))               # Output: MyClass with value 10
obj3 = obj1 + obj2
print(str(obj3))               # Output: MyClass with value 30

  # - `__str__` allows you to provide a string representation of the object.
   #- `__add__` allows you to use the `+` operator with objects of your class.


### 12. **Decorator to Measure and Print Execution Time of a Function:**
import time

def time_decorator(func):
       def wrapper(*args, **kwargs):
           start_time = time.time()
           result = func(*args, **kwargs)
           end_time = time.time()
           print(f"Execution time: {end_time - start_time} seconds")
           return result
       return wrapper

@time_decorator
def some_function():
       time.sleep(2)  # Simulate a time-consuming task

some_function()  # Output: Execution time: 2.00... seconds

### 13. **Diamond Problem in Multiple Inheritance and Python’s Resolution:**
  # The **Diamond Problem** occurs when a class inherits from two classes that both inherit from the same base class. Python resolves this issue using the **Method Resolution Order (MRO)**, which ensures each method is called only once and follows a specific path (depth-first, left-to-right).

   #**Example**:

class A:
       def method(self):
           print("A method")

class B(A):
       def method(self):
           print("B method")

class C(A):
       def method(self):
           print("C method")

class D(B, C):
       pass

obj = D()
obj.method()  # Output: B method
print(D.mro())  # Output shows the MRO: D -> B -> C -> A -> object

### 14. **Class Method to Keep Track of Instances Created:**

class MyClass:
       instance_count = 0

       def __init__(self):
           MyClass.instance_count += 1

       @classmethod
       def get_instance_count(cls):
           return cls.instance_countx