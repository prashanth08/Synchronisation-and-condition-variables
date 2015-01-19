from __future__ import with_statement
from threading import Thread, Lock

# This program simulates a postmodern game between two teams.  Each team
# presses their button as fast as they can.  There is a counter that starts at
# zero; the red team's increases a counter, while the blue team's button
# decreases the counter.  They each get to press their button 10000 times. If the
# counter ends up positive, the read team wins; a negative counter means the blue
# team wins.
#
# a. This game is boring: it should always end in a draw.  However, the provided
#    implementation is not properly synchronized.  When both threads terminate,
#    what are the largest and smallest possible scores?
#
# b. What other values can the score have when both threads have terminated?
#
# c. Add appropriate synchronization such that updates to the counter
#    occur in a critical section, ensuring that the energy level is
#    always at 0 when the two threads terminate.
#
#    Your synchronization must still allow interleaving between the two threads.


counter = 0

class Button(Thread):
    def __init__(self,lock):
        self.lock = lock
        Thread.__init__(self,target= self.run)

    def run(self):
        global counter
        for i in range(10000):
            self.lock.acquire()
            counter += 1
            self.lock.release()

class Team(Thread):
    def __init__(self,lock):
        self.lock = lock
        Thread.__init__(self,target=self.run)

    def run(self):
        global counter
        for j in range(10000):
            self.lock.acquire()
            counter -= 1
            self.lock.release()

l= Lock()
w1 = Button(l)
w2 = Team(l)
w1.start()
w2.start()
w1.join()
w2.join()

print("The counter is " + str(counter))

##
## vim: ts=4 sw=4 et ai
##
