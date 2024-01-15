#!/usr/bin/python3
"""
Base Class
"""
from json import dumps, loads
import csv


class Base:
    """ The Class Methodes """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """To Json Methode"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """From Json Methode"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save To File Methode"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        """Load To File Methode"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def create(cls, **dictionary):
        """Create Methode"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new_cre = Rectangle(1, 1)
        elif cls is Square:
            new_cre = Square(1)
        else:
            new_cre = None
        new_cre.update(**dictionary)
        return new_cre

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to file Methode"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Load From File Methode"""
        from models.rectangle import Rectangle
        from models.square import Square
        rect = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            read = csv.reader(f)
            for row in read:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                rect.append(cls.create(**d))
        return rect

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            tu = turtle.Turtle()
            tu.color((randrange(255), randrange(255), randrange(255)))
            tu.pensize(1)
            tu.penup()
            tu.pendown()
            tu.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            tu.pensize(10)
            tu.forward(i.width)
            tu.left(90)
            tu.forward(i.height)
            tu.left(90)
            tu.forward(i.width)
            tu.left(90)
            tu.forward(i.height)
            tu.left(90)
            tu.end_fill()

        time.sleep(5)
