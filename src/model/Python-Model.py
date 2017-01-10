#ecoding=utf-8

"""
    python model Example
    
        create by 11:02 2016-7-22 M.simple
"""
import math

grobalVar = 2000

def testMethod():
    global  grobalVar 
    grobalVar = grobalVar + 1
    
    return grobalVar

'''
    This method return this model`s model/class/varibal/mehod
    @return: list
'''
def modelDir():
    print "model dir:", dir(math)
    
def globalsAndLocals():
    print "Can get GolbalVar:", globals()
    
print "result:", testMethod()
print "model dir result", modelDir()
globalsAndLocals()

        