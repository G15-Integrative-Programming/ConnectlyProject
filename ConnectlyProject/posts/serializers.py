from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User, Post, Comment

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        error_messages={
            'blank': 'email is required',
            'max_length': 'email must be 50 characters or less',
            'unique': 'email already exists'
    })
    username = serializers.CharField(
        error_messages={
            'blank': 'username is required',
            'max_length': 'username must be 50 characters or less',
    }, validators=[
            UniqueValidator(queryset=User.objects.all(), message='username already exists')
        ])
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True, read_only=True)
    content = serializers.CharField(
        error_messages={
            'blank': 'content is required',
})
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        error_messages={
            'required': 'Author is required.',
            'does_not_exist': 'User with the given ID does not exist.'
})
    class Meta:
        model = Post
        fields = ['id', 'content', 'author', 'created_at', 'comments']

class CommentSerializer(serializers.ModelSerializer):
    # Override author and post fields to be simple integers
    author = serializers.IntegerField()
    post = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'post', 'created_at']

    def validate_author(self, value):
        if not value:
            raise serializers.ValidationError("Author is required and cannot be empty.")
        try:
            user = User.objects.get(id=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("Author with the given ID does not exist or is invalid.")
        return user

    def validate_post(self, value):
        if not value:
            raise serializers.ValidationError("Post is required and cannot be empty.")
        try:
            post = Post.objects.get(id=value)
        except Post.DoesNotExist:
            raise serializers.ValidationError("Post with the given ID does not exist or is invalid.")
        return post