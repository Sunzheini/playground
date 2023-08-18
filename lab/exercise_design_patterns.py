# -----------------------------------------------------------------------------------
# 01. Singleton pattern
# -----------------------------------------------------------------------------------

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True


# -----------------------------------------------------------------------------------
# 02. Factory pattern
# -----------------------------------------------------------------------------------

from abc import ABC, abstractmethod


# Abstract Product
class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

# Concrete Products
class CheesePizza(Pizza):
    def prepare(self):
        print("Preparing Cheese Pizza")

    def bake(self):
        print("Baking Cheese Pizza")

class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing Pepperoni Pizza")

    def bake(self):
        print("Baking Pepperoni Pizza")

# Abstract Creator
class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self, pizza_type):
        pass

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()

# Concrete Creators
class NewYorkPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()

class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()

# Client code
ny_store = NewYorkPizzaStore()
chicago_store = ChicagoPizzaStore()

ny_store.order_pizza("cheese")
chicago_store.order_pizza("pepperoni")


# -----------------------------------------------------------------------------------
# 03. Observer pattern
# -----------------------------------------------------------------------------------

from abc import ABC, abstractmethod

# Abstract Observer
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

# Abstract Subject
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# Concrete Observers
class CurrentConditionsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Current conditions: {temperature}°C, {humidity}%, {pressure} hPa")

class StatisticsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print("Updating statistics...")

# Concrete Subject
class WeatherStation(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()

# Client code
weather_station = WeatherStation()
current_display = CurrentConditionsDisplay()
statistics_display = StatisticsDisplay()

weather_station.register_observer(current_display)
weather_station.register_observer(statistics_display)

weather_station.set_measurements(25, 60, 1010)


# -----------------------------------------------------------------------------------
# 04. Decorator pattern
# -----------------------------------------------------------------------------------

from abc import ABC, abstractmethod

# Component
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

# Concrete Components
class Espresso(Coffee):
    def cost(self):
        return 2.0

class Decaf(Coffee):
    def cost(self):
        return 1.5

# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    @abstractmethod
    def cost(self):
        pass

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.2

class WhippedCreamDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.7

# Client code
coffee = Espresso()
print(f"Espresso: ${coffee.cost()}")

coffee_with_milk = MilkDecorator(coffee)
print(f"Espresso with milk: ${coffee_with_milk.cost()}")

coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print(f"Espresso with milk and sugar: ${coffee_with_milk_and_sugar.cost()}")

coffee_with_whipped_cream = WhippedCreamDecorator(coffee)
print(f"Espresso with whipped cream: ${coffee_with_whipped_cream.cost()}")


# -----------------------------------------------------------------------------------
# 05. Strategy pattern
# -----------------------------------------------------------------------------------

from abc import ABC, abstractmethod

# Strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} using credit card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} using PayPal")

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} using Bitcoin")

# Context
class ShoppingCart:
    def __init__(self, payment_strategy):
        self._payment_strategy = payment_strategy

    def checkout(self, total_amount):
        self._payment_strategy.pay(total_amount)

# Client code
credit_card = CreditCardPayment()
paypal = PayPalPayment()
bitcoin = BitcoinPayment()

cart1 = ShoppingCart(credit_card)
cart1.checkout(100)

cart2 = ShoppingCart(paypal)
cart2.checkout(50)

cart3 = ShoppingCart(bitcoin)
cart3.checkout(200)


# -----------------------------------------------------------------------------------
# 06. Adapter pattern
# -----------------------------------------------------------------------------------

from abc import ABC, abstractmethod

# Target interface (Expected by client)
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type, file_name):
        pass

# Adaptee classes (Incompatible interfaces)
class AdvancedMediaPlayer(ABC):
    @abstractmethod
    def play_vlc(self, file_name):
        pass

    @abstractmethod
    def play_mp4(self, file_name):
        pass

class VLCPlayer(AdvancedMediaPlayer):
    def play_vlc(self, file_name):
        print(f"Playing VLC file: {file_name}")

    def play_mp4(self, file_name):
        pass

class MP4Player(AdvancedMediaPlayer):
    def play_vlc(self, file_name):
        pass

    def play_mp4(self, file_name):
        print(f"Playing MP4 file: {file_name}")

# Adapter class
class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type):
        if audio_type == 'vlc':
            self.advanced_player = VLCPlayer()
        elif audio_type == 'mp4':
            self.advanced_player = MP4Player()

    def play(self, audio_type, file_name):
        if audio_type == 'vlc':
            self.advanced_player.play_vlc(file_name)
        elif audio_type == 'mp4':
            self.advanced_player.play_mp4(file_name)

# Concrete MediaPlayer
class AudioPlayer(MediaPlayer):
    def play(self, audio_type, file_name):
        if audio_type == 'mp3':
            print(f"Playing MP3 file: {file_name}")
        elif audio_type == 'vlc' or audio_type == 'mp4':
            media_adapter = MediaAdapter(audio_type)
            media_adapter.play(audio_type, file_name)
        else:
            print(f"Unsupported audio type: {audio_type}")

# Client code
audio_player = AudioPlayer()
audio_player.play('mp3', 'song.mp3')
audio_player.play('vlc', 'movie.vlc')
audio_player.play('mp4', 'video.mp4')
audio_player.play('avi', 'video.avi')


# -----------------------------------------------------------------------------------
# 07. Facade pattern
# -----------------------------------------------------------------------------------

class CPU:
    def freeze(self):
        print("Freezing CPU")

    def jump(self, position):
        print(f"Jumping to position: {position}")

    def execute(self):
        print("Executing CPU instructions")

class Memory:
    def load(self, position, data):
        print(f"Loading data into memory at position {position}")

class HardDrive:
    def read(self, lba, size):
        print(f"Reading data from hard drive LBA {lba}, size {size}")

# Facade class
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        print("Starting computer...")
        self.cpu.freeze()
        self.memory.load(0, "BOOT_DATA")
        self.cpu.jump(0)
        self.cpu.execute()
        self.hard_drive.read(BOOT_SECTOR, SECTOR_SIZE)
        print("Computer started and ready to use")

# Constants
BOOT_SECTOR = 100
SECTOR_SIZE = 512

# Client code
computer = ComputerFacade()
computer.start()


# -----------------------------------------------------------------------------------
# 08. Iterator pattern
# -----------------------------------------------------------------------------------

from abc import ABC, abstractmethod

# Iterator interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# Concrete Iterator
class BookIterator(Iterator):
    def __init__(self, books):
        self.books = books
        self.current_index = 0

    def has_next(self):
        return self.current_index < len(self.books)

    def next(self):
        book = self.books[self.current_index]
        self.current_index += 1
        return book

# Collection interface
class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

# Concrete Collection
class BookstoreInventory(IterableCollection):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def create_iterator(self):
        return BookIterator(self.books)

# Book class
class Book:
    def __init__(self, title):
        self.title = title

# Client code
inventory = BookstoreInventory()
inventory.add_book(Book("The Great Gatsby"))
inventory.add_book(Book("To Kill a Mockingbird"))
inventory.add_book(Book("1984"))

iterator = inventory.create_iterator()

while iterator.has_next():
    book = iterator.next()
    print(f"Book Title: {book.title}")


# -----------------------------------------------------------------------------------
# 09. Command pattern
# -----------------------------------------------------------------------------------

from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Commands
class TVOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()

class TVOffCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_off()

class StereoOnCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.turn_on()

class StereoOffCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.turn_off()

# Receiver classes
class TV:
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")

class Stereo:
    def turn_on(self):
        print("Stereo is ON")

    def turn_off(self):
        print("Stereo is OFF")

# Invoker
class RemoteControl:
    def __init__(self):
        self.commands = [None] * 2

    def set_command(self, slot, command):
        self.commands[slot] = command

    def press_button(self, slot):
        if self.commands[slot]:
            self.commands[slot].execute()


# Client code
tv = TV()
stereo = Stereo()

tv_on = TVOnCommand(tv)
tv_off = TVOffCommand(tv)

stereo_on = StereoOnCommand(stereo)
stereo_off = StereoOffCommand(stereo)

remote = RemoteControl()
remote.set_command(0, tv_on)
remote.set_command(1, stereo_on)

remote.press_button(0)
remote.press_button(1)


# -----------------------------------------------------------------------------------
# 10. Template Method pattern
# -----------------------------------------------------------------------------------

from abc import ABC, abstractmethod

# Abstract class with template method
class Beverage(ABC):
    def prepare_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def boil_water(self):
        pass

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def pour_in_cup(self):
        print("Pouring into cup")

    @abstractmethod
    def add_condiments(self):
        pass

# Concrete subclasses
class Tea(Beverage):
    def boil_water(self):
        print("Boiling water")

    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

class Coffee(Beverage):
    def boil_water(self):
        print("Boiling water")

    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")

# Client code
tea = Tea()
coffee = Coffee()

print("Making tea...")
tea.prepare_beverage()

print("\nMaking coffee...")
coffee.prepare_beverage()


# -----------------------------------------------------------------------------------
# 11. State pattern
# -----------------------------------------------------------------------------------

from abc import ABC, abstractmethod

# State interface
class ATMState(ABC):
    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def eject_card(self):
        pass

    @abstractmethod
    def enter_pin(self, pin):
        pass

    @abstractmethod
    def request_cash(self, amount):
        pass

# Concrete state classes
class NoCard(ATMState):
    def insert_card(self):
        print("Card inserted")
        return HasCard()

    def eject_card(self):
        print("No card to eject")

    def enter_pin(self, pin):
        print("Please insert a card first")

    def request_cash(self, amount):
        print("Please insert a card first")

class HasCard(ATMState):
    def insert_card(self):
        print("Card is already inserted")

    def eject_card(self):
        print("Card ejected")
        return NoCard()

    def enter_pin(self, pin):
        if pin == 1234:
            print("PIN correct")
            return HasPin()
        else:
            print("Invalid PIN")
            return NoCard()

    def request_cash(self, amount):
        print("Please enter PIN first")

class HasPin(ATMState):
    def insert_card(self):
        print("Card is already inserted")

    def eject_card(self):
        print("Card ejected")
        return NoCard()

    def enter_pin(self, pin):
        print("PIN is already entered")

    def request_cash(self, amount):
        if amount <= 0:
            print("Amount should be greater than zero")
        else:
            print(f"Withdrawing ${amount}")

class ATM:
    def __init__(self):
        self.current_state = NoCard()

    def set_state(self, state):
        self.current_state = state

    def insert_card(self):
        self.current_state = self.current_state.insert_card()

    def eject_card(self):
        self.current_state = self.current_state.eject_card()

    def enter_pin(self, pin):
        self.current_state = self.current_state.enter_pin(pin)

    def request_cash(self, amount):
        self.current_state.request_cash(amount)

# Client code
atm = ATM()

atm.insert_card()
atm.enter_pin(1234)
atm.request_cash(1000)

atm.eject_card()
atm.enter_pin(4321)


# -----------------------------------------------------------------------------------
# 12. Proxy pattern
# -----------------------------------------------------------------------------------

from abc import ABC, abstractmethod

# Subject interface
class InternetAccess(ABC):
    @abstractmethod
    def grant_access(self):
        pass

# Concrete real subject
class RealInternetAccess(InternetAccess):
    def __init__(self, website):
        self.website = website

    def grant_access(self):
        print(f"Access granted to {self.website}")

# Proxy
class ProxyInternetAccess(InternetAccess):
    def __init__(self, age):
        self.age = age
        self.real_access = RealInternetAccess("example.com")

    def grant_access(self):
        if self.age >= 18:
            self.real_access.grant_access()
        else:
            print("Access denied. Age is below 18")

# Client code
user1 = ProxyInternetAccess(20)
user1.grant_access()

user2 = ProxyInternetAccess(15)
user2.grant_access()

