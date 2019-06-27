class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        class A:
            def __init__(self):
                self._internal = 0  # An internal attribute
                self.public = 1  # A public attribute

    def public_method(self):
        '''
        A public method
        '''
        pass

    def _internal_method(self):
        pass
        class B:
            def __init__(self):
                self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()
        class C(B):
            def __init__(self):
                super().__init__()
                self.__private = 1  # Does not override B.__private

    # Does not override B.__private_method()
    def __private_method(self):
        pass
        class Person:
            def __init__(self, first_name):
                self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")
        class Person1:
            def __init__(self, first_name):
                self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)


print(Person1.name.fget)
print(Person1.name.fset)
print(Person1.name.fdel)


class Circle:
    """动态计算的property"""

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius ** 2


c = Circle(4.0)
print(c.radius)
print(c.area)  # Notice lack of ()