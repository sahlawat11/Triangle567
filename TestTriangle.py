# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
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
        self.assertEquals(classifyTriangle(3,2,4), 'Scalene', '3,2,4 should be scalene')
    
    def testScalenetrianglesB(self):
        self.assertEquals(classifyTriangle(10,15,12), 'Scalene', '10,15,12 should be scalene')

    def testScalenetrianglesC(self):
        self.assertEquals(classifyTriangle(7,4,10), 'Scalene', '7,4,10 should be scalene')
    
    def testIsoscelestrianglesA(self):
        self.assertEquals(classifyTriangle(3,5,5), 'Isosceles', '3,5,5 should be isosceles')

    def testIsoscelestrianglesB(self):
        self.assertEquals(classifyTriangle(3,3,5), 'Isosceles', '3,3,5 should be isosceles')

    def testIsoscelestrianglesC(self):
        self.assertEquals(classifyTriangle(10,10,15), 'Isosceles', '10,10,15 should be isosceles')

    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(-1,0,1), 'NotATriangle', '-1, 0, 1 should not be a triangle')

    def testNotATriangleB(self):
        self.assertEquals(classifyTriangle(0,5,4), 'NotATriangle', '0,5,4 should not be a triangle')

    def testNotATriangleC(self):
        self.assertEquals(classifyTriangle(3,5,20), 'NotATriangle', '3,5,20 should not be a triangle')
    
    def testNotATriangleD(self):
        self.assertEquals(classifyTriangle(20,3,4), 'NotATriangle', '20,3,4 should not be a triangle')

    def testInvalidTriangleA(self):
        self.assertEquals(classifyTriangle(3,5,''), 'InvalidInput', '3,5,"" is invalid input')

    def testInvalidTriangleB(self):
        self.assertEquals(classifyTriangle('','',20), 'InvalidInput', '"","",20 is invalid input')

    def testInvalidTriangleC(self):
        self.assertEquals(classifyTriangle('test','whatever','test1'), 'InvalidInput', '"test","whatever","test1" is invalid input')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

