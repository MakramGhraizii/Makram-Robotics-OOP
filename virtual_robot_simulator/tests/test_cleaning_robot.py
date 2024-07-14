import unittest
from src.robots.cleaning_robot import CleaningRobot

class TestCleaningRobot(unittest.TestCase):
    """
    Test cases for the CleaningRobot class.
    """

    def setUp(self) -> None:
        """
        Set up a test cleaning robot instance before each test.
        """
        self.clean_bot = CleaningRobot(name="CleanBot", cleaning_tool="vacuum")

    def test_work(self) -> None:
        """
        Test the work method.
        """
        self.clean_bot.work()
        self.assertEqual(self.clean_bot.battery_level, 80)
        self.assertEqual(self.clean_bot.status, "working")

    def test_insufficient_battery(self) -> None:
        """
        Test the work method with insufficient battery.
        """
        self.clean_bot.battery_level = 10
        self.clean_bot.work()
        self.assertEqual(self.clean_bot.battery_level, 10)
        self.assertEqual(self.clean_bot.status, "idle")

if __name__ == '__main__':
    unittest.main()
