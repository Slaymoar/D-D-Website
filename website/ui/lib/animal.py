#!/usr/bin/python


class Animal(object):

    name = "John Doe"

    def __init__(self, *args, **kwargs):
        name = kwargs.get('name', None)
        if name is not None:
            self.name = name

    def hello(self):
        print "Hello, my name is {}".format(self.name)

