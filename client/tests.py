from django.test import TestCase


class PostsViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # TODO: truncate db table
        pass

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('http://localhost:8000/posts')
        self.assertEqual(resp.status_code, 200)

    def test_view_base_url_is_404(self):
        resp = self.client.get('http://localhost:8000')
        self.assertEqual(resp.status_code, 404)

    def _test_(self):
        # TODO add data inserting to db to read it via views
        # resp = self.client.get('http://localhost:8000/posts')
        # self.assertEqual(resp.status_code, 200)
        pass

    def tearDown(self) -> None:
        # TODO: truncate db table
        pass