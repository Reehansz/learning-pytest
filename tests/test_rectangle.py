import pytest
import os 
import sys
import math

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))

import shapes

class TestRectangle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.rectangle = shapes.Rectangle(10, 20)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del(self.rectangle)

    def test_area(self):
        result = self.rectangle.area()
        expected = self.rectangle.length * self.rectangle.width
        assert result == expected
    
    def test_perimeter(self):
        result = self.rectangle.perimeter()
        expected = 2 * self.rectangle.length * self.rectangle.width
        assert result == expected