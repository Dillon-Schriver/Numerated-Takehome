import requests
class RouteInfo():
    def __init__(self) -> None:
        
        self.MBTA_API = "https://api-v3.mbta.com/"

        # reference data
        self.stop_ids = {}
        self.routes = set()
        # assumption - this is unchanging
        self.directions = {}
        # Default route - serve our HTML and corresponding JS for frontend
    # Handle our rail information requets - serve light and heavy rail routes
    def get_rail_options(self):
        # GET route - return all Light and Heavy Rail Trains
        call = self.MBTA_API+"routes/"
        response = requests.get(call)
        light_or_heavy = []
        if response:
            result = response.json()
            # process our data and retain only the light and heavy rail lines
            for route in result["data"]:
                if route['attributes']['type'] == 1 or route['attributes']['type'] == 0:
                    light_or_heavy.append(route['id'])
                    self.directions[route['id']] = route['attributes']['direction_names'] 
            return [(light_or_heavy), self.directions]
        else:
            print(response.status_code)
            print('Request error')
            return ['Error', 'Error']

    # Handle stops for a given route selection from user
    def get_specific_stops(self, route):
        # GET route - return all scheduled stops on this route
        # print('incoming route',route)
        call = self.MBTA_API+"schedules?filter[route]="+route
        response = requests.get(call)
        relevant_stops = set({})
        if response:
            result = response.json()
            # print(response.status_code)
            for stop in result["data"]:
                id = stop["relationships"]["stop"]["data"]["id"] 
                #check if we know what stop this corresponds to, if not just query the API
                # if for some reason our list of ids isn't populated, recache them
                if id not in self.stop_ids:
                    #TODO - Filter this
                    id_call =  requests.get(self.MBTA_API+'/stops/')
                    if id_call:
                        for entry in id_call.json()['data']:
                            name = entry['attributes']['name']
                            update_id =  entry['id']
                            try:
                                int(update_id)
                                self.stop_ids[update_id] = name
                                self.stop_ids[name] = update_id
                            except:
                                continue
                
                relevant_stops.add(self.stop_ids[id])

            return list(relevant_stops)
        # Otherwise, catch error
        else:
            print('Request error - Stops')
            # print(response.status_code)
            return ['Error']

    # Return the nearest predicted train given a route, direction, and stop as query parameters
    def get_predicted_arrival(self, route, direction, stop):
        # check for valid stop, this must be included in stop_ids as we recorded in dictionary on previous calls
        if stop in self.stop_ids:
            temp =self.stop_ids[stop]
        else:
            return "Invalid Stop"
        stopid = str(temp)
        # print(type(stopid))
        # print(stopid)
        call = self.MBTA_API + "predictions?sort[arrival_time],filter[stop]=" + stopid + "&filter[direction_id]="+direction +"&filter[route]="+route
        result = requests.get(call).json()
        if result:
            # since our times are already sorted in order of departure, just need to return the first one that is valid
            for arrival in result["data"]:
                # check to make sure it has not timed out or otherwise set to null for the earliest departure, and return the first valid option
                if arrival["attributes"]["departure_time"] is not None:
                    return arrival["attributes"]["departure_time"]

            # if something went wrong and we failed, just return generic response
        else:
            return 'Error'

    