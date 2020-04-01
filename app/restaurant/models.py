from django.db import models
from phone_field import PhoneField


# from phonenumber_field.formfields import PhoneNumberField


class Restaurant(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='식당이름')
    address1 = models.CharField(default='없음', max_length=100, blank=True, verbose_name='식당주소')

    address2 = models.CharField(default='없음', max_length=100, blank=True, verbose_name='식당지번주소')
    point = models.PositiveSmallIntegerField(default=0, blank=True, verbose_name='식당평점')
    phone = PhoneField(default='없음', unique=True, blank=True, help_text='Contact phone number')
    price_range = models.CharField(default='없음', max_length=100, blank=True, verbose_name='식당가격대')
    parking_text = models.CharField(default='주차여부 알수 없음', max_length=100, blank=True, verbose_name='주차여부')
    opening_hours = models.CharField(default='없음', max_length=100, blank=True, verbose_name='오픈시간')
    menu = models.CharField(default='없음', max_length=300, blank=True, verbose_name='식당메뉴')

    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    date_update = models.DateTimeField(auto_now=True, verbose_name='수정날짜')

    def restaurant_save(self, name, address1, *args, **kwargs):
        if not name:
            raise ValueError('식당 이름은 필수입니다.')
        if not address1:
            raise ValueError('식당 주소는 필수입니다.')

        super().save(name, address1, *args, **kwargs)

    # custom manager 구성 다음에 해보기
    # def _create_restaurant(self, name, address1, **kwargs):
    #     if not name:
    #         raise ValueError('식당 이름은 필수입니다.')
    #     if not address1:
    #         raise ValueError('식당 주소는 필수입니다.')
    #
    #     restaurant = self.model(
    #         name=name,
    #         address1=address1,
    #         **kwargs
    #     )
    #     restaurant.save(using=self._db)
    #     return restaurant
    #
    # def create_restaurant(self, name, address1, **kwargs):
    #     """
    #     일반 유저 생성
    #     """
    #
    #     # kwargs.setdefault('kwargs', kwargs)
    #     return self._create_restaurant(name, address1, **kwargs)
    #
    # def _create_restaurant(self, name, address1, force_insert=False, force_update=False, using=None,
    #                        update_fields=None, *args, **kwargs):
    #
    #
    #     super().save(*args, **kwargs)
    #     kwargs.setdefault('is_admin', True)
    #     return self._create_user(name, address1, **kwargs)

    def __str__(self):
        return self.name


class RestaurantImages(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, verbose_name='이미지_식당')
    photo = models.ImageField(upload_to="restaurant/images", blank=True)  # 처음 이미지를 업로드하면 media 폴더가 자동으로 생성된다.
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    date_update = models.DateTimeField(auto_now=True, verbose_name='수정날짜')


# 나중에 지역 카테고리도 만들게 되면 주소에서 데이터 짤라서 카테고리별로 나누기
class RestaurantCategory(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, verbose_name='카테고리_식당')
    category = models.CharField(max_length=10, verbose_name='카테고리_유형')
    thumbnail = models.ImageField(upload_to="category/images", blank=True,
                                  verbose_name='카테고리_식당_섬네일')  # 처음 이미지를 업로드하면 media 폴더가 자동으로 생성된다.
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    date_update = models.DateTimeField(auto_now=True, verbose_name='수정날짜')


class RestaurantLocation(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, verbose_name='지역_식당')
    location = models.CharField(max_length=30, blank=True,
                                verbose_name='카테고리_식당_섬네일')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    date_update = models.DateTimeField(auto_now=True, verbose_name='수정날짜')

# class RestaurantReview(models.Model):
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     title = models.CharField(max_length=50)
#     review = models.TextField()
#     photo = models.ImageField(upload_to="review/images", blank=True)  # 처음 이미지를 업로드하면 media 폴더가 자동으로 생성된다.
#     date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
#     date_update = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
#
#     def __str__(self):
#         return self.title
