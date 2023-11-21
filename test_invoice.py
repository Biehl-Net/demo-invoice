import unittest
from unittest.mock import patch
from io import StringIO
from invoice import Service

class TestService(unittest.TestCase):
    def setUp(self):
        Service.services = []

    def test_service_menu(self):
        with patch('builtins.input', return_value='2'):
            service = Service.service_menu()
            self.assertEqual(service, 2)

    def test_get_service_name(self):
        service_name = Service.get_service_name(1)
        self.assertEqual(service_name, "Bathing")

        service_name = Service.get_service_name(2)
        self.assertEqual(service_name, "Haircut")

        service_name = Service.get_service_name(3)
        self.assertEqual(service_name, "Nail trim")

    def test_collect_services(self):
        with patch('builtins.input', side_effect=['1', '10', '3', '15', '4']):
            Service.collect_services()
            expected_services = [
                {"name": "Bathing", "price": 10.0},
                {"name": "Nail trim", "price": 15.0}
            ]
            self.assertEqual(Service.services, expected_services)

    def test_display_services(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            Service.services = [
                {"name": "Bathing", "price": 10.0},
                {"name": "Haircut", "price": 20.0},
                {"name": "Nail trim", "price": 15.0}
            ]
            Service.display_services()
            expected_output = "Services:\n-  Bathing ($ 10.00 )\n-  Haircut ($ 20.00 )\n-  Nail trim ($ 15.00 )\n"
            self.assertEqual(fake_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()