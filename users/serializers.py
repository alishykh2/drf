from rest_framework import serializers
from .models import User, UserDetail, Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, obj):
        self.fields["category"] = CategorySerializer(many=True, read_only=True)
        return super().to_representation(obj)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ["phoneNo", "number"]


class UserSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True, read_only=True)
    userDetail = UserDetailSerializer(required=True)

    class Meta:
        model = User
        fields = ["id", "firstName", "lastName", "age", "userDetail", "product_set"]

    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data.pop("userDetail")
        user = User(
            firstName=validated_data["firstName"],
            lastName=validated_data["lastName"],
            age=validated_data["age"],
        )
        user.save()
        user_data["user"] = user
        UserDetailSerializer.create(UserDetailSerializer(), validated_data=user_data)

        return user
