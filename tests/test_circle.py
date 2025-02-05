import pytest
import math
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))
import shapes

class TestCircle :

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del(self.circle)

    def test_Area(self):
        result = self.circle.area()
        expected = math.pi * self.circle.radius ** 2
        assert result==expected

    def test_Perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected