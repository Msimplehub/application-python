# -*- coding: UTF-8 -*-

def printDef(para):
    print(para)
    
class MyUtil:
     def __init__(self):
         print("init")
     def utilDef(self, para):
         print(para)   
    
    
printDef("hello world");
myUtil = MyUtil()
myUtil.utilDef("nimeide")
