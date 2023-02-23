int_variable = 6  # int
assert isinstance(int_variable, int)

float_variable = 6.6     # float
assert isinstance(float_variable, float)

string_variable = '6.6'  # string
assert isinstance(string_variable, str)

bool_variable = True  # bool
assert isinstance(bool_variable, bool)

list_variable = ['66', 66]  # list
assert isinstance(list_variable, list)

tuple_variable = ('66', 66, '66') # tuple
assert isinstance(tuple_variable, tuple)

set_variable = {1, 6}  # set
assert isinstance(set_variable, set)

dict_variable = {'number': 66, 'name':'Dmitry'}  # dict
assert isinstance(dict_variable, dict)
#------------------------------------------------------------>>>

def difference_of_two_numbers(first, second):
    """Возвращает разницу между первым и вторым аргументом"""

    return abs(first-second)
    pass
assert difference_of_two_numbers(2, 1) == 1
assert difference_of_two_numbers(4, 1) == 3
assert difference_of_two_numbers(10, 0) == 10
assert difference_of_two_numbers(-5, -6) == 1
#------------------------------------------------------------>>>
def condition_function(input_number):
    """
    Если входное число меньше либо равно 0, то умножить его на 2.
    В противном случае, если число больше 0, но меньше или равно 10, умножить на 3.
    Во всех прочих случаях поделить на 10.
    """
    if input_number <= 0:
        return input_number * 2
    elif input_number > 0 and input_number <= 10: 
        return input_number * 3
    else:
        return input_number / 10
    pass

assert condition_function(0) == 0
assert condition_function(-1) == -2
assert condition_function(1) == 3
assert condition_function(10) == 30
assert condition_function(11) == 1.1
assert condition_function(20) == 2
#------------------------------------------------------------>>>
def calculator(number_1, operation, number_2):
    """
    Простой оператор, способный выполнять операции +, -, *, /.
    На входе первое число, операция в виде строки и второе число.
    
    Пример: 
    >>> calculator(1, "+", 1)
    >>> 2
    """
    if operation == "+":
        return number_1 + number_2
    elif operation == "-":
        return number_1 - number_2
    elif operation == "*":
        return number_1 * number_2
    elif operation == "/":
        return number_1 / number_2
    pass

assert calculator(1, "+", 2) == 3
assert calculator(3, "-", 1) == 2
assert calculator(4, "*", 3) == 12
assert calculator(2, "/", 2) == 1
#------------------------------------------------------------>>>
def number_of_unique_elements(input_list):
    """
    Считает количество уникальных элементов в листе.
    """
    uniq = set(input_list)
    return len(uniq)
    pass

assert number_of_unique_elements([1, 2, 3]) == 3
assert number_of_unique_elements([1] * 93) == 1
assert number_of_unique_elements(list(range(1000))) == 1000
#------------------------------------------------------------>>>
def counter(input_list):
    """
    Считает количество вхождений каждого из элементов листа.
    Возвращает словарь вида {число: количество вхождений}
    
    Замечание (!): встроенным в collections Counter'ом пользоваться нельзя
    
    Например:
    counter([1, 1, 2, 3]) вернет {1: 2, 2: 1, 3: 1}
    """
    co = {}
    for a in input_list:
        if a not in co:
            co[a] = 1
        else:
            co[a] += 1
    return co
    pass

assert counter([1, 1, 1, 2, 3]) == {1: 3, 2: 1, 3: 1}
assert counter([1] * 1000) == {1: 1000}
assert counter([1, 3, 5] * 100) == {1: 100, 3: 100, 5: 100}
#------------------------------------------------------------>>>
def multiply_nums(input_string):
    """
    Перемножить числа, переданные в строке, перечисленные через запятую.
    
    hint: можно использовать метод .split()
    """
    result = 1
    nums = input_string.split(",")
    for num in nums:
        result *= int(num)
    return result
    pass

assert multiply_nums("2, 3") == 6
assert multiply_nums("1, 1, 1, 1, 1, 1, 1") == 1
assert multiply_nums("345, 4576, 794, 325, 0") == 0
#------------------------------------------------------------>>>
from math import *
def custom_function(x):
    """
    Реализуйте функцию, описанную выше.
    """
    y = sin(x) * cos(x)
    return y 
    pass

assert round(custom_function(1), 3) == 0.455
assert round(custom_function(1.5), 3) == 0.071
assert round(custom_function(2), 3) == -0.378
assert custom_function(0) == 0
#------------------------------------------------------------>>>
def custom_function_1(x, n):
    """
    Реализуйте функцию, описанную выше.
    """
    s = 1
    for i in range(1, n + 1):
        y = (((i + 2)**x + log(x)) / (x**2 + 4 * i))  
        s *= y
    return s
    pass

assert round(custom_function_1(2, 3), 3) == 2.707
assert round(custom_function_1(3, 2), 3) == 8.277
assert round(custom_function_1(3, 3), 3) == 49.7
#------------------------------------------------------------>>>
class MyList:
    def __init__(self, mas):
        self.mas = mas
        pass
    
    def return_sum(self):
        """
        Возвращает сумму всех элементов сохраненного листа.
        Пользоваться sum нельзя!
        """
        a = 0
        for el in self.mas:
            a += el
        return a
        pass
    
    def make_reverse(self):
        """
        Разворачивает сохраненный лист.
        """
        return self.mas[::-1]
        pass
    
    def make_slice(self, start, stop):
        """
        Делает слайсинг сохраненного листа.
        """
        return self.mas[start:stop]
        pass
    
a = MyList([1, 2, 3, 4])
assert a.return_sum() == 10
assert a.make_reverse() == [4, 3, 2, 1]
assert a.make_slice(0, 2) == [1, 2]

b = MyList([5, 6, 6, 5])
assert b.return_sum() == 22
assert b.make_reverse() == [5, 6, 6, 5]
assert b.make_slice(1, 2) == [6]