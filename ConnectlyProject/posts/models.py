from django.db import models

# Create your models here.

class User(models.Model): # User model
    username = models.CharField(max_length=50, unique=True, blank=False )  # User's unique username which includes validation for uniqueness and blankness
    email = models.EmailField(max_length=50, unique=True, blank=False)  # User's unique email, which includes validation for uniqueness and blankness
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the user was created

    def __str__(self):
        return self.username

class Post(models.Model):
    content = models.TextField(blank=False)  # The text content of the post
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', blank=False)  # The user who created the post
    liked_by = models.ManyToManyField(User, related_name='liked_posts', blank=True)  # Users who liked the post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the post was created

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"

class Comment(models.Model):
    text = models.TextField(blank=False)  # The text content of the comment
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, blank=False) 
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, blank=False) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return f"Comment by {self.author.username} on Post {self.post.id}"  