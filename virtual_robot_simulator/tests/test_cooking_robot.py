import unittest
from src.robots.cooking_robot import CookingRobot

class TestCookingRobot(unittest.TestCase):
    """
    Test cases for the CookingRobot class.
    """

    def setUp(self) -> None:
        """
        Set up a test cooking robot instance before each test.
        """
        self.cook_bot = CookingRobot(name="CookBot", cooking_skill="expert")

    def test_work(self) -> None:
        """
        Test the work method.
        """
        self.cook_bot.work()
        self.assertEqual(self.cook_bot.battery_level, 70)
        self.assertEqual(self.cook_bot.status, "working")

    def test_insufficient_battery(self) -> None:
        """
        Test the work method with insufficient battery.
        """
        self.cook_bot.battery_level = 20
        self.cook_bot.work()
        self.assertEqual(self.cook_bot.battery_level, 20)
        self.assertEqual(self.cook_bot.status, "idle")

if __name__ == '__main__':
    unittest.main()
