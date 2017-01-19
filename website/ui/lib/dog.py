#!/usr/bin/python

import animal
import time

class Dog(animal.Animal):

    breed = "Shitzu"

    def __init__(self, *args, **kwargs):
        breed = kwargs.get('breed', None)
        if breed is not None:
            self.breed = breed
        super(Dog, self).__init__(*args, **kwargs)

    def hello(self):
        print "Hello, my name is {} and I am a {} ".format(self.name, self.breed)
        print "The time is: {}".format(time.time())

    def say_breed(self):
        print "I am a {}".format(self.breed)
