import Data
import unittest

""" Simple unit tests for the challenge """

class Test(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.rt = Data.RouteInfo()        

    # route unit tests
    def test_routes(self):
        options = self.rt.get_rail_options()
        # should return a list
        self.assertEqual(type(options), type([]))
        # list should be nonempty - bad query
        self.assertTrue(len(options) > 0 )
        # first list of directions should be nonempty
        self.assertTrue(len(options[0]) > 0 )
        # second element should be a dictionary
        self.assertEqual(type(options[1]), type({}))
        # successfully connected to API
        self.assertTrue(options[0] != 'Error')
    
    # stop unit tests - get_specific_stops()
    def test_stops(self):
        # Valid returns expected - valid route
        valid = self.rt.get_specific_stops('Red')
        # should return a list
        self.assertEqual(type(valid), type([]))
        # list should be nonempty
        self.assertTrue(len(valid) > 0 )
         # first element should be a str
        self.assertEqual(type(valid[0]), type('S'))
        # successfully connected to API
        self.assertTrue(valid[0] != 'Error')

        # Invalid returns
        invalid = self.rt.get_specific_stops("Banana")
        # return empty list
        self.assertEqual(len(invalid),0)

    # predition unit tests
    def test_predict(self):
        # run intial user steps 
        self.rt.get_rail_options()
        self.rt.get_specific_stops('Red')
        # Valid returns expected - valid route
        valid = self.rt.get_predicted_arrival('Red',"1","Harvard")
        # should return a str
        self.assertEqual(type(valid), type('S'))
        # str should be non trivial
        self.assertTrue(len(valid) > 0 )
        # should have returned valid stop(s) and successfully connected to API
        self.assertTrue(valid != ['Error'])
    
        # Invalid returns
        invalid = self.rt.get_predicted_arrival("Banana","apple","Mars")
        # should detect an invalid stop before making a call
        self.assertEqual(invalid, "Invalid Stop")
        
        invalid2 = self.rt.get_predicted_arrival("Banana","apple","Harvard")
        # should return generic for bad query with valid stop
        self.assertEqual(len(invalid), 12)


if __name__ == "__main__":
    """ Execute from command line """
    unittest.main()