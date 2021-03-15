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

    def testInvalidInputforValuesA(self):
        self.assertEqual(classifyTriangle(201,5,4),'InvalidInput','201,5,4 => Invalid input')

    def testInvalidInputforValuesB(self):
        self.assertEqual(classifyTriangle(3,205,4),'InvalidInput','3,205,4 => Invalid input')

    def testInvalidInputforValuesC(self):
        self.assertEqual(classifyTriangle(2,5,204),'InvalidInput','2,5,204 => Invalid input')

    def testInvalidInputforValuesD(self):
        self.assertEqual(classifyTriangle(0,5,4),'InvalidInput','0,5,4 => Invalid input')

    def testInvalidInputforValuesE(self):
        self.assertEqual(classifyTriangle(1,-5,4),'InvalidInput','1,-5,4 => Invalid input')

    def testInvalidInputforValuesF(self):
        self.assertEqual(classifyTriangle(6,5,-4),'InvalidInput','6,5,-4 => Invalid input')

    def testInvalidInputforObjectTypeA(self):
        self.assertEqual(classifyTriangle("a",2,3), 'InvalidInput','a,2,3 => Invalid input')

    def testInvalidInputforObjectTypeB(self):
        self.assertEqual(classifyTriangle(2,"a",3), 'InvalidInput','2,a,3 => Invalid input')

    def testInvalidInputforObjectTypeC(self):
        self.assertEqual(classifyTriangle(3,2,"c"), 'InvalidInput','3,2,c => Invalid input')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be Scalene')

    def testIsocelesTriangle(self):
        self.assertEqual(classifyTriangle(5,5,4),'Isoceles','5,5,4 should be Isoceles')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

