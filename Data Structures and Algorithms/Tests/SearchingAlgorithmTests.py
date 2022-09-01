import sys
import math
from time import perf_counter
import queue
from collections import deque
from Methods import Passenger, Plane, Seats, WaitList
with open("Flights.txt", "r") as f, open("Flights2.txt", "w") as n: # Converts Flights.txt into Classes
    lines = f.readlines()
    lines = [line.replace(' ', ' ') for line in lines]
    n.writelines(lines)
    arr = []
    arr2 = []
    arr3 = []
    arr4 = []
    arr5 = []
    arr6 = []
    for f in range(0, 7):
        a = lines[f]
        arr.append(a.split("\n")[0])
    arr3.append(arr[6])
    arr[4] = [int(s) for s in arr[4] if s.isdigit()] # convert to int
    arr[5] = [int(s) for s in arr[5] if s.isdigit()]
    for y in range(9, 16):
        aa = lines[y]
        arr2.append(aa.split("\n")[0])
    arr4.append(arr2[4])
    arr5.append(arr2[5])
    arr6.append(arr2[6])
def ConvertListToInt(oldlist, newlist):
    a = ','.join(oldlist)
    b = [int(s) for s in a.split() if s.isdigit()]
    newlist = b
    return newlist
dict1 = {}
emp1 = []
arr3 = ConvertListToInt(arr3, emp1)
arr4 = ConvertListToInt(arr4, emp1)
arr5 = ConvertListToInt(arr5, emp1)
arr6 = ConvertListToInt(arr6, emp1)
arr[6] = arr3
arr2[4] = arr4
arr2[5] = arr5
arr2[6] = arr6
# CONVERT TEXT FILE - CONVERT TEXT FILE - CONVERT TEXT FILE - CONVERT TEXT FILE - CONVERT TEXT FILE - CONVERT TEXT FILE - 

# PLANES - PLANES - PLANES - PLANES - PLANES - PLANES - PLANES - PLANES - PLANES - PLANES - PLANES - 
allPlanes = []
allPlanes.append(Plane(arr[0], arr[1], arr[2], arr[3], (arr[4], arr[5], arr[6])))
allPlanes.append(Plane(arr2[0], arr2[1], arr2[2], arr2[3], (arr2[4], arr2[5], arr2[6])))

# PASSENGERS - PASSENGERS - PASSENGERS - PASSENGERS - PASSENGERS - PASSENGERS - PASSENGERS - PASSENGERS - 
allPassengers = []

# SEATS - SEATS - SEATS - SEATS - SEATS - SEATS - SEATS - SEATS - SEATS - SEATS - SEATS - SEATS - SEATS - 
allSeats = []
allSeats.append(Seats(arr[0], arr[4], arr[5], arr[6]))
allSeats.append(Seats(arr2[0], arr2[4], arr2[5], arr2[6]))

# WAITLIST PLANE1 - WAITLIST PLANE1 - WAITLIST PLANE1 - WAITLIST PLANE1 - WAITLIST PLANE1 - WAITLIST PLANE1 - 
first101 = queue.Queue()
business101 = queue.Queue()
economy101 = queue.Queue()
# WAITLIST PLANE2 - WAITLIST PLANE2 - WAITLIST PLANE2 - WAITLIST PLANE2 - WAITLIST PLANE2 - WAITLIST PLANE2 - 
first700 = queue.Queue()
business700 = queue.Queue()
economy700 = queue.Queue()

# WAIT LIST - WAIT LIST - WAIT LIST - WAIT LIST - WAIT LIST - WAIT LIST - WAIT LIST - WAIT LIST - WAIT LIST - 
allWaitList = []
allWaitList.append(WaitList(arr[0], first101, business101, economy101))
allWaitList.append(WaitList(arr2[0], first700, business700, economy700))

class Node:
    def __init__(self, key):
        self.key = key
        self.child = []

def newNode(key):
    temp = Node(key)
    return temp

def PrintTree(root, flightnumber):
    for x in allPlanes:
        if x.flight_num == flightnumber:
            axy = [x for x in x.seats]
            i_departure_airport = x.departure_airport
            i_departure_date = x.departure_date
            i_arrival_airport = x.arrival_airport
    # Standard level order traversal code
    # using queue
    q = [] # Create a queue
    q.append(root); # Enqueue root
    while (len(q) != 0):
        n = len(q);
        # If this node has children
        while (n > 0):
            # Dequeue an item from queue and print it
            p = q[0]
            q.pop(0)
            # Enqueue all children of the dequeued item
            for i in range(len(p.child)):
                q.append(p.child[i])
            print(p.key, end=' ')
            n -= 1
        print() # Print new line between two levels

def CreateTree(root, flightnumber):
    for x in allPlanes:
        if x.flight_num == flightnumber:
            axy = [x for x in x.seats]
            i_departure_airport = x.departure_airport
            i_departure_date = x.departure_date
            i_arrival_airport = x.arrival_airport
    #root = Node(flightnumber);
    (root.child).append(newNode("Seats"));
    (root.child).append(newNode(i_departure_airport));
    (root.child).append(newNode(i_departure_date));
    (root.child).append(newNode(i_arrival_airport));
    (root.child[0].child).append(newNode(dict.fromkeys(axy[0])));
    (root.child[0].child).append(newNode(dict.fromkeys(axy[1])));
    (root.child[0].child).append(newNode(dict.fromkeys(axy[2])));

flight101 = Node("101")
flight700 = Node("700")
CreateTree(flight101, "101")
CreateTree(flight700, "700")
allNodes = []
allNodes.append(flight101)
allNodes.append(flight700)

def linear_search(list, var):
    for x in range(len(list)): # Big O: O(N)
        if list[x] == var:
            return x # Big O: O(1)
    print("Not Found")
    # Big O: N * O(1) = O(N)

def BinarySearch(lys, val):
    first = 0 # Big O: O(1)
    last = len(lys)-1 # Big O: O(1)
    index = -1 # Big O: O(1)
    while (first <= last) and (index == -1):
        # Finds the middle position
        mid = (first+last)//2
        # result of binary search
        if lys[mid] == val:
            index = mid
            # drop right
        else:
            if val<lys[mid]:
                last = mid -1
                # drop left
            else:
                first = mid +1
    # empty
    return index

def JumpSearch (lys, val):
    length = len(lys)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lys[left] <= val:
        right = min(length - 1, left + jump)
        if lys[left] <= val and lys[right] >= val:
            break
        left += jump;
    if left >= length or lys[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and lys[i] <= val:
        if lys[i] == val:
            return i
        i += 1
    return -1

# Best Case: Searching for key element at the first index
# Worst Case: Search for a key element at the last index
# Average Case: All possible case time % number of cases -- May not always be possible

# Best Case:
# O(1)

name = "Harold" # Name being searched for
for x in allWaitList:
    if "101" == x.flight_num:
        for y in x.classes.items():
            if y[0] == "First":
                y[1].put("Adam")
                y[1].put("Benjy")
                y[1].put("Charlie")
                y[1].put("Danny")
                y[1].put("Elley")
                y[1].put("Foxtrot")
                y[1].put("Gilbert")
                y[1].put("Harold")
                y[1].put("Islington")
                y[1].put("Jerry")
                print("List:",[x for x in y[1].queue])
                l0 = perf_counter()
                print("Linear Search:",linear_search(y[1].queue, name))
                l1 = perf_counter()
                b0 = perf_counter()
                print("Binary Search:",BinarySearch(y[1].queue, name))
                b1 = perf_counter()
                j0 = perf_counter()
                print("Jump Search:",BinarySearch(y[1].queue, name))
                j1 = perf_counter()


LinearTotal = l1-l0
BinaryTotal = b1-b0
JumpTotal = j1-j0
print("Time Taken With Linear Search:",LinearTotal) # O(n)
print("Time Taken With Binary Search:",BinaryTotal) # O(log n)
print("Time Taken With Jump Search:",JumpTotal) # O (√n)