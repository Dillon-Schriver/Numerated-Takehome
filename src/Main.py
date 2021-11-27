import Data
import sys
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
        route_prompt ="\nPlease Enter a Route, your choices are:{routes}".format(routes=rt.get_rail_options()) 
        route = input(route_prompt)
        if route.lower() == "exit": break
        print("\nrecieved",route)

        stop_prompt ="\nYou selected{r}, what stop would you like to select?:{stops}" \
            .format(r=route, stops=rt.get_specific_stops(route))
        stop = input(stop_prompt)
        if stop.lower() == "exit": break
        print("\nrecieved",stop)

        print("\nOk, for route {r}, at stop {s} , the next train is departing at: {t}" \
            .format(r=route, s=stop, t=rt.get_predicted_arrival(route,"1",stop)))
        print("You'd better hurry!")
        print()
        final = input("Press any button to continue or EXIT to quit")
        if stop.lower() == "exit": break
        # break



if __name__ == "__main__":
    """ Execute from command line """
    main()