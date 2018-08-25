from django.test import TestCase

from ..db_models.place import Place as DBPlace
from .place import Place, Location


class Test(TestCase):
    def setUp(self):
        self.data = {
            'location': {
                'lat': 10,
                'lng': 10,
            },
            'display_name': 'Dirty Bones',
            'display_address': 'Top Floor, Kingly Court',
        }

    def test_create_place_from_dict(self):
        expected = Place(
            location=Location(lat=10, lng=10),
            display_name='Dirty Bones',
            display_address='Top Floor, Kingly Court',
            description=None,
        )

        self.assertEqual(Place.from_dict(self.data), expected)

    def test_create_place_from_dict_throws_key_error(self):
        data = { 'display_name': 'foo' }
        with self.assertRaises(KeyError):
            _ = Place.from_dict(data)

    def test_create_place_safe_from_dict_returns_none(self):
        data = { 'display_name': 'foo' }
        self.assertEqual(Place.safe_from_dict(data), None)

    def test_to_db_model(self):
        expected = DBPlace(
            lat=self.data['location']['lat'],
            lng=self.data['location']['lng'],
            display_name=self.data['display_name'],
            display_address=self.data['display_address'],
            description=None,
        )

        place = Place.from_dict(self.data)
        db_place = place.to_db_model()
        self.assertEqual(db_place, expected)
