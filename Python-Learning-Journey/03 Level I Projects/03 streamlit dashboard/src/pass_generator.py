import random
import string
from abc import ABC, abstractclassmethod

import nltk
from nltk.corpus import words


nltk.download('words')


class StrongPasswordGenerator():
    """for inheritance and abstract classes
    """
    @abstractclassmethod

    def generate(self):
        pass


import random
import string
from abc import ABC, abstractclassmethod

import nltk


class StrongPasswordGenerator():
    """for inheritance and abstract classes
    """
    @abstractclassmethod

    def generate(self):
        pass


class RandomPasswordGenerator(StrongPasswordGenerator):
    """generate Random password include Letters, digits, symbols
    you can see what in letters with defind an object like 'test' and call test.letter

    Args:
        StrongPasswordGenerator : for inhritance
    """
    def __init__(self, number: int=8, include_number: bool=False, include_symbol: bool=False):
        self.number = number
        self.include_number = include_number
        self.include_symbol = include_symbol
    
        self.letters = string.ascii_letters
        if self.include_number:
            self.letters += string.digits
        
        if self.include_symbol:
            self.letters += string.punctuation
    
    def generate(self, ):
        return ''.join(random.choice(self.letters) for _ in range(self.number))


class MemorablePassword(StrongPasswordGenerator):
    """generate memoreble words for password
    you can get it your own words


    """
    def __init__(self, number = 5, devider = "-", have_upper = False, list_of_word = []):
        self.number = number
        self.devider = devider
        self.have_upper = have_upper
        self.list_of_word = list_of_word

    def generate(self, ):
        if self.list_of_word:
            if len(self.list_of_word) < self.number:
                return f"that's bullshit! You want me to choose from {len(self.list_of_word)} words to {self.number}!!!!"
        
        if self.list_of_word:
            _word = self.list_of_word
        else:
            _word = [random.choice(words.words()) for _ in range(self.number)]
        
        if self.have_upper:
            _words = []

            for _ in _word:
                choice = random.randint(0, 1)
                if choice:
                    _words.append(_.upper())
                else:
                    _words.append(_)

            _word = _words
        
        password = self.devider.join(_word)
        return password
    
class PinCode(StrongPasswordGenerator):
    """generate digit password (only number)
    """
    def __init__(self, number: int=8):
        self.number = number
    
    def generate(self, ):
        self._numbers = [str(random.randint(0, 9)) for _ in range(self.number)]
        return int(''.join(self._numbers))

