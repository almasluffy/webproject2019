from django.db import models


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

    my_city = models.ForeignKey(City, on_delete=models.CASCADE)
    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    my_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    s_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=200)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

class My_Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    count = models.IntegerField()
    added_date = models.DateField()
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    my_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    my_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)


    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


class Delivery(models.Model):
    name = models.CharField(max_length=200)
    s_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

class Customer(models.Model):
    name = models.CharField(max_length=200)
    s_name = models.TextField()
    phone_number = models.CharField(max_length=20)
    credit_card = models.CharField(max_length=20)
    qiwi_card = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    my_city = models.ForeignKey(City, on_delete=models.CASCADE)
    # my_store = models.ForeignKey(Store, on_delete=models.CASCADE)

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


