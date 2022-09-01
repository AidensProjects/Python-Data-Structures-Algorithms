import re
class Plane:
    allPlanes = [] # Useful for algorithms, as the plane information is in a list.
    planesCreated = 0

    def __init__(self, flight_num, departure_airport, departure_date, arrival_airport, seats):
        self.flight_num = flight_num
        self.departure_airport = departure_airport
        self.departure_date = departure_date
        self.arrival_airport = arrival_airport
        self.seats  = seats
        Plane.allPlanes.extend([self.flight_num, self.departure_airport, self.departure_date, self.arrival_airport, self.seats])
        Plane.planesCreated += 1

    def print_plane(self):
        print("Flight Number:",self.flight_num)
        print("Departure Airport:",self.departure_airport)
        print("Arrival Airport:",self.arrival_airport)  

class Passenger:
    # Constants
    allPassengers = []
    number_of_passengers = 0

    def __init__(self, name):
        self.name = name
        self.flights = dict()
        self.waitList = dict()
        Passenger.number_of_passengers += 1
        Passenger.allPassengers.append(self.name)
    
    def addFlights(self, flight_number, seat_type, seat_num): # , seat_type, seat_num
        self.flights[flight_number] = (seat_type, seat_num)
    
    def addToWaitingList(self, flight_number, seat_type, wait_list_position):
        self.waitList[flight_number] = (seat_type, wait_list_position)
    
    def removeFlights(self, flight_number):
        del self.flights[flight_number]

    def removeWaitList(self, flight_number):
        del self.waitList[flight_number]

    def print_passenger(self):
        return self.name, self.flights, self.waitList
    
    def print_passenger2(self):
        print("Name:",self.name)
        print("Flights:",self.flights)
        print("Wait Lists:",self.waitList)
    
    def printWaitList(self):
        print("===-==-=-==-===-==-=-==-===-===-==-=-==-===-==-=-==-===")
        print("Wait List:")
        for x in self.waitList.items():
            print("===-==-=-==-===-==-=-==-===-===-==-=-==-===-==-=-==-===")
            print("Flight Number:",x[0])
        
    def printFlights(self):
        print("===-==-=-==-===-==-=-==-===-===-==-=-==-===-==-=-==-===")
        print("Flights:")
        for x in self.flights.items():
            print("===-==-=-==-===-==-=-==-===-===-==-=-==-===-==-=-==-===")
            print("Flight Number:",x[0])
            print("Seat Type:",x[1][0])
            print("Seat Number:",x[1][1])
            print("===-==-=-==-===-==-=-==-===-===-==-=-==-===-==-=-==-===")
        
    def findPassengersPosition(self):
        print(self.waitList)

class Seats:
    passengers_in_seats = []
    all_seats = []

    def __init__(self, flight_num, first, business, economy):
        self.flight_num = flight_num
        self.first = dict.fromkeys(first) #Key = int of seat number // Value = Passanger Object
        self.business = dict.fromkeys(business) 
        self.economy = dict.fromkeys(economy)
        self.classes = {"First" : self.first, "Business" : self.business, "Economy" : self.economy}
        Seats.all_seats.append(self.flight_num)
        Seats.all_seats = list(dict.fromkeys(Seats.all_seats)) # Removes duplicates from declaring Seats0/Seats1 & allSeats.append()

    def get_seat_num(self, flight_num, seattype, name):
        for x in self.classes:
            if flight_num == all_seats.classes[seattype]:
                pass
    
    def print_seats(self):
        return self.flight_num, self.classes
    
    def print_all_passengers(dict, list):
        for x in dict:
            a = x.values()
            for y in a:
                if y == None:
                    pass
                elif y != None:
                    list.append(y)
        return list
    
    def seats_occupied(dict, list):
        for x in dict:
            a = x.values()
            for y in a:
                if y == None:
                    pass
                elif y != None:
                    list.append(y)
        return len(list)

    def add_passenger_to_seat(name, dict):
        a = len(dict.values())
        b = 0
        for x in dict.values():
            if x == None:
                b += 1
        if b == 0:
            return
        for key, value in dict.items():
            if value == None:
                aa = key
                dict[aa] = name
                return
    
    def remove_passenger(dict, name):
        a = 0
        for x in dict:
            a += 1
            if dict[x] == name:
                break
            else:
                print("Passenger not found")
                break
        dict[a] = None

class WaitList:
    def __init__(self, flight_num, first, business, economy):
        self.flight_num = flight_num
        self.first = first
        self.business = business
        self.economy = economy
        self.classes = {"First" : self.first, "Business" : self.business, "Economy" : self.economy}

        