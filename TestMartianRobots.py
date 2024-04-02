import unittest
import martianRobots

class TestMartianRobots(unittest.TestCase):

    # test mainProcess, that the whole process gives an expected result
    def test_oneRobotwithFall(self):
        result = martianRobots.mainProcess('5 3 3 2 N FRRFLLFFRRFLL')
        self.assertEqual(result, ['3 3 N LOST']) 
    
    def test_oneRobotStays(self):
        result = martianRobots.mainProcess('5 3 1 1 E RFRFRFRF')
        self.assertEqual(result, ['1 1 E'])

    def test_fewRobotsWithFall(self):
        result = martianRobots.mainProcess('5 3 1 1 E RFRFRFRF 3 2 N FRRFLLFFRRFLL 0 3 W LLFFFLFLFL')
        self.assertEqual(result, ['1 1 E', '3 3 N LOST', '2 3 S']) 

    # isSomeFallBefore
    def test_isSomeFallBefore_True(self):
        result = martianRobots.isSomeFallBefore(3, 3, 'N', {3: '3N'})
        self.assertTrue(result)

    def test_isSomeFallBefore_False(self):
        result = martianRobots.isSomeFallBefore(3, 2, 'N', {3: '3N'})
        self.assertFalse(result)

    # turnRobot
    def test_turnRobotLFromN(self):
        result = martianRobots.turnRobot('N', 'L')
        self.assertEqual(result, 'W') 
    
    def test_turnRobotRFromW(self):
        result = martianRobots.turnRobot('W', 'R')
        print(result)
        self.assertEqual(result, 'N') 

    # movingRobOnField
    def movingRobOnField_Lost(self):
        result = martianRobots.movingRobOnField(1, 1, [], {}, 0, 0, 'S', 'F')
        print(result)
        self.assertEqual(result, ['0 0 S LOST'])

    def movingRobOnField_Stays(self):
        result = martianRobots.movingRobOnField(1, 1, [], {}, 0, 0, 'S', 'LLF')
        print(result)
        self.assertEqual(result, ['0 1 N'])

if __name__ == '__main__':
    unittest.main()