from django.contrib.auth.models import User

from Example.Example1.blog.models import Post
from Example.Utils.randomString import randomString


def addPost(*args):

    user = User.objects.get(username='admin')
    post = Post(title=args[0],
                slug=args[1],
                body=args[2:],
                status ='published',
                author=user)
    post.save()

def generatePosts():
    path_ = "D:\Google_drive\Python_\Django_test\Example\example1\\blog\\Utils"
    for i in range(10):
        title = randomString(10)
        slug = randomString(10)
        with open(path_ + '\\lore.txt', 'r') as f:
            content = f.read()
        addPost(title,slug,content)

generatePosts()

#need to be run from django shell