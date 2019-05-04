from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Country, City, Store, Category, Customer, My_Item, Supplier, Delivery, My_Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'capital', 'currency')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'my_country')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'my_city')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'my_store')

class MyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = My_Item
        fields = ('id', 'name', 'description', 'price', 'count', 'added_date', 'my_category', 'my_supplier')

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'name', 's_name', 'phone_number', 'company_name')

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('id', 'name', 's_name', 'company_name')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 's_name', 'phone_number', 'qiwi_card', 'credit_card', 'address', 'my_city')

class MyOrderSeialzer(serializers.ModelSerializer):
    class Meta:
        model = My_Order
        fields = ('id', 'status', 'ship_date', 'item_count', 'transportation_cost', 'price', 'my_delivery', 'my_store', 'my_customer')