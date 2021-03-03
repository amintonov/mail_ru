import pytest
d = {'a' : 1,
     'b' : 2,
     'c' : 3}

s = {1, 2, 3, 4, 5, 6, 7}

# Тесты для словарей
def dictionary_test_1(dictionary, key):
    """
    Ключа не существует внутри словаря.
    :return: error
    """
    assert dictionary[key]

dictionary_test_1(d, 'd')

def dictionary_test_2(dictionary):
    try:
        assert next(d)
    except TypeError:
        pass

dictionary_test_2(d)

@pytest.mark.parametrize(
"keys",
[[0], [1], [100]])
def dictionary_test_3(d, keys):
    assert d[keys]
keys = [[0], [1], [100]]

dictionary_test_3(d, keys)

# Тесты для множеств
def set_test_1(s, ind):
    try:
        assert s[ind]
    except TypeError:
        pass

set_test_1(s, 10)

def set_test_2(s, char):
    assert s.count(char)

set_test_2(s, '1')

@pytest.mark.parametrize(
"terms",
[{0}, {1, 2}])
def set_test_3(s, terms):
    assert s + terms

set_test_3(s, terms=[{0}, {1, 2}])
