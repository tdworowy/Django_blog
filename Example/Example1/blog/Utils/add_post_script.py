import os

from django.contrib.auth.models import User

from Example.Example1.blog.models import Post
from Example.Utils.random_string import generate_random_string


def add_post(*args):
    user = User.objects.get(username='admin')
    post = Post(title=args[0],
                slug=args[1],
                body=args[2:],
                status='published',
                author=user)
    post.save()


def generate_posts():
    path_ = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    for i in range(10):
        title = generate_random_string(10)
        slug = generate_random_string(10)
        with open(path_ + '\\lore.txt', 'r') as f:
            content = f.read()
        add_post(title, slug, content)


generate_posts()

# need to be run from django shell
