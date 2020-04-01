from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    point = models.PositiveSmallIntegerField(default=0)

    # phone_number = PhoneNumberField()
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    price_range = models.CharField(max_length=100)
    parking = models.PositiveSmallIntegerField(default=0)
    opening_ours = models.CharField(max_length=100)
    menu = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # 나중에 지역 카테고리도 만들게 되면 주소에서 데이터 짤라서 카테고리별로 나누

    def __str__(self):
        return self.name


class RestaurantImages(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to="restaurant/images", blank=True)  # 처음 이미지를 업로드하면 media 폴더가 자동으로 생성된다.

# class RestaurantLocation(models.Model):
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
#     location = models.ImageField(upload_to="category/images", blank=True)  # 처음 이미지를 업로드하면 media 폴더가 자동으로 생성된다.
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)


# class RestaurantReview(models.Model):
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     title = models.CharField(max_length=50)
#     review = models.TextField()
#     photo = models.ImageField(upload_to="review/images", blank=True)  # 처음 이미지를 업로드하면 media 폴더가 자동으로 생성된다.
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
