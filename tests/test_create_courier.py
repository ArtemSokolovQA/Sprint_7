import allure

import data
from helper import TestDataHelper
import pytest
from scooter_api import ScooterApi


class TestCreateCourier:

    @allure.title('Проверка возможности создания курьера с валидными данными')
    def test_is_possible_to_create__courier(self):
        response = ScooterApi.create_courier(TestDataHelper.generate_create_courier_body())
        assert response.status_code == 201
        assert response.json()['ok']

    @allure.title('Невозможно создать двух курьеров с одинаковыми данными')
    def test_impossible_to_create_2_identical_couriers(self):
        courier_body = TestDataHelper.generate_create_courier_body()
        response_1 = ScooterApi.create_courier(courier_body)
        response_2 = ScooterApi.create_courier(courier_body)
        assert response_1.status_code == 201
        assert response_2.status_code == 409
        assert response_2.json()['code'] == 409
        assert response_2.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'


