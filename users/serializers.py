from rest_framework import serializers
from .models import User, UserDetail


class UserSerializer(serializers.ModelSerializer):
    # user = UserDetailSerializer()

    class Meta:
        model = User
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = UserDetail
        fields = "__all__"

    def create(self, validated_data):

        user_data = validated_data.pop("user")
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        userDetail, created = UserDetail.objects.update_or_create(
            user=user,
            phoneNo=validated_data.pop("phoneNo"),
            number=validated_data.pop("number"),
        )
        print(created)
        return userDetail
