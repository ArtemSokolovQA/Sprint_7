import allure

import data
from helper import TestDataHelper
import pytest
from scooter_api import ScooterApi


class TestCreateCourier:

    @allure.title('Проверка возможности создания курьера с валидными данными')
    def test_is_possible_to_create__courier(self):
        response = ScooterApi.create_courier(TestDataHelper.generate_create_courier_body())
        print(response.request.body)
        assert response.status_code == 201
        assert response.json()['ok']
