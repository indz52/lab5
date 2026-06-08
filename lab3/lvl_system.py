"""
.. module:: lvl_system
   :platform: Unix, Windows
   :synopsis: Модуль для управления прогрессом и уровнями игровых персонажей.

.. moduleauthor:: Павлов Александр <your_email@example.com>
"""

class LvlSystem:
    """Класс для работы с системой уровней (LVL) главного героя.

    Отвечает за накопление опыта, повышение уровня и распределение бонусов.
    
    .. note::
       Текущая реализация использует приватные атрибуты для защиты данных игрока 
       от прямой модификации извне.

    :param hp: Начальное количество очков здоровья персонажа.
    :type hp: int or float
    :param gold: Начальное количество золота у персонажа.
    :type gold: int

    **Пример использования:**
    
    .. code-block:: python

       hero_lvl = LvlSystem(hp=100, gold=50)
       hero_lvl.add_xp(350)  # Автоматически повысит уровень
    """

    #: Количество очков опыта, необходимое для базового повышения уровня.
    #: Расчет итогового порога: :math:`current\_lvl \times lvl\_up\_points\_amount`
    __lvl_up_points_amount = 300

    def __init__(self, hp, gold) -> None:
        self.__current_lvl = 1
        self.__lvl_points = 0
        self.__hp = hp
        self.__gold = gold
    
    def show_lvl(self):
        """Выводит в консоль информацию о текущем уровне персонажа.
        
        .. seealso:: О методе повышения уровня см. в :meth:`lvl_up`.
        """
        print(f"Текущий уровень персонажа: {self.__current_lvl}")
    
    def lvl_up(self):
        """Проверяет условия и осуществляет повышение уровня героя.
        
        Если очков опыта достаточно, списывает их, увеличивает уровень на 1 
        и вызывает метод распределения наград :meth:`lvl_up_bonus`.
        """
        if self.__lvl_points >= self.__current_lvl * self.__lvl_up_points_amount:
            self.__lvl_points = self.__lvl_points - self.__current_lvl * self.__lvl_up_points_amount
            self.__current_lvl += 1
            print("Вы повысили уровень своего персонажа!", end=" ")
            self.show_lvl()
            self.lvl_up_bonus()
    
    def add_xp(self, amount):
        """Добавляет персонажу очки опыта (XP).

        После добавления автоматически запускается проверка на повышение уровня :meth:`lvl_up`.

        :param amount: Количество добавляемого опыта.
        :type amount: int
        
        .. todo:: Реализовать валидацию входящего значения (amount не должно быть отрицательным).
        """
        self.__lvl_points += amount
        self.lvl_up()
    
    def lvl_up_bonus(self):
        """Интерактивный метод выбора бонуса при достижении нового уровня.
        
        Предоставляет игроку выбор в консоли:
        
        1. Получить **100 золота**
        2. Увеличить максимальное здоровье на **20%**
        
        .. warning::
           Метод использует блокирующий ввод `input()`, что может остановить игровой цикл в реальной игре.
        """
        print("Выберите бонус за достижение нового уровня")
        print("1. 100 золота")
        print("2. 20% к здоровью")
        choice = input()
        if choice == "1":
            self.__gold += 100
        elif choice == "2":
            self.__hp = self.__hp * 1.2