#!/usr/bin/env python
import unittest
from pyweek13 import generate_fib

class TestFab(unittest.TestCase):
   def test_fib_1(self):
      a = [1, 1, 2, 3, 5, 8, 13]
      res = []
      pyweek13.raw_input = 7
      res = generate_fib(7)
      self.assertEqual(res, a)

if __name__ == '__main__':
   unittest.main()
