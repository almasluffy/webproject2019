from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=200)
    capital = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

class City(models.Model):
    name = models.CharField(max_length=200)
    my_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

class Store(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    my_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


class Manager(models.Model):
    name = models.CharField(max_length=200)
    s_name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

class My_Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    count = models.IntegerField()
    added_date = models.DateField()
    rating = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    my_category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


class Delivery(models.Model):
    name = models.CharField(max_length=200)
    s_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

class Customer(models.Model):
    name = models.CharField(max_length=200)
    s_name = models.TextField()
    phone_number = models.CharField(max_length=20)
    credit_card = models.CharField(max_length=20)
    qiwi_card = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    my_city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

class My_Order(models.Model):
    status = models.CharField(max_length=10)
    ship_date = models.DateField()
    item_count = models.IntegerField()
    transportation_cost = models.IntegerField()
    price = models.IntegerField()

    my_delivery = models.ForeignKey(Delivery,on_delete=models.CASCADE)
    my_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    my_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


class ItemReview(models.Model):
    review_text = models.TextField()

    rev_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rev_item = models.ForeignKey(My_Item, on_delete=models.CASCADE)
