"""

Sample tests

"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module """

    def test_add_numbers(self):
        """ test adding numbers """
        res = calc.add(6, 6)

        self.assertEqual(res, 12)

    def test_substract_numbers(self):
        """ test adding numbers """
        res = calc.subtract(6, 6)

        self.assertEqual(res, 0)
