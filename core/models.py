from django.contrib.auth.decorators import login_required

from django.db import models
from django.contrib.auth.models import User
# from sorl.thumbnail import ImageField


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_address = models.CharField(max_length=200)
    shipping_zip_code = models.CharField(max_length=200, null=True, blank=True)
    shipping_city = models.CharField(max_length=200, null=True, blank=True)
    shipping_country = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)

    date_registered = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.user}"
#
#
# class Product(models.Model):
#     CATEGORY_CHOICES = (
#         ('dining-tables', 'Dining Tables'),
#         ('kitchen-chairs', 'Kitchen Chairs'),
#
#         ('office-chairs', 'Office Chairs'),
#         ('office-desks', 'Office Desks'),
#
#         ('sofas', 'Sofas'),
#         ('coffee-tables', 'Coffee Tables'),
#
#         ('beds', 'Beds'),
#         ('bedside-tables', 'Bedside Tables'),
#         ('wardrobes', 'Wardrobes'),
#     )
#     name = models.CharField(max_length=150)
#     category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
#     attributes = models.TextField()
#     price = models.FloatField()
#     discount_price = models.FloatField(blank=True, null=True)
#     image = ImageField(upload_to='product_images')
#     stock = models.IntegerField()
#     is_visible = models.BooleanField(default=True)
#
#     @property
#     def is_out_of_stock(self):
#         return self.stock <= 0
#
#     def __str__(self):
#         return f'[{self.category}] {self.name} - ${self.price:.2f}'
#
#
# class Order(models.Model):
#     STATUS = (
#         ('Pending', 'Pending'),
#         ('Shipped', 'Shipped'),
#         ('Delivered', 'Delivered'),
#     )
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False, null=True, blank=False)
#     status = models.CharField(max_length=200, null=True, choices=STATUS)
#
#     @property
#     def get_cart_total(self):
#         order_items = self.orderitem_set.all()
#         total = sum([item.get_total for item in order_items if not item.is_out_of_stock])
#         return total
#
#     @property
#     def is_shipped(self):
#         return self.status != "Pending"
#
#     @property
#     def get_items(self):
#         order_items = self.orderitem_set.all()
#         return order_items
#
#     @property
#     def has_out_of_stock_products(self):
#         return any(item.is_out_of_stock for item in self.orderitem_set.all())
#
#     @property
#     def get_total_items(self):
#         order_items = self.orderitem_set.all()
#         total_products = sum([item.quantity for item in order_items if not item.is_out_of_stock])
#         return total_products
#
#     def __str__(self):
#         return f"[{self.date_ordered}] User: {self.user}"
#
#
# class OrderItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     @property
#     def is_out_of_stock(self):
#         return self.product.stock <= 0 or self.quantity > self.product.stock
#
#     @property
#     def get_total(self):
#         if self.product.discount_price:
#             return self.quantity * self.product.discount_price
#         else:
#             return self.quantity * self.product.price
#
#     def __str__(self):
#         if self.product is not None:
#             return f"{str(self.order)} {self.product.name} - {self.quantity}"
#
#
# class ShippingAddress(models.Model):
#     order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
#
#     first_name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=250)
#
#     shipping_address = models.CharField(max_length=200)
#     shipping_zip_code = models.CharField(max_length=200)
#     shipping_city = models.CharField(max_length=200)
#     shipping_country = models.CharField(max_length=200)
#     phone_number = models.CharField(max_length=200)
#
#     def __str__(self):
#         return f"{self.order.date_ordered} [{self.order.user.username}] {self.shipping_country} | {self.shipping_city} | {self.shipping_address}"
#
#
# class Review(models.Model):
#     STAR_RATING_CHOICES = (
#         (1, '1 Star'),
#         (2, '2 Stars'),
#         (3, '3 Stars'),
#         (4, '4 Stars'),
#         (5, '5 Stars'),
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     review = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     star_rating = models.IntegerField(choices=STAR_RATING_CHOICES)
#
#     def __str__(self):
#         return f'{self.product} - {self.star_rating} Stars (by {self.user})'
#
#
# class WishlistItem(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"User {self.user.username}: {self.product.name}"
