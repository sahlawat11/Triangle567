# -*- coding: utf-8 -*-
"""
Updated Sept 8, 2019
The primary goal of this file is to test the valid triangles in Triangle.py
@author: Saransh Ahlawat
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    """Test class to test different types of triangles """

    def test_right_triangle_a(self):
        """function to check whether triangle (3, 4, 5) is a right triangle"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        """function to check whether triangle (5, 3, 4) is a right triangle"""
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def test_right_triangle_c(self):
        """function to check whether triangle (6, 8, 10) is a right triangle"""
        self.assertEqual(classify_triangle(6, 8, 10), 'Right', '6,8,10 is a Right triangle')

    def test_equilateral_triangles_a(self):
        """function to check whether triangle (1, 1, 1) is an equilateral triangle"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_equilateral_triangles_b(self):
        """function to check whether triangle (5, 5, 5) is an equilateral triangle"""
        self.assertEqual(classify_triangle(5, 5, 5), 'Equilateral', '5,5,5 should be equilateral')

    def test_equilateral_triangles_c(self):
        """function to check whether triangle (32, 32, 32) is an equilateral triangle"""
        self.assertEqual(classify_triangle(32, 32, 32),
                         'Equilateral', '32,32,32 should be equilateral')

    def test_scalene_triangles_a(self):
        """function to check whether triangle (3, 2, 4) is a scalene triangle"""
        self.assertEqual(classify_triangle(3, 2, 4), 'Scalene', '3,2,4 should be scalene')

    def test_scalene_triangles_b(self):
        """function to check whether triangle (10, 15, 12) is a scalene triangle"""
        self.assertEqual(classify_triangle(10, 15, 12), 'Scalene', '10,15,12 should be scalene')

    def test_scalene_triangles_c(self):
        """function to check whether triangle (7, 4, 10) is a scalene triangle"""
        self.assertEqual(classify_triangle(7, 4, 10), 'Scalene', '7,4,10 should be scalene')

    def test_isoceles_triangles_a(self):
        """function to check whether triangle (3, 5, 5) is an isosceles triangle"""
        self.assertEqual(classify_triangle(3, 5, 5), 'Isoceles', '3,5,5 should be Isoceles')

    def test_isoceles_triangles_b(self):
        """function to check whether triangle (3, 3, 5) is an isosceles triangle"""
        self.assertEqual(classify_triangle(3, 3, 5), 'Isoceles', '3,3,5 should be Isoceles')

    def test_isoceles_triangles_c(self):
        """function to check whether triangle (10, 10, 15) is an isosceles triangle"""
        self.assertEqual(classify_triangle(10, 10, 15), 'Isoceles', '10,10,15 should be Isoceles')

    def test_invalid_triangle_a(self):
        """function to check whether triangle (-1, 0, 1) is an invalid triangle"""
        self.assertEqual(classify_triangle(-1, 0, 1),
                         'InvalidInput', '-1, 0, 1 should not be a triangle')

    def test_invalid_triangle_b(self):
        """function to check whether triangle (0, 5, 4) is an invalid triangle"""
        self.assertEqual(classify_triangle(0, 5, 4),
                         'InvalidInput', '0,5,4 should not be a triangle')

    def test_invalid_triangle_c(self):
        """function to check whether triangle (3, 5, '') is an invalid triangle"""
        self.assertEqual(classify_triangle(3, 5, ''), 'InvalidInput', '3,5,"" is invalid input')

    def test_invalid_triangle_d(self):
        """function to check whether triangle ('', '', 20) is an invalid triangle"""
        self.assertEqual(classify_triangle('', '', 20), 'InvalidInput', '"","",20 is invalid input')

    def test_invalid_triangle_e(self):
        """function to check whether triangle ('test',
            'whatever', 'test1') is an invalid triangle
        """
        self.assertEqual(classify_triangle('test', 'whatever', 'test1'),
                         'InvalidInput', '"test","whatever","test1" is invalid input')

    def test_not_a_triangle_a(self):
        """function to check whether triangle (2, 3, 5) is an invalid triangle"""
        self.assertEqual(classify_triangle(2, 3, 5), 'NotATriangle', '"","",20 is not a triangle')

    def test_not_a_triangle_b(self):
        """function to check whether triangle (3, 5, 20) is an invalid triangle"""
        self.assertEqual(classify_triangle(3, 5, 20),
                         'NotATriangle', '3,5,20 should not be a triangle')

    def test_not_a_triangle_c(self):
        """function to check whether triangle (20, 3, 4) is an invalid triangle"""
        self.assertEqual(classify_triangle(20, 3, 4),
                         'NotATriangle', '20,3,4 should not be a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
