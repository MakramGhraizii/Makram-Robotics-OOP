import unittest
from src.robots.base_robot import Robot

class TestRobot(unittest.TestCase):
    """
    Test cases for the Robot class.
    """

    def setUp(self) -> None:
        """
        Set up a test robot instance before each test.
        """
        self.robot = Robot("TestBot")

    def test_initial_status(self) -> None:
        """
        Test the initial status of the robot.
        """
        self.assertEqual(self.robot.name, "TestBot")
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, "idle")

    def test_charge(self) -> None:
        """
        Test the charge method.
        """
        self.robot.battery_level = 50
        self.robot.charge()
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, "charging")

if __name__ == '__main__':
    unittest.main()
