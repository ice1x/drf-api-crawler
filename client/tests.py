import datetime

from django.test import TestCase
from django.utils import timezone

from client.models import Posts


class PostsModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        post = Posts(created=time)
        self.assertIs(post.id, None)
