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
        print(1)
        time = timezone.now() + datetime.timedelta(days=30)
        print(2)
        post = Posts(created=time)
        print(dir(post))
        self.assertIs(post.id, None)
