from rest_framework import serializers # import the serializers module from the rest_framework package
from rest_framework.validators import UniqueValidator # used to validate unique fields
from .models import User, Post, Comment # import the User, Post, and Comment models

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
            UniqueValidator(queryset=User.objects.all(), message='username already exists') #uses the UniqueValidator class to validate that the username is unique
        ])
    def validate_username(self, value): # Check if username is alphanumeric (only letters and numbers)
        if not value.isalnum(): # uses the isalnum() method to check if the username contains only alphanumeric characters
            raise serializers.ValidationError("Username must contain only alphanumeric characters.") # raises a validation error if the username contains non-alphanumeric characters
        return value

    class Meta: # Meta class to define the model and fields to serialize
        model = User
        fields = ['id', 'username', 'email', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True, read_only=True) # Define the comments field as a StringRelatedField
    content = serializers.CharField( # Define the content field as a CharField
        error_messages={
            'blank': 'content is required and cannot be empty.',
})
    author = serializers.PrimaryKeyRelatedField( # Define the author field as a PrimaryKeyRelatedField
        queryset=User.objects.all(), # Query the User model for all objects
        error_messages={
            'required': 'Author is required.',
            'does_not_exist': 'User with the given ID does not exist.'
})
    class Meta: # Meta class to define the model and fields to serialize
        model = Post
        fields = ['id', 'content', 'author', 'created_at', 'comments']

class CommentSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField to ensure the fields remain as relation objects
    text = serializers.CharField(
        error_messages={
            'blank': 'Text is required and cannot be empty.'
        }
    )
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        error_messages={
            'required': "Author is required and cannot be empty.",
            'does_not_exist': "Author with the given ID does not exist."
        }
    )
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        error_messages={
            'required': "Post is required and cannot be empty.",
            'does_not_exist': "Post with the given ID does not exist."
        }
    )

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'post', 'created_at']