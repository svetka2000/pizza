from random import randint
import click

class pizza():
    """
    Родительский класс пицца
    """

    def __init__(self, size):
        self.tomato_sauce = True
        self.mozzarella = True
        if size == 'L' or size == 'XL':
            pass
        else:
            raise ValueError('Нужно выбрать размер L или XL')

    def __hash__(self):
        pass

    def __eq__(self, another):
        pass


class Margherita(pizza):
    """
    Пицца Маргарита размера L или XL
    """

    def __init__(self, size):
        self.size = size
        if self.size == 'L':
            self.tomato_sauce = 10
            self.mozzarella = 2
            self.tomatoes = 4
        elif self.size == 'XL':
            self.tomato_sauce = 15
            self.mozzarella = 3
            self.tomatoes = 12
        else:
            raise ValueError('Нужно выбрать размер L или XL')

    def __repr__(self):
        return f'Margherita {self.size}'

    def __dict__(self):
        """
        Рецепт
        """
        return {"tomato_sauce": self.tomato_sauce, "mozzarella": self.mozzarella, "tomatoes": self.tomatoes}

    def __hash__(self):
        """
        Делает пиццы одного размера тождественными
        """
        return hash((self.tomato_sauce, self.mozzarella, self.tomatoes, self.size))

    def __eq__(self, another):
        """
        Возможность сравнивать пиццы
        """
        eq_tomato_sauce = (self.tomato_sauce == another.tomato_sauce)
        eq_mozzarella = (self.mozzarella == another.mozzarella)
        eq_tomatoes = (self.tomatoes == another.tomatoes)
        return eq_tomato_sauce and eq_mozzarella and eq_tomatoes


class Pepperoni(pizza):
    """
    Пицца Пепперони размера L или XL
    """

    def __init__(self, size):
        self.size = size
        if self.size == 'L':
            self.tomato_sauce = 10
            self.mozzarella = 2
            self.pepperoni = 10
        elif self.size == 'XL':
            self.tomato_sauce = 15
            self.mozzarella = 3
            self.pepperoni = 20
        else:
            raise ValueError('Нужно выбрать размер L или XL')

    def __repr__(self):
        return f'Pepperoni {self.size}'

    def __dict__(self):
        """
        Рецепт
        """
        return {"tomato_sauce": self.tomato_sauce, "mozzarella": self.mozzarella, "pepperoni": self.pepperoni}

    def __hash__(self):
        """
        Делает пиццы одного размера тождественными
        """
        return hash((self.tomato_sauce, self.mozzarella, self.pepperoni, self.size))

    def __eq__(self, another):
        """
        Возможность сравнивать пиццы
        """
        eq_tomato_sauce = (self.tomato_sauce == another.tomato_sauce)
        eq_mozzarella = (self.mozzarella == another.mozzarella)
        eq_pepperoni = (self.pepperoni == another.pepperoni)
        return eq_tomato_sauce and eq_mozzarella and eq_pepperoni


class Hawaiian(pizza):
    """
    Пицца Гавайская размера L или XL
    """

    def __init__(self, size):
        self.size = size
        if self.size == 'L':
            self.tomato_sauce = 10
            self.mozzarella = 2
            self.chicken = 1
            self.pineapples = 1
        elif self.size == 'XL':
            self.tomato_sauce = 15
            self.mozzarella = 3
            self.chicken = 2
            self.pineapples = 2
        else:
            raise ValueError('Нужно выбрать размер L или XL')

    def __repr__(self):
        return f'Hawaiian {self.size}'

    def __dict__(self):
        """
        Рецепт
        """
        return {"tomato_sauce": self.tomato_sauce,
                "mozzarella": self.mozzarella, "chicken": self.chicken,
                "pineapples": self.pineapples}

    def __hash__(self):
        """
        Делает пиццы одного размера тождественными
        """
        return hash((self.tomato_sauce, self.mozzarella, self.chicken, self.size))

    def __eq__(self, another):
        """
        Возможность сравнивать пиццы
        """
        eq_tomato_sauce = (self.tomato_sauce == another.tomato_sauce)
        eq_mozzarella = (self.mozzarella == another.mozzarella)
        eq_chicken = (self.chicken == another.chicken)
        eq_pineapples = (self.pineapples == another.pineapples)
        return eq_tomato_sauce and eq_mozzarella and eq_chicken and eq_pineapples


def log(message):
    def decorator(function):
        def decorated(*args, **kwargs):
            print(message.format(*args, function(*args, **kwargs)))
            return function(*args, **kwargs)
        return decorated
    return decorator


@log('🍳 Готовим {} {} за {}с!')
def bake(pizza_: str, size: str) -> int:
    """Готовит пиццу, возвращает время приготовления"""
    return randint(1, 60)


@log('🛵 Доставили {} за {}с!')
def delivery(pizza_: str) -> int:
    """Доставляет пиццу, возвращает время доставки"""
    return randint(1, 60)


@log('🏠 Забрали {} за {}с!')
def pickup(pizza_: str) -> int:
    """Самовывоз, возвращает время время остывания пиццы, пока её не забрали"""
    return randint(1, 60)


@click.group()
def cli():
    pass


@cli.command()
@click.option('=delivery_', prompt='want to deliver?', default=False, is_flag=True)
@click.argument('pizza_')
@click.argument('size')
def order(pizza_: str, size: str, delivery_: bool):
    """Готовит и доставляет пиццу"""
    if f'{pizza_} {size}' in [str(subclass('L')) for subclass in pizza.__subclasses__()]:
            bake(pizza_, size)
    elif f'{pizza_} {size}' in [str(subclass('XL')) for subclass in pizza.__subclasses__()]:
            bake(pizza_, size)
    else:
        raise KeyError("Внимательнее смотри меню...")
    if delivery_:
        delivery(pizza_)


@cli.command()
def menu():
    """
    Выводит меню из всех наследников класса pizza размера L, XL
    '"""
    for subclass in pizza.__subclasses__():
        print("- ", subclass('XL'), ": ", ''.join('{} - {} gr, '.format(key, val)
              for key, val in sorted(subclass("XL").__dict__().items())))
        print("- ", subclass('L'), ": ", ''.join('{} - {} gr, '.format(key, val)
              for key, val in sorted(subclass("L").__dict__().items())))


if __name__ == '__main__':
    #menu()
    cli()

