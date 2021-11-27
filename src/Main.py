import sys
import Data
""" 
Main method - run Main.py to interact with the finished challenge and recieve data for each of the 4 requirements

This is a very simple text-based user prompt to get and supply the required information
    Key additions we could discuss: 
        user input handling (e.g. testing for malformed input) and general error handling
        Front-end additions or prettier formatting
        More robust testing
    """


def main():
    running = True
    rt = Data.RouteInfo()
    """ Main entry point of the MBTA challenge """
    print("++++------ Welcome to the MBTA Service ------++++")
    print("++++------ ~~~~~~~~~~~~~~~~~~~~~~~~~~~ ------++++")
    print()
    while running:
        
        # TODO - implement error handling!
        # TODO - add direction prompt!

        print("Please Type EXIT to quit at any time")
        routes, directions = rt.get_rail_options()
        route_prompt ="\nPlease Enter a Route, your choices are:{r}".format(r=routes) 
        route = input(route_prompt)
        if route.lower() == "exit": break
        print("\nrecieved",route)
        
        dir_prompt ="\nPlease Enter a direction, your choices are:{d}".format(d=directions[route]) 
        dir = input(dir_prompt)
        if route.lower() == "exit": break
        print("\nrecieved",dir)
        # convert to numeric
        dir = directions[route].index(dir) 

        stop_prompt ="\nYou selected{r}, what stop would you like to select?:{stops}" \
            .format(r=route, stops=rt.get_specific_stops(route))
        stop = input(stop_prompt)
        if stop.lower() == "exit": break
        print("\nrecieved",stop)

        print("\nOk, for route {r}, at stop {s} , the next train is departing at: {t}" \
            .format(r=route, s=stop, t=rt.get_predicted_arrival(route,str(dir),stop)))
        print("You'd better hurry!")
        print()
        final = input("Press any button to continue or EXIT to quit")
        if stop.lower() == "exit": return
        # break



if __name__ == "__main__":
    """ Execute from command line """
    main()