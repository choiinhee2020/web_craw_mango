import random

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer


class RestaurantTest(APITestCase):
    """
    Postmane이 하는 일을 코드로 자동화
    DB는 분리됨
    """

    def test_restaurant_list(self):
        url = '/api-view/restaurants/'

        # request 같은 역할( http get 요청을 보냄)
        response = self.client.get(url)

        # assert 기대하는 것!! status code 가 200dlfkrh rleogka
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len((response.data, 0)))

        for i in range(5):
            Restaurant.objects.create(name='1', name_address1_unique=i)
        response = self.client.get(url)
        #
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # # self.assertEqual(len(response.data), 4)
        #
        # for restaurant_data in response.data:
        #     self.assertIn('name', restaurant_data)
        #     self.assertIn('address1', restaurant_data)
        #     self.assertIn('name_address1_unique', restaurant_data)
        #     self.assertIn('address2', restaurant_data)
        #     self.assertIn('phone', restaurant_data)

            # 전달된 Restaurant object(dict)dml 'pk'에 해당하는
            # 실제 Restaurant model instance를
            # RestaurantSerializer을 통해 serializer한 값과 restaurant_data가 같은지 비교

            # pk = restaurant_data['id']
            # restaurant = Restaurant.objects.get(pk=pk)
            # self.assertEqual(
            #     RestaurantSerializer(restaurant).data,
            #     restaurant_data
            #     )

    def test_restaurant_create(self):
        """
        Res
        :return:
        """
        url = '/api-view/restaurants/'

        # Restaurant객체를 만들기 위해 클라이언트로부터 전달될 JSON객체를 Parse한 Python객체
        data = {
            "name":"이층집",
            "name_address1_unique":"uuid",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 응답에 돌아온 객체가 RestaurantSerializer로
        # 실제 Model instance를 serialize한 결과와 같은지 확인
        pk = response.data['id']
        restaurant = Restaurant.objects.get(pk=pk)
        self.assertEqual(
            response.data,
            RestaurantSerializer(restaurant).data
        )

        # 객체를 하나 생성했으니, 전체 Restaurant객체의 개수가 1개인지 확인(ORM)
        self.assertEqual(Restaurant.objects.count(), 1)

    def test_restaurant_delete(self):
        # 미리 객체를 5개 만들어 놓는다.
        # delete API를 적절히 실행 한 후, 객체가 4개가 되었는지 확인
        # 지운 객체가 실제로 존재하지 않는지 확인
        restaurants = [Restaurant.objects.create(name=i, name_address1_unique=i) for i in range(5)]
        self.assertEqual(Restaurant.objects.count(), 5)

        restaurant = random.choice(restaurants)
        url = f'/api-view/restaurants/{restaurant.id}/'

        # delete는 안보내줘도 됨 data
        response = self.client.delete(url)

        # self.assertEqual(response.status_code, status.HTTP301)
        self.assertEqual(Restaurant.objects.count(), 4)
        # 지워진 id 존재하는지 확인
        self.assertFalse(
            Restaurant.objects.filter(id=restaurant.id).exists()
        )





















