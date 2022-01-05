from django.db import models
from users.models import CustomUser


class Post(models.Model):

    # News Post model
    title = models.CharField(max_length=60)
    link = models.URLField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(
        CustomUser, related_name='voted_posts', blank=True)
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="authored_posts")

    def __str__(self):
        return self.title

    @property
    def amount_of_upvotes(self):
        return self.upvotes.count()

    @property
    def author_name(self):
        return self.author.name


class Comment(models.Model):

    # comments Model on a News Post
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment for Post: {self.post.id}'

    @property
    def author_name(self):
        return self.author.name
