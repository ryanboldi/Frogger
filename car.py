import random
import math

class Car(object):
    def __init__(self, lanes):
        self.lanes = math.floor(random.random()*lanes)
        