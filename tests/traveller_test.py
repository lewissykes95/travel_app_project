import unittest
from repositories.traveller_repository import Traveller
from repositories.destination_repository import Destination
from models.traveller import Traveller
from models.destination import Destination
import repositories.traveller_repository as traveller_repository
import repositories.destination_repository as destination_repository


class TestTraveller(unittest.TestCase):
    def setUp(self):
        self.traveller1 = Traveller("Lewis", 27)
        self.destination1 = Destination("Lewis", "Sydney", "Australia", 30, False)

    def test_traveller_has_name(self):
        self.assertEqual("Lewis", self.traveller1.name)

    def test_traveller_has_city(self):
        self.assertEqual("Sydney", self.destination1.city)

    def test_traveller_has_been(self):
        self.destination1.checked_off_country()
        self.assertEqual(True, self.destination1.checked_off)

    def test_can_add_traveller(self):
        traveller_repository.save(self.traveller1)
        traveller = traveller_repository.select(self.traveller1.id)
        self.assertEqual("Lewis", traveller.name)











