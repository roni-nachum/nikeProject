import unittest

from jb_60.function_example.utils import utils

class multipleExample(unittest.TestCase):

    def setUp(self):
        print('into set up')
        self.num1=2
        self.num2=5

    def test_add(self ):
        print('test summary')

        assert self.num1+self.num2==3, 'The summery of 1 and 2 is not 3'

    def test_minus(self ):
        print('test diff')

        assert self.num1-self.num2 ==3, 'The diff of 4 and 1 is not 3'

    def test_multiple_with_error(self):
        num1 = 3
        num2 = 2
        assert self.num1*self.num2 ==5, 'The result of multiple action is not as expected'

    def test_city1(self):
        city1 = 'london'
        assert len(city1)==6, 'wrong length for city london'

    def test_city2(self):
        city2 = 'paris'
        assert len(city2)==6, 'wrong length for city paris'

    def test_city3(self):
        city3 = 'lod'
        assert len(city3)==6, 'wrong length for the city lod'
