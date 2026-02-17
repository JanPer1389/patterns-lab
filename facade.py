from abc import ABC, abstractmethod
from enum import Enum

class Menu(Enum):
    VEGAN = 1
    NOT_VEGAN = 2
    MIXED = 3

class IMenu(ABC):
    """Базовый класс, задающий интерфейс меню"""
    @abstractmethod
    def get_name(self):
        pass

class VeganMenu(IMenu):
    def get_name(self):
        return "Веганское меню"

class NotVeganMenu(IMenu):
    def get_name(self):
        return "Не веганское меню"

class MixedMenu(IMenu):
    def get_name(self):
        return "Смешанное меню"

class IClient(ABC):
    @abstractmethod
    def request_menu(self, menu: IMenu):
        pass

    @abstractmethod
    def form_order(self):
        pass

    @abstractmethod
    def eating_food(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

class Kitchen:
    def prepare_food(self):
        print("Заказанная еда готовится")

    def call_waiter(self):
        print("Отдаем еду официанту")

class Waiter:
    def take_order(self, client: IClient):
        print(f"Официант принял заказ клиента {client.get_name()}")

    def send_to_kitchen(self, kitchen: Kitchen):
        print("Официант передал заказ на кухню")

    def serve_client(self, client: IClient):
        print(f"Блюда готовы, несу клиенту с именем {client.get_name()}")

class PizzeriaFacade:
    def __init__(self):
        self.kitchen = Kitchen()
        self.waiter = Waiter()
        # Словарь классов
        self.menus = {
            Menu.VEGAN: VeganMenu,
            Menu.NOT_VEGAN: NotVeganMenu,
            Menu.MIXED: MixedMenu
        }

    def get_menu(self, type_menu: Menu) -> IMenu:
        # Используем [], чтобы достать класс из словаря, затем () для создания объекта
        return self.menus[type_menu]()

    def take_order(self, client: IClient):
        self.waiter.take_order(client)
        self.waiter.send_to_kitchen(self.kitchen)
        self.__kitchen_work()
        self.waiter.serve_client(client)

    def __kitchen_work(self):
        self.kitchen.prepare_food()
        self.kitchen.call_waiter()

class Client(IClient):
    def __init__(self, name: str):
        self.name = name

    def request_menu(self, menu: IMenu):
        print(f"Клиент {self.name} ознакамливается с '{menu.get_name()}'")

    def form_order(self) -> dict:
        print(f"Клиент {self.name} делает заказ")

    def eating_food(self):
        print(f"Клиент {self.name} приступает к трапезе")

    def get_name(self):
        return self.name

if __name__ == "__main__":
    pizzeria = PizzeriaFacade()
    
    client1 = Client("Иван")
    client2 = Client("Александр")

    # Взаимодействие
    client1.request_menu(pizzeria.get_menu(Menu.MIXED))
    pizzeria.take_order(client1)
    
    print("-" * 30)
    
    client2.request_menu(pizzeria.get_menu(Menu.VEGAN))
    pizzeria.take_order(client2)
    
    print("-" * 30)
    
    client1.eating_food()
    client2.eating_food()
