#flight search engine
#flight - starting city + time
#city - strings and time

#1. Good choice of state - Current City and Current Time

from search import Problem, breadth_first_search

class FlightState:
    def __init__(self, city, time):
        self.current_city = city
        self.current_time = time
    
    def __repr__(self):
        return f'{self.current_city},{self.current_time}'

class Flight:
    def __init__(self, start_city, start_time, end_city, end_time):
        self.start_city = start_city
        self.start_time = start_time
        self.end_city = end_city
        self.end_time = end_time

    def __str__(self):
        return str((self.start_city, self.start_time))+ "->"+ str((self.end_city, self.end_time))

    def matches(self, city, time):
        #returns boolean whether city and time match those of the flights, flight leaves city past the time argument
        return (self.start_city == city and self.start_time >= time)



flightDB = [Flight("Rome", 1, "Paris", 4),
            Flight("Rome", 3, "Madrid", 5),
            Flight("Rome", 5, "Istanbul", 10),
            Flight("Paris", 2, "London", 4),
            Flight("Paris", 5, "Oslo", 7),
            Flight("Paris", 5, "Istanbul", 9),
            Flight("Madrid", 7, "Rabat", 10),
            Flight("Madrid", 8, "London", 10),
            Flight("Istanbul", 10, "Constantinople", 10)]

class FlightProblem(Problem): #inheriting from Problem SuperClass
    def __init__(self, start, end):
        super().__init__(start, end) #start contains city and time, end contains city and time
        #calls the super class initialisation, sets initial state and goal state
    
    #implementing abstract methods
    def actions(self, state): #current flight state
        possible_actions = []
        for flight in flightDB:
            if flight.matches(state.current_city, state.current_time):
                possible_actions.append(flight)
        return possible_actions #returns a list of possible actions
    
    def result(self, state, action):
        return (FlightState(action.end_city, action.end_time)) #returns a new FlightState from carrying out the action

    def goal_test(self, state):
        return state.current_city == self.goal.current_city and state.current_time <= self.goal.current_time


def find_itinerary(start_city, start_time, end_city, deadline):
    start_flight_state = FlightState(start_city, start_time)
    end_flight_state = FlightState(end_city, deadline)
    flightProblem = FlightProblem(start_flight_state, end_flight_state)
    solution = breadth_first_search(flightProblem)
    return solution

def find_shortest_itinerary(start_city, start_time, end_city, end_time):
    #Part 4
    #When the shortest path is length 200, it will take roughly 2x number of calls to find_itinerary to solve
    #Assuming that a s
    return

def main():
    #Part 3
    deadline = 1
    solution = None
    while solution is None:
        solution = find_itinerary('Rome', 1, 'Istanbul', deadline)
        deadline += 1

    for sol in solution.solution():
        print (str(sol))

    #Part 4
if __name__ == "__main__":
    main()