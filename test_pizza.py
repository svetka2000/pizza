from pizza import pizza, Margherita, Pepperoni, Hawaiian, pickup, bake, delivery
import pytest


def test_Margherita_L():
    assert str(Margherita('L')) == 'Margherita L'

def test_Margherita_XL():
    assert str(Margherita('XL')) == 'Margherita XL'

def test_Pepperoni_L():
    assert str(Pepperoni('L')) == 'Pepperoni L'

def test_Pepperoni_XL():
    assert str(Pepperoni('XL')) == 'Pepperoni XL'

def test_Hawaiian_L():
    assert str(Hawaiian('L')) == 'Hawaiian L'

def test_Hawaiian_XL():
    assert str(Hawaiian('XL')) == 'Hawaiian XL'

def test_Margherita_wrong_size():
    with pytest.raises(ValueError):
        str(Margherita('S'))

def test_Pepperoni_wrong_size():
    with pytest.raises(ValueError):
        str(Pepperoni('S'))

def test_Hawaiian_wrong_size():
    with pytest.raises(ValueError):
        str(Hawaiian('S'))

def test_eq_Pepperoni():
    A = Pepperoni('XL')
    B = Pepperoni('XL')
    assert A == B

def test_noeq_Hawaiian():
    A = Hawaiian('XL')
    B = Hawaiian('L')
    assert A != B

def test_eq_Margherita():
    A = Margherita('L')
    B = Margherita('L')
    assert A == B

def test_pickup():
    assert type(pickup('pizza')) is int

def test_delivery():
    assert type(delivery('pizza')) is int

def test_bake():
    assert type(bake('pizza', 'XL')) is int

def test_dict_Margherita():
    A = Margherita('XL')
    assert A.__dict__() == {"tomato_sauce": 15, "mozzarella": 3, "tomatoes": 12}

def test_dict_Pepperoni():
    A = Pepperoni('XL')
    assert A.__dict__() == {"tomato_sauce": 15, "mozzarella": 3, "pepperoni": 20}

def test_dict_Hawaiian():
    A = Hawaiian('XL')
    assert A.__dict__() == {"tomato_sauce": 15, "mozzarella": 3, "chicken": 2, "pineapples": 2}

def test_pizza():
    with pytest.raises(ValueError):
        str(pizza('S'))
    assert str(pizza('L'))

def test_hash_Pepperoni():
    A = Pepperoni('XL')
    B = Pepperoni('XL')
    assert A.__hash__() == B.__hash__()

def test_hash_Hawaiian():
    A = Hawaiian('XL')
    B = Hawaiian('XL')
    assert A.__hash__() == B.__hash__()

def test_hash_Margherita():
    A = Margherita('L')
    B = Margherita('L')
    assert A.__hash__() == B.__hash__()