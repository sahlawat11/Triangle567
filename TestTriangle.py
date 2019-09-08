# -*- coding: utf-8 -*-
"""
Updated Sept 8, 2019
The primary goal of this file is to test the valid triangles in Triangle.py

@author: Saransh Ahlawat
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(6,8,10), 'Right', '6,8,10 is a Right triangle')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(5,5,5), 'Equilateral', '5,5,5 should be equilateral')

    def testEquilateralTrianglesC(self): 
        self.assertEqual(classifyTriangle(32,32,32), 'Equilateral', '32,32,32 should be equilateral')

    def testScalenetrianglesA(self):
        self.assertEqual(classifyTriangle(3,2,4), 'Scalene', '3,2,4 should be scalene')
    
    def testScalenetrianglesB(self):
        self.assertEqual(classifyTriangle(10,15,12), 'Scalene', '10,15,12 should be scalene')

    def testScalenetrianglesC(self):
        self.assertEqual(classifyTriangle(7,4,10), 'Scalene', '7,4,10 should be scalene')
    
    def testIsocelestrianglesA(self):
        self.assertEqual(classifyTriangle(3,5,5), 'Isoceles', '3,5,5 should be Isoceles')

    def testIsocelestrianglesB(self):
        self.assertEqual(classifyTriangle(3,3,5), 'Isoceles', '3,3,5 should be Isoceles')

    def testIsocelestrianglesC(self):
        self.assertEqual(classifyTriangle(10,10,15), 'Isoceles', '10,10,15 should be Isoceles')

    def testInvalidTriangleA(self): 
        self.assertEqual(classifyTriangle(-1,0,1), 'InvalidInput', '-1, 0, 1 should not be a triangle')

    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle(0,5,4), 'InvalidInput', '0,5,4 should not be a triangle')

    def testInvalidTriangleC(self):
        self.assertEqual(classifyTriangle(3,5,''), 'InvalidInput', '3,5,"" is invalid input')

    def testInvalidTriangleD(self):
        self.assertEqual(classifyTriangle('','',20), 'InvalidInput', '"","",20 is invalid input')

    def testInvalidTriangleE(self):
        self.assertEqual(classifyTriangle('test','whatever','test1'), 'InvalidInput', '"test","whatever","test1" is invalid input')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(2,3,5), 'NotATriangle', '"","",20 is not a triangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(3,5,20), 'NotATriangle', '3,5,20 should not be a triangle')
    
    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(20,3,4), 'NotATringle', '20,3,4 should not be a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

