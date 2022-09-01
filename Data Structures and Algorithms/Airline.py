print("===============================================================================================================")
# CONVERT TEXT FILE - CONVERT TEXT FILE - CONVERT TEXT FILE - CONVERT TEXT FILE - CONVERT TEXT FILE - CONVERT TEXT FILE - 

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


# GENERAL TREE - GENERAL TREE - GENERAL TREE - GENERAL TREE - GENERAL TREE - GENERAL TREE - GENERAL TREE - 
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
# GENERAL TREE - GENERAL TREE - GENERAL TREE - GENERAL TREE - GENERAL TREE - GENERAL TREE - GENERAL TREE - 

# FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 
def FindNextSeat2(dict):
    counter = 0
    for x in dict.items():
        if x[1] == None:
            return x[0]

def Main():
    # Main Function that allows for S C P F input
    value = True
    a = input("\nWelcome to DSA Airlines, What would you like to do?\n(S) - Schedule / (C) - Cancel / (P) - Passenger Status / (F) - Flight Status\n:").lower()
    if a == "s":
        print("\nSchedule")
        AddPassenger()
    elif a == "c":
        print("\nCancel")
        Cancel()
    elif a == "p":
        print("\nPassenger Status")
        PassengerStatus()
    elif a == "f":
        print("\nFlight Status")
        FlightStatus()
    else:
        print("Wrong Input, Returning to Main.")
        Main()
    
def PassengerExists(passengerName):
    count = 0
    for x in allPassengers:
        if x.name == passengerName:
            return False
        else:
            pass
    allPassengers.append(Passenger(passengerName))

def Cancel():
    # Passenger 1
    # Class: Seats - Remove Seat
    # Class: Passenger - Remove Flight
    # Passenger 2
    # Class: Seats - Add Wait List Passenger
    # Class: Wait List - Remove Flight
    # Class: Passenger - Remove Wait List Flight
    passengerName = input("Enter Name: ").capitalize()
    flightnumber = input("Enter Flight Number: ")
    def FindClassType(flightnumber, passengerName):
        for x in allPassengers:
            if passengerName == x.name:
                for y in x.flights.items():
                    return y[1][0]
    classType = FindClassType(flightnumber, passengerName)
    def RemovePassengerFromSeat(flightnumber, passengerName): # Class: Seats - Removes Passenger From Seats
        for x in allNodes:
            if x.key == flightnumber:
                for y in x.child:
                    if y.key == "Seats":
                        for i in y.child:
                            for u in i.key.items():
                                if u[1] == passengerName:
                                    print("Passenger Is On This Flight, Removing Passenger.")
                                    i.key[u[0]] = None
    def RemovePassengerFlight(flightnumber, passengerName):
        for x in allPassengers:
            if x.name == passengerName:
                del x.flights[flightnumber]
    def FindPassengerName(flightnumber):
        for x in allWaitList:
            if x.flight_num == flightnumber:
                return x.classes[classType].queue[0]
    RemovePassengerFromSeat(flightnumber, passengerName)
    RemovePassengerFlight(flightnumber, passengerName)
    print("Next Passenger is:",FindPassengerName(flightnumber))
    seatNumArr = []
    for x in allPassengers:
        for x in x.waitList.items():
            print(x[1][1])
            seatNumArr.append(x[1][1])
    print(seatNumArr)
    a = input("Do You Want To Schedule This Passenger?: ").capitalize()
    if a == "Yes":
        for x in allNodes: # Class - Seats
            if x.key == flightnumber:
                for y in x.child:
                    if y.key == "Seats":         
                        for i in y.child:
                            for u in i.key.items():
                                if u[1] == None:
                                    i.key[u[0]] = FindPassengerName(flightnumber)
                                    return
    elif a == "No":
        print("No Selected, Returning.")
        return
    Main()

def AddPassenger():
    # Passenger
    # Class: Seats - Add Seats
    # Class: Passenger - Add Flight
    # If No Space:
    # Class: WaitList - Add Flight
    # Class Passenger: Add WaitList Flight
    name = input("Enter Name: ").capitalize()
    flightnumber = input("Enter Flight Number: ")
    seatType = input("Enter Class: ").capitalize()
    classType = seatType
    if PassengerExists(name) == False: # If Passenger Exists: Return.
        b = ("Passenger Already Exists, Do You Want To Schedule Passenger Again?: ").capitalize()
        if b == "Yes":
            pass
        elif b == "No":
            print("No Selected, Returning.")
            return    
    def AddWaitList(name, flightnumber, classType, seatNum): # Class: Wait List - Add Flight
        for x in allWaitList:
            if flightnumber == x.flight_num:
                for y in x.classes.items():
                    if y[0] == seatType:
                        y[1].put(name)
                        queuePosition = linear_search(y[1].queue, name) # Searching Algorithm
        seatarr = []
        for x in allPassengers:
            for x in x.waitList.items():
                print(x[1][1])
                seatarr.append(x[1][1])
        for x in allPassengers: # Class Passenger: Add WaitList Flight
            if x.name == name:
                Passenger.addToWaitingList(x, flightnumber, seatType, queuePosition)
                print("\n--",x.name)
                print("Flights:",x.flights)
                print("Wait Lists:",x.waitList)
    def AddPassengerFlight(name, flightnumber, classType, seatNum): # Class: Passenger - Add Flight
        for x in allPassengers:
            if x.name == name:
                Passenger.addFlights(x, flightnumber, classType, seatNum)
    def AddPassengerSeat(flightnumber, seatType, name, classType): # Class: Seats - Add Seats
        for x in allNodes: # Class - Seats
            if x.key == flightnumber:
                for y in x.child:
                    if y.key == "Seats":
                        first = y.child[0].key
                        business = y.child[1].key
                        economy = y.child[2].key
        if classType == "First":
            counter = 0
            for x in first.items():
                counter += 1
                if x[1] == None:
                    first[x[0]] = name
                    seatNum = x[0]
                    AddPassengerFlight(name, flightnumber, classType, seatNum)
                    break
                if counter == len(first):
                    print("Counter Len Loop")
                    a = input("No Spaces Avaliable, Do You Want To Go On a Wait List?: ").capitalize()
                    if a == "Yes":
                        print("Yes Selected, Adding Passenger To Wait List")
                        seatNum = x[0]
                        print("SeatNumber:", seatNum)
                        AddWaitList(name, flightnumber, classType, counter)
                    elif a != "Yes":
                        print("No Selected, Returning")
                    return
        elif classType == "Business":
            counter = 0
            for x in business.items():
                counter += 1
                if x[1] == None:
                    business[x[0]] = name
                    seatNum = x[0]
                    AddPassengerFlight(name, flightnumber, classType, seatNum)
                    break
                if counter == len(business):
                    print("Counter Len Loop")
                    a = input("No Spaces Avaliable, Do You Want To Go On a Wait List?: ").capitalize()
                    if a == "Yes":
                        print("Yes Selected, Adding Passenger To Wait List")
                        seatNum = x[0]
                        print("SeatNumber:", seatNum)
                        AddWaitList(name, flightnumber, classType, counter)
                    elif a != "Yes":
                        print("No Selected, Returning")
                    return
        elif classType == "Economy":
            counter = 0
            for x in economy.items():
                counter += 1
                if x[1] == None:
                    economy[x[0]] = name
                    seatNum = x[0]
                    AddPassengerFlight(name, flightnumber, classType, seatNum)
                    break
                if counter == len(economy):
                    print("Counter Len Loop")
                    a = input("No Spaces Avaliable, Do You Want To Go On a Wait List?: ").capitalize()
                    if a == "Yes":
                        print("Yes Selected, Adding Passenger To Wait List")
                        seatNum = x[0]
                        print("SeatNumber:", seatNum)
                        AddWaitList(name, flightnumber, classType, counter)
                    elif a != "Yes":
                        print("No Selected, Returning")
                    return
    AddPassengerSeat(flightnumber, seatType, name, classType)
    Main()
    
def PassengerStatus():
    print("\nPassenger Status")
    name = input("Enter Your Name: ").capitalize()
    for x in allPassengers:
        if x.name == name:
            print("Name:",x.name)
            print("Flights:",x.flights)
            print("Wait Lists:",x.waitList)
    Main()

def FlightStatus():
    flightnumber = input("Enter Flight Number: ")
    if flightnumber == "101" or "700":
        print("Valid Flight Number.")
        pass
    else:
        print("Valid Flight Number.")
        Main()
    for x in allPlanes:
        if flightnumber == x.flight_num:
            print("\nFlight Number:",x.flight_num)
            print("Departure Airport:",x.departure_airport)
            print("Arrival Airport:",x.arrival_airport)
    for x in allNodes: # Class - Seats
        if x.key == flightnumber:
            for y in x.child:
                if y.key == "Seats":
                    print("First:",y.child[0].key)
                    print("Business:",y.child[1].key)
                    print("Economy:",y.child[2].key)
    Main()

# FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - FUNCTIONS - 

# SEARCHING ALGORITHMS - SEARCHING ALGORITHMS - SEARCHING ALGORITHMS - SEARCHING ALGORITHMS - SEARCHING ALGORITHMS - 
def linear_search(list, var):
    for x in range(len(list)): # Big O: O(N)
        if list[x] == var:
            return x # Big O: O(1)
    print("Not Found")
    # Big O: N * O(1) = O(N)

# SEARCHING ALGORITHMS - SEARCHING ALGORITHMS - SEARCHING ALGORITHMS - SEARCHING ALGORITHMS - SEARCHING ALGORITHMS - 

# SORTING ALGORITHMS - SORTING ALGORITHMS - SORTING ALGORITHMS - SORTING ALGORITHMS - SORTING ALGORITHMS - SORTING ALGORITHMS - 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# SORTING ALGORITHMS - SORTING ALGORITHMS - SORTING ALGORITHMS - SORTING ALGORITHMS - SORTING ALGORITHMS - SORTING ALGORITHMS - 

def Populate(): # Populate Seats
    # Class: Flight - Add to Flight
    # Class: Passenger - Add to Passsenger
    for x in allNodes: # Class - Seats
        if x.key == "101":
            for y in x.child:
                if y.key == "Seats":
                    y.child[0].key[1] = "Maria"
                    y.child[0].key[2] = "Aiden"
                    y.child[0].key[3] = "Jerry"
                    y.child[0].key[4] = "Tom"
                    print(y.child[0].key)

allPassengers.append(Passenger("Maria"))

allPassengers.append(Passenger("Aiden"))

allPassengers.append(Passenger("Jerrrrrry"))
def ww(name, flightnumber, seatType):
    for x in allWaitList:
        if x.flight_num == flightnumber:
            for y in x.classes.items():
                if y[0] == seatType:
                    y[1].put(name)
                    queuePosition = linear_search(y[1].queue, name) # Searching Algorithm
    for x in allPassengers: # Class Passenger: Add WaitList Flight
        if x.name == name:
            Passenger.addToWaitingList(x, flightnumber, seatType, queuePosition)

ww("Maria", "101", "First")
ww("Aiden", "101", "First")
ww("Jerrrrrry", "101", "First")
# seatNumArr = []
# for x in allPassengers:
#     #print(x.name, x.waitList)
#     for x in x.waitList.items():
#         print(x[1][1])
#         seatNumArr.append(x[1][1])
# print(seatNumArr)
Main()

#FlightStatus()
#PrintTree(flight101, "101")


