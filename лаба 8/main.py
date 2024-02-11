import doctest
from typing import Union


class Car:
    """Базовый класс машины. """
    def __init__(self, name: str, weight: Union[int, float], color: str, mark: str, wheels: int):
        """
        Создание и подготовка к работе класса 'Машина'
        :param name: Названия и модель машины
        :param color: Цвет машины
        :param weight: Вес машины в килограммах
        :param mark: Марка автомобиля
        :param wheels: Количество колёс у машины
        Пример:
        >>> Car1 = Car("Camry", 2000, "black", "Toyota", 4) # инициализация экземпляра класса
        """
        self._name = name
        self._mark = mark
        self.weight = weight
        self.color = color
        self.wheels = wheels

    def __str__(self):
        """
        Возвращает информацию об объекте класса для пользователей
        Пример:
        >>> Car1 = Car("Camry", 2000, "black", "Toyota", 4)
        >>> Car1.__str__()
        'Автомобиль Camry производителя Toyota, вес 2000 кг, цвет black, 4 колеса'
        """
        return f"Автомобиль {self.name} производителя {self.mark}, вес {self.weight} кг, " \
               f"цвет {self.color}, {self.wheels} колеса"

    def __repr__(self):
        """
        Возвращает информацию об объекте класса для разработчиков
        Пример:
        >>> Car1 = Car("Camry", 2000, "black", "Toyota", 4)
        >>> Car1.__repr__()
        "Car(name='Camry', weight=2000, color='black', mark='Toyota', wheels=4)"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight!r}, color={self.color!r}, mark={self.mark!r}, wheels={self.wheels})"

    def remove_wheels(self, wheels_remove: int) -> int:
        """
        Удаление колёс с автомобиля
        :param wheels_remove: количество удаляемых колёс
        :return: текущее количество колёс автомобиля
        Пример:
        >>> Car1 = Car("Camry", 2000, "black", "Toyota", 4)
        >>> Car1.remove_wheels(2)
        2
        """

        if not isinstance(wheels_remove, int):
            raise TypeError("Количество удаляемых колёс автомобиля должно быть целым числом")
        if wheels_remove < 0:
            raise ValueError("Количество удаляемых колёс автомобиля не может быть меньше 0")
        if self.wheels < wheels_remove:
            raise ValueError("Количество колёс автомобиля не может быть меньше 0")
        self.wheels -= wheels_remove
        return self.wheels

    def add_weight(self, new_weight: Union[int, float]) -> Union[int, float]:
        """
        Добавление веса автомобилю
        :param new_weight: Вес добавляемого груза в килограммах
        :return: Текущий вес автомобиля
        Пример:
        >>> Car1 = Car("Camry", 2000, "black", "Toyota", 4)
        >>> Car1.add_weight(15)
        2015
        """
        if not isinstance(new_weight, (int, float)):
            raise TypeError("Добавляемый вес должен быть величиной типа int или float")
        if new_weight < 0:
            raise ValueError("Добавляемый вес должен быть больше 0")
        self.weight += new_weight
        return self.weight

    @property
    def name(self) -> str:
        """
        Возвращает название автомобиля
        Пример:
        >>> Car1 = Car("Camry", 2000, "black", "Toyota", 4)
        >>> Car1.name
        'Camry'
        """
        return self._name

    @property
    def mark(self) -> str:
        """
        Возвращает марку автомобиля
        Пример:
        >>> Car1 = Car("Camry", 2000, "black", "Toyota", 4)
        >>> Car1.mark
        'Toyota'
        """
        return self._mark

    @property
    def weight(self) -> float:
        """
        Возвращает вес автомобиля в килограммах
        Пример:
        >>> Car1 = Car("Camry", 2000, "black", "Toyota", 4)
        >>> Car1.weight
        2000
        """
        return self._weight

    @property
    def color(self) -> str:
        """
        Возвращает цвет автомобиля
        Пример:
        >>> Car1 = Car("Camry", 2000, "black", "Toyota", 4)
        >>> Car1.color
        'black'
        """
        return self._color

    @property
    def wheels(self) -> int:
        """
        Возвращает количество колёс у автомобиля
        Пример:
        >>> Car1 = Car("Camry", 2000, "black", "Toyota", 4)
        >>> Car1.wheels
        4
        """
        return self._wheels

    @weight.setter
    def weight(self, new_weight: Union[int, float]) -> None:
        """
        Устанавливает вес автомобиля в килограммах
        :param new_weight: Устанавливаемый вес автомобиля в килограммах
        Пример:
        >>> Car1 = Car("Camry", 2000, "black", "Toyota", 4)
        >>> Car1.weight = 15
        """
        if not isinstance(new_weight, (int,float)):
            raise TypeError("Вес автомобиля должен быть типа int или float")
        if new_weight <= 0:
            raise ValueError("Вес автомобиля должен быть положительным числом")
        self._weight = new_weight

    @color.setter
    def color(self, new_color: str) -> None:
        """
        Устанавливает цвет автомобиля
        :param new_color: Новый цвет автомобиля
        Пример:
        >>> Car1 = Car("Camry", 2000, "black", "Toyota", 4)
        >>> Car1.color = "Black"
        """
        if not isinstance(new_color, str):
            raise TypeError("Цвет автомобиля должен быть строкой")
        self._color = new_color

    @wheels.setter
    def wheels(self, new_wheels: int) -> None:
        """
        Устанавливает количество колёс автомобиля
        :param new_wheels: Устанавливаемое количество колёс автомобиля
        Пример:
        >>> Car1 = Car("Camry", 2000, "black", "Toyota", 4)
        >>> Car1.wheels = 6
        """
        if not isinstance(new_wheels, int):
            raise TypeError("Количество колёс автомобиля должно быть целым числом")
        if new_wheels < 0:
            raise ValueError("Количество колёс автомобиля не может быть меньше 0")
        self._wheels = new_wheels


class Truck(Car):
    def __init__(self, name: str, weight: Union[int, float], color: str, mark: str,
                 wheels: int, cargo_weight: Union[int, float], cargo_name: str):
        """
        Создание и подготовка к работе подкласса класса 'Машина' 'Грузовая машина'
        :param name: Названия и модель машины
        :param color: Цвет машины
        :param weight: Вес машины в килограммах
        :param mark: Марка автомобиля
        :param wheels: Количество колёс у машины
        :param cargo_weight: Вес груза
        :param cargo_name: Название груза
        Пример:
        >>> Car2 = Truck("Camry", 2000, "black", "Toyota", 4, 70, "Wood") # инициализация экземпляра класса
        """
        self.cargo_name = cargo_name
        self.cargo_weight = cargo_weight
        super().__init__(name, weight, color, mark, wheels)

    def __str__(self):
        """
        Возвращает информацию об объекте класса для пользователей
        Пример:
        >>> Car2 = Truck("Camry", 2000, "black", "Toyota", 4, 70, "Wood")
        >>> Car2.__str__()
        'Автомобиль Camry производителя Toyota, вес 2000 кг, цвет black, 4 колеса'
        """
        return super().__str__()

    def __repr__(self):
        """
        Возвращает информацию об объекте класса для разработчиков. Метод перегружен из-за появления
        новых параметров: cargo_weight, cargo_name.
        Пример:
        >>> Car2 = Truck("Camry", 2000, "black", "Toyota", 4, 70, "Wood")
        >>> Car2.__repr__()
        "Truck(name='Camry', weight=2000, color='black', mark='Toyota', wheels=4, cargo_name='Wood', cargo_weight=70)"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight!r}, " \
               f"color={self.color!r}, mark={self.mark!r}, wheels={self.wheels}," \
               f" cargo_name={self.cargo_name!r}, cargo_weight={self.cargo_weight!r})"

    def remove_wheels(self, wheels_remove: int) -> int:
        """
        Удаление колёс с автомобиля
        :param wheels_remove: количество удаляемых колёс
        :return: текущее количество колёс автомобиля
        Пример:
        >>> Car2 = Truck("Camry", 2000, "black", "Toyota", 4, 70, "Wood")
        >>> Car2.remove_wheels(2)
        2
        """
        return super().remove_wheels(wheels_remove)

    def add_weight(self, new_weight: Union[int, float]) -> Union[int, float]:
        """
        Добавление веса автомобилю
        Метод перегружен из-за наличия максимального веса у астомобиля
        :param new_weight: Вес добавляемого груза в килограммах
        :return: Текущий вес автомобиля
        Пример:
        >>> Car2 = Truck("Camry", 2000, "black", "Toyota", 4, 70, "Wood")
        >>> Car2.add_weight(15)
        2015
        """
        if not isinstance(new_weight, (int, float)):
            raise TypeError("Добавляемый вес должен быть величиной типа int или float")
        if new_weight < 0:
            raise ValueError("Добавляемый вес должен быть больше 0")
        self.weight += new_weight
        if self.weight >= 20000:
            raise ValueError("бщий вес грузового автомобиля не должен превышать 20000кг")
        return self.weight

    @property
    def cargo_name(self) -> str:
        """
        Возвращает название груза
        Пример:
        >>> Car2 = Truck("Camry", 2000, "black", "Toyota", 4, 70, "Wood")
        >>> Car2.cargo_name
        'Wood'
        """
        return self._cargo_name

    @property
    def cargo_weight(self) -> float:
        """
        Возвращает вес груза
        Пример:
        >>> Car2 = Truck("Camry", 2000, "black", "Toyota", 4, 70, "Wood")
        >>> Car2.cargo_weight
        70
        """
        return self._cargo_weight

    @cargo_weight.setter
    def cargo_weight(self, new_cargo_weight: Union[int, float]) -> None:
        """
        Устанавливает вес груза
        :param new_cargo_weight: Устанавливаемый вес груза
        Пример:
        >>> Car2 = Truck("Camry", 2000, "black", "Toyota", 4, 70, "Wood")
        >>> Car2.cargo_weight = 65
        """
        if not isinstance(new_cargo_weight, (float,int)):
            raise TypeError("Вес груза должен быть числом")
        if new_cargo_weight <= 0:
            raise ValueError("Вес груза должен быть положительным числом")
        self._cargo_weight = new_cargo_weight

    @cargo_name.setter
    def cargo_name(self, new_cargo_name: str) -> None:
        """
        Устанавливает название груза
        :param new_cargo_name: Устанавливаемое название груза
        Пример:
        >>> Car2 = Truck("Camry", 2000, "black", "Toyota", 4, 70, "Wood")
        >>> Car2.cargo_name = "Body"
        """
        if not isinstance(new_cargo_name, str):
            raise TypeError("Название груза должно быть строкой")
        self._cargo_name = new_cargo_name


if __name__ == "__main__":
    doctest.testmod()