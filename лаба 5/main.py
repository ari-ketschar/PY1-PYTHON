import doctest


class Series:
    """
        Документация на класс.
        Класс описывает модель Сериала.
    """
    def __init__(self, name: str, episodes: (int, float)) -> None:
        """ Создание и подготовка к работе объекта "Сериал"

        :param name: Название сериала
        :param episodes: количество эпизодов

        Примеры:
        >>> series = Series("Доктор кто", 848)  # инициализация экземпляра класса """
        if not isinstance(name, str):
            raise TypeError("Название сериала должно быть типа str.")
        self.name = name

        if not isinstance(episodes, (int, float)):
            raise TypeError("Количество серий должно быть типа int.")
        if episodes <= 0:
            raise ValueError("Количество серий должно быть больше 0.")
        self.episodes = episodes

        self.current_episode = 0

    def bookmark(self, current_episode: (int, float)) -> None:
        """
               Запоминание последней просмотренной серии.
               current_episode: номер последней просмотренной серии

               Примеры:
               >>> series = Series("Доктор кто", 848)
               >>> series.bookmark(666)
               """

        if not isinstance(current_episode, (int, float)):
            raise TypeError("Номер текущего эпизода должен быть типа int.")
        if current_episode <= 0 or current_episode > self.episodes:
            raise ValueError("Номер текущего эпизода должен быть больше нуля и меньше общего количества эпизодов.")
        self.current_episode = current_episode

    def reset_watching_progress(self) -> None:
        """
               Сброс прогресса просмотра сериала.

               Примеры:
               >>> series = Series("Доктор кто", 848)
               >>> series.reset_watching_progress()
               """
        self.current_episode = 0


class Rectangle:
    """
            Документация на класс.
            Класс описывает модель Прямоугольника.
        """
    def __init__(self, height: (int, float), width: (int, float)) -> None:

        """ Создание и подготовка к работе объекта "Прямоугольник"

                :param height: высота
                :param width: ширина

                Примеры:
                >>> rectangle = Rectangle(7, 8)  # инициализация экземпляра класса """

        if not isinstance(height, (int, float)):
            raise TypeError("Высота прямоугольника должна быть типа int.")
        if height <= 0:
            raise ValueError("Высота прямоугольника должна быть больше нуля.")
        self.height = height

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина прямоугольника должна быть типа int.")
        if width <= 0:
            raise ValueError("Ширина прямоугольника должна быть больше нуля.")
        self.width = width

    def calculate_perimeter(self) -> float:
        """
            Посчитать периметр прямоугольника.

            :return: периметр прямоугольника

            Примеры:
            >>> rectangle = Rectangle(7, 6)
            >>> P = rectangle.calculate_perimeter()
            """
        perimeter = (self.height + self.width) * 2
        return perimeter

    def calculate_square(self) -> float:
        """
            Посчитать площадь прямоугольника.

            :return: площадь прямоугольника

            Примеры:
            >>> rectangle = Rectangle(7, 6)
            >>> S = rectangle.calculate_square()
            """
        square = self.height * self.width
        return square


class Kettle:

    def __init__(self, kettle_volume: (int, float), water_volume: (int, float), temperature: (int, float)) -> None:
        """ Создание и подготовка к работе объекта "Чайник"

                :param kettle_volume: объем чайника
                :param water_volume: объем воды
                :param temperature: температура чайника

                Примеры:
                >>> kettle = Kettle(500, 250, 20)  # инициализация экземпляра класса """
        if not isinstance(kettle_volume, (int, float)):
            raise TypeError("Объем чайника должен быть типа int или float.")
        if kettle_volume <= 0:
            raise ValueError("Объем чайника должен быть больше 0.")
        self.kettle_volume = kettle_volume

        if not isinstance(water_volume, (int, float)):
            raise TypeError("Объем воды должен быть типа int или float.")
        if water_volume < 0 or water_volume > self.kettle_volume:
            raise ValueError("Объем воды не может быть отрицательным и не может быть больше объема чайника.")
        self.water_volume = water_volume

        if not isinstance(temperature, (int, float)):
            raise TypeError("Объем чайника должен быть типа int или float.")
        if temperature <= 0:
            raise ValueError("Объем чайника должен быть больше 0.")
        self.temperature = temperature

    def fill_kettle(self, water_volume: (int, float)) -> None:
        """
            Наполнить чайник водой.

            :water_volume: объем воды

            Примеры:
            >>> kettle = Kettle(500, 0, 20)
            >>> kettle.fill_kettle(250)"""

        if not isinstance(water_volume, (int, float)):
            raise TypeError("Объем воды должен быть типа int или float.")
        if water_volume < 0 or water_volume > self.kettle_volume:
            raise ValueError("Объем воды не может быть отрицательным и не может быть больше объема чайника.")
        self.water_volume = water_volume

    def boil_kettle(self) -> None:
        """
            Вскипятить чайник.

            Примеры:
            >>> kettle = Kettle(500, 250, 20)
            >>> kettle.boil_kettle()"""

        if self.water_volume == 0:
            raise ValueError("Нельзя кипятить пустой чайник!")
        self.temperature = 100


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

    pass
