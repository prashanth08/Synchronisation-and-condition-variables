from threading import Thread, Lock, Condition
import time
import random

# a. Complete the implementation of the OneLaneBridge monitor below using
#    python locks and condition variables.  Your implementation should be able
#    to make progress if there are any cars that can cross.
#
# b. What fairness properties does your implementation have?  Under what
#    conditions (if any) can a thread starve?
#


north = 0
south = 1

dirFlag = 0 #initially set to north

class OneLaneBridge(object):
    """
    A one-lane bridge allows multiple cars to pass in either direction, but at any
    point in time, all cars on the bridge must be going in the same direction.

    Cars wishing to cross should call the cross function, once they have crossed
    they should call finished()
    """

    def __init__(self):
        # TODO
        self.lock = Lock()
        self.cv = Condition()


    def cross(self,direction):
        """wait for permission to cross the bridge.  direction should be either
        north (0) or south (1)."""
        if(direction == north && dirFlag == north)

        # TODO

        pass

    def finished(self,direction):
        # TODO
        pass


class Car(Thread):
    def __init__(self, bridge, car_id):
        Thread.__init__(self)
        self.direction = random.randrange(2)
        self.wait_time = random.uniform(0.1,0.5)
        self.bridge    = bridge
        self.car_id    = car_id

    def run(self):
        # drive to the bridge
        time.sleep(self.wait_time)
        print "Car %d: Trying to cross %s" % (self.car_id, "south" if self.direction else "north")
        # request permission to cross
        self.bridge.cross(self.direction)
        print "Car %d: Crossing" % self.car_id
        # drive across
        time.sleep(0.01)
        print "Car %d: Crossed" % self.car_id
        # signal that we have finished crossing
        self.bridge.finished(self.direction)
        print "Car %d: Finished crossing" % self.car_id


if __name__ == "__main__":

    judd_falls = OneLaneBridge()
    for i in range(10):
        Car(judd_falls, i).start()


##
## vim: ts=4 sw=4 et ai
##
