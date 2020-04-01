import uuid as uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
import datetime
from config.settings import AUTH_USER_MODEL


class MyUserManager(BaseUserManager):
    def _create_user(self, email, gender, password=None, **kwargs):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        if not gender:
            raise ValueError('성별 선택은 필수입니다.')

        user = self.model(
            email=self.normalize_email(email),
            gender=gender,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, gender, password, **kwargs):
        """
        일반 유저 생성
        """

        kwargs.setdefault('is_admin', False)
        return self._create_user(email, gender, password, **kwargs)

    def create_superuser(self, email, gender, password, **kwargs):
        """
        관리자 유저 생성
        """

        kwargs.setdefault('is_admin', True)
        return self._create_user(email, gender, password, **kwargs)


class MyUser(AbstractBaseUser, PermissionsMixin):
    GENDER = (
        ('남자', '남자'),
        ('여자', '여자'),
    )
    uuid = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='PK'
    )
    gender = models.CharField(max_length=10, choices=GENDER, verbose_name='성별')
    email = models.EmailField(max_length=100, unique=True, verbose_name='이메일')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    date_update = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
    is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')
    like_users = models.ManyToManyField('self', through='SendLikes', related_name='pick_me_users',
                                        symmetrical=False)
    star_users = models.ManyToManyField('self', through='SendStars', related_name='user_star_users',
                                        symmetrical=False)
    pick_users = models.ManyToManyField('self', through='SendPicks', related_name='user_pick_users',
                                        symmetrical=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['gender']

    def __str__(self):
        return "username: " + self.username

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        db_table = 'users'
        verbose_name = '유저'
        verbose_name_plural = '유저들'


class Profile(models.Model):
    MAJOR = [
        ('건축학과', '건축학과'),
        ('교통운송학과', '교통운송학과'),
        ('기계공학과', '기계공학과'),
        ('자동차공학', '자동차공학'),
        ('산업학과', '산업학과'),
        ('광학공학', '과학공학'),
        ('전기공학', '전기공학'),
        ('전자공학', '전자공학'),
        ('응용소프트웨어공학', '응용소프트웨어공학'),
        ('토목학과', '토목학과'),
    ]
    SHAPE = [
        ('마른', '마른'),
        ('슬림탄탄', '슬림탄탄'),
        ('보통', '보통'),
        ('통통한', '통통한'),
        ('살짝볼륨', '살짝볼륨'),
        ('글래머', '글래머'),

    ]
    RESULT = [
        ('P', 'PASS'),
        ('F', 'FAIL'),
        ('Evaluate', 'Evaluate'),
        ('IMPOSSIBLE', 'IMPOSSIBLE'),
    ]
    CHARACTER = [
        ('지적인', '지적인'),
        ('차분한', '차분한'),
        ('유머있는', '유머있는'),
        ('낙천적인', '낙천적인'),
        ('내향적인', '내향적인'),
        ('외향적인', '외향적인'),
        ('감성적인', '감성적인'),
        ('상냥한', '상냥한'),
        ('귀여운', '귀여운'),
        ('섹시한', '섹시한'),
        ('4차원인', '4차원인'),
        ('발랄한', '발랄한'),
        ('도도한', '도도한'),
        ('섹시한', '토목학과'),
    ]
    RELIGION = [
        ('기독교', '기독교'),
        ('천주교', '천주교'),
        ('이슬람교', '이슬람교'),
        ('신천지', '신천지'),
        ('무교', '무교'),
    ]
    BLOOD = [
        ('AB', 'AB형'),
        ('A', 'A형'),
        ('B', 'B형'),
        ('O', 'O형'),
    ]

    author_id = models.OneToOneField(MyUser, on_delete=models.PROTECT)
    nickname = models.CharField(max_length=20, unique=True, verbose_name='닉네임')
    username = models.CharField(max_length=20, verbose_name='이름')
    age = models.PositiveIntegerField(default=20)
    average_point = models.PositiveIntegerField(default=0)
    job = models.CharField(max_length=30, blank=True)
    university = models.CharField(max_length=30, blank=True)
    major = models.CharField(max_length=30, choices=MAJOR, blank=True)
    company_name = models.CharField(max_length=10, help_text='Type company name here', blank=True)
    location = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=50, blank=True)
    body_shape = models.CharField(choices=SHAPE, max_length=10, blank=True)
    character = models.CharField(choices=CHARACTER, max_length=20, blank=True)
    date_style = models.CharField(max_length=20, blank=True)
    result = models.CharField(choices=RESULT, max_length=10, blank=True)
    status = models.BooleanField(default=False)
    chance = models.PositiveIntegerField(default=1)
    rank = models.PositiveIntegerField(default=50)
    perfection = models.PositiveIntegerField(default=50)
    religion = models.CharField(choices=RELIGION, max_length=10, blank=True)
    height = models.PositiveIntegerField(default=150)
    intro = models.CharField(max_length=500, blank=True)
    blood = models.CharField(choices=BLOOD, max_length=10, blank=True)
    smoke = models.BooleanField(default=False)
    alcohol = models.BooleanField(default=False)

    birth_date = models.DateTimeField(default=datetime.date(1999, 1, 1))
    date_joined = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.age = timezone.now().year - self.birth_date.year
        # if self.chance > 3:
        #     self.result = 'IMPOSSIBLE'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'계정 닉네임 : {self.nickname} '

# 고민 userimage를 프로필필드에 추가하여 foreignkey를 user에 걸것 이냐
# (onetoone)user - profile에 foreignkey 걸것인가
# user에 foreignkey를 걸 것이냐
class MyUserImage(models.Model):
    author_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, upload_to="account/profile")


class SendLikes(models.Model):
    current_user = models.ForeignKey(MyUser, related_name='current_user_sendlikes_set',
                                     on_delete=models.CASCADE)
    give_point = models.PositiveIntegerField(default=0)
    friend = models.ForeignKey(MyUser, related_name='friend_sendlikes_set',
                               on_delete=models.CASCADE)
    take_point  = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)


class SendStars(models.Model):
    current_user = models.ForeignKey(MyUser, related_name='current_user_sendstars_set',
                                     on_delete=models.CASCADE)
    give_point = models.PositiveIntegerField(default=0)
    friend = models.ForeignKey(MyUser, related_name='friend_sendstars_set',
                               on_delete=models.CASCADE)
    take_point  = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)


class SendPicks(models.Model):
    current_user = models.ForeignKey(MyUser, related_name='current_user_sendpicks_set',
                                     on_delete=models.CASCADE)
    give_point = models.PositiveIntegerField(default=0)
    friend = models.ForeignKey(MyUser, related_name='friend_sendpicks_set',
                               on_delete=models.CASCADE)
    take_point  = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
