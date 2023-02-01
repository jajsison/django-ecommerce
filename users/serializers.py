from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import authenticate, login

# from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = CustomUser
    #     fields = ('email', 'first_name', 'last_name', 'password')
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    email = serializers.EmailField(max_length=255)
    # first_name = serializers.CharField(max_length=30)
    # last_name = serializers.CharField(max_length=30)
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def validate_login(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                "Incorrect email/password combination")
        return user


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = CustomUser(
            email=self.validated_data['email'],

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

        email = serializers.EmailField(max_length=255)
        password = serializers.CharField(
            write_only=True,
            required=True,
            style={'input_type': 'password'}
        )

        def validate_login(self, data):
            email, password = data.values()

            if not email or not password:
                message = _('Email and password are required.')
                raise serializers.ValidationError(
                    message, code='authorization')

            self.user = authenticate(
                request=self.request, email=email, password=password)

            login(self.request, self.user)

            return data

# class LoginSerializers(serializers.Serializer):

#     email = serializers.EmailField(max_length=255)
#     password = serializers.CharField(
#         label=("Password"),
#         style={'input_type': 'password'},
#         trim_whitespace=False,
#         write_only=True
#     )

#     def validate(self, data):
#         import pdb
#         pdb.set_trace()
#         email = data.get('email')
#         password = data.get('password')

#         if email and password:
#             user = authenticate(request=self.context.get('request'),
#                                 username=email, password=password)
#             if not user:
#                 msg = ('Unable to log in with provided credentials.')
#                 raise serializers.ValidationError(
#                     msg, code='authorization')
#             else:
#                 msg = ('Must include "email" and "password".')
#                 raise serializers.ValidationError(msg, code='authorization')

#             data['user'] = user
#             return data

# class LoginSerializer(serializers.Serializer):
#     """
#     This serializer defines two fields for authentication:
#       * username
#       * password.
#     It will try to authenticate the user with when validated.
#     """
#     username = serializers.CharField(
#         label="Username",
#         write_only=True
#     )
#     password = serializers.CharField(
#         label="Password",
#         # This will be used when the DRF browsable API is enabled
#         style={'input_type': 'password'},
#         trim_whitespace=False,
#         write_only=True
#     )

#     def validate(self, attrs):
#         # Take username and password from request
#         username = attrs.get('username')
#         password = attrs.get('password')

#         if username and password:
#             # Try to authenticate the user using Django auth framework.
#             user = authenticate(request=self.context.get('request'),
#                                 username=username, password=password)
#             if not user:
#                 # If we don't have a regular user, raise a ValidationError
#                 msg = 'Access denied: wrong username or password.'
#                 raise serializers.ValidationError(msg, code='authorization')
#         else:
#             msg = 'Both "username" and "password" are required.'
#             raise serializers.ValidationError(msg, code='authorization')
#         # We have a valid user, put it in the serializer's validated_data.
#         # It will be used in the view.
#         attrs['user'] = user
#         return attrs
