from run import app
from unittest import TestCase, main


class FlaskTestCase(TestCase):

    # Ensure flask login route was set up correctly
    def test_login_route(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure flask login route was set up correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Log In' in response.data)

    # Ensure login behaves correctly given the correct credentials
    def test_correct_login_credentials(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(email='admin@gmail.com', password='copycat123'),
            follow_redirects=True
        )
        self.assertIn(b'Our Sidebar', response.data)


if __name__ == '__main__':
    main()

