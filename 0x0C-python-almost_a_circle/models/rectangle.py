#!/usr/bin/python3
"""The Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Define The Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisation"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width Methode"""
        return self.__width

    @width.setter
    def width(self, value):
        """The width setter"""
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """The Height Methode"""
        return self.__height

    @height.setter
    def height(self, value):
        """The height setter"""
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """The X Methodes"""
        return self.__x

    @x.setter
    def x(self, value):
        """The X Setter"""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """The Y Methode"""
        return self.__y

    @y.setter
    def y(self, value):
        """The Y setter"""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """The Method for validating the value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """The area Methode"""
        return self.width * self.height

    def display(self):
        """Methode Prints string representation of this rectangle"""
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        """Methode Returns string info about this rectangle"""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Method that updates instance attributes via */**args"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Methode Updates instance attributes via no-keyword & keyword args"""
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Methode Returns dictionary representation of this class"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
