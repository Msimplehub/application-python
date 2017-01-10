#ecoding=utf-8

"""
    pythons study time
        
        create by 9:58 2016-7-22 M.simple
"""

import time
import calendar

class MyTimer:
    
    def timeMethod(self):
        print "当前时间的时间戳:", time.time()
        print "time local:", time.localtime(time.time())
        print "time default format:", time.asctime(time.localtime(time.time()))
        print "time self format:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print "time zone:", time.altzone;
        
    def calendarMethod(self):
        print "2016年7月份日历", calendar.month(2016, 7)
        
    def test(self):
        print "M.simpl test"
  
mytimer = MyTimer()
mytimer.timeMethod()
mytimer.calendarMethod()










       