#-------------------------------------------------------------------------------
# Name:        RepeatTimer
# Purpose:
#
# Author:      elbar
#
# Created:     26/03/2012
# Copyright:   (c) elbar 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import threading

class RepeatTimer(threading.Thread):

    def __init__(self, interval, function, iterations=0, args=[], kwargs={}):
        threading.Thread.__init__(self)
        self.interval = interval
        self.function = function
        self.iterations = iterations
        self.args = args
        self.kwargs = kwargs
        self.finished = threading.Event()

    def run(self):
        count = 0
        while not self.finished.is_set() and (self.iterations <= 0 or count < self.iterations):
            self.finished.wait(self.interval)
            if not self.finished.is_set():
                self.function(*self.args, **self.kwargs)
                count += 1

    def cancel(self):
        self.finished.set()

