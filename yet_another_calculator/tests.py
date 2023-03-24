from django.test import TestCase, Client


class Tests(TestCase):

    def set_up(self):
        self.client = Client()

    def test_main_page_status_code(self):
        response = self.client.get('/').status_code
        self.assertEqual(response, 200)

    def test_profile_page_status_code(self):
        status_code = self.client.get('/profile').status_code
        self.assertEqual(status_code, 301)

    def test_registration_page_status_code(self):
        status_code = self.client.get('http://127.0.0.1:8000/reg').status_code
        self.assertEqual(status_code, 301)

    def test_calc_page_status_code(self):
        status_code = self.client.get('http://127.0.0.1:8000/elementary_mathematics/').status_code
        self.assertEqual(status_code, 200)

    def test_trigonometry_page_status_code(self):
        status_code = self.client.get('http://127.0.0.1:8000/trigonometry/').status_code
        self.assertEqual(status_code, 200)

    def test_graphic_page_status_code(self):
        status_code = self.client.get('http://127.0.0.1:8000/graphic/').status_code
        self.assertEqual(status_code, 200)

    def test_equation_page_status_code(self):
        status_code = self.client.get('http://127.0.0.1:8000/equation/').status_code
        self.assertEqual(status_code, 200)

    def test_currency_page_status_code(self):
        status_code = self.client.get('http://127.0.0.1:8000/currency/').status_code
        self.assertEqual(status_code, 200)

    def test_radix_page_status_code(self):
        status_code = self.client.get('http://127.0.0.1:8000/radix/').status_code
        self.assertEqual(status_code, 200)

    def test_stereometry_page_status_code(self):
        status_code = self.client.get('http://127.0.0.1:8000/stereometry/').status_code
        self.assertEqual(status_code, 200)

    def test_antiderivative_page_status_code(self):
        status_code = self.client.get('http://127.0.0.1:8000/antiderivative/').status_code
        self.assertEqual(status_code, 200)

    def test_integral_page_status_code(self):
        status_code = self.client.get('http://127.0.0.1:8000/integral/').status_code
        self.assertEqual(status_code, 200)

    def test_factorial_page_status_code(self):
        status_code = self.client.get('http://127.0.0.1:8000/factorial/').status_code
        self.assertEqual(status_code, 200)
