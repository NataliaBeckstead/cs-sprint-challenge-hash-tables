#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = []
    flights_hash = {}
    for i in range(length):
        flights_hash[tickets[i].source] = tickets[i].destination
    
    key = "NONE"
    for item in flights_hash.items():
        route.append(flights_hash[key])
        key = flights_hash[key]
        
    return route
