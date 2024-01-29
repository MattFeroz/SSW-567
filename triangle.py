import unittest
import math

def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    # First, test if the values create a triangle, then test what type of triangle it is
    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotTriangle' 
    
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2+c**2 == b:
        return 'Right'

    if a == b and b == c:
        return 'Equilateral'
    
    elif a == b or b == c or a == c:
        return 'Isoceles'
    
    else:
        return 'Scalene'
   
    
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testRightTriangle(self): # test invalid inputs
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testEquilateralTriangle(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is an Equilateral triangle')
        
    def testIsocelesTriangle(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 is an Isoceles triangle')

    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(4,2,3),'Scalene','4,2,3 is an Scalene triangle')
        
    def testNotTriangle(self):
        self.assertEqual(classifyTriangle(1,2,30), 'NotTriangle', '1, 2, 30 is not a triangle')
    
    #def testInput(self):
        #self.assertFalse(classifyTriangle(null,null,null), 'Input', 'no numbers are inputed')

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(3,3,3)
    runClassifyTriangle(7,5,9)
    runClassifyTriangle(9,16,25)
    runClassifyTriangle(100,4,2)
    #runClassifyTriangle()
    
    #unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    

       