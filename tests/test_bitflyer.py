import unittest

from bitflyer.bitflyer import API


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.api = API()

    def test_markets(self):
        response = self.api.markets()
        self.assertEqual(response["status_code"], 200)

    def test_borad(self):
        response = self.api.board()
        self.assertEqual(response["status_code"], 200)

    def test_ticker(self):
        response = self.api.ticker()
        self.assertEqual(response["status_code"], 200)

    def test_executions(self):
        response = self.api.executions()
        self.assertEqual(response["status_code"], 200)

    def test_boardstate(self):
        response = self.api.boardstate()
        self.assertEqual(response["status_code"], 200)

    def test_health(self):
        response = self.api.health()
        self.assertEqual(response["status_code"], 200)

    def test_chats(self):
        response = self.api.chats()
        self.assertEqual(response["status_code"], 200)


if __name__ == "__main__":
    unittest.main()
