from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

#############################################################model base seri...


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
#login
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")
##user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
        depth=1
class PostchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
        # depth=1

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
        depth=1

class ReplytSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reply
        fields='__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=ImageGet
#         fields='__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'
        #depth=1
class ProfileTeoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'
        depth=1