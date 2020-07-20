import subprocess
import psycopg2

from django.test import TestCase


# TODO: import from base settings
HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'postgres'
DBNAME = 'postgres'
BASE_API_URL = 'http://localhost:8000/posts'


class PostsViewsTests(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get(BASE_API_URL)
        self.assertEqual(resp.status_code, 200)

    def test_view_base_url_is_404(self):
        resp = self.client.get('http://localhost:8000')
        self.assertEqual(resp.status_code, 404)

    def test_view_positive_order_url(self):
        resp = self.client.get(f'{BASE_API_URL}?order=url')
        self.assertEqual(resp.status_code, 200)

    def test_view_positive_order_title(self):
        resp = self.client.get(f'{BASE_API_URL}?order=title')
        self.assertEqual(resp.status_code, 200)

    def test_view_positive_order_created(self):
        resp = self.client.get(f'{BASE_API_URL}?order=created')
        self.assertEqual(resp.status_code, 200)


# class CrawlerGetsOneDayPosts(TestCase):
#     con = psycopg2.connect(
#         host=HOST,
#         user=USER,
#         password=PASSWORD,
#         dbname=DBNAME
#     )
#     cur = con.cursor()
#
#     @classmethod
#     def setUpTestData(cls):
#         cls.cur.execute("TRUNCATE client_posts")
#         cls.con.commit()
#
#     def test_count_one_page_posts_amount(self):
#         self.cur.execute("SELECT count(1) FROM client_posts")
#         result_begin = self.cur.fetchone()
#
#         subprocess.call(['scrapy', 'crawl', 'forward'])
#
#         self.cur.execute("SELECT count(1) FROM client_posts")
#         result_end = self.cur.fetchone()
#
#         self.assertEqual((0, 30), (result_begin[0], result_end[0]))
#
#     def tearDown(self):
#         self.cur.execute("TRUNCATE client_posts")
#         self.con.commit()
