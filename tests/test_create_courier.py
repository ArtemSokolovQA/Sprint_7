import allure
import data
from helper import TestDataHelper
import pytest
from scooter_api import ScooterApi
from data import DataTestCreateCourier


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

    @allure.title('Невозможно создать курьера с незаполненнным полем login')
    def test_impossible_to_create_courier_if_login_field_is_empty(self):
        response = ScooterApi.create_courier(DataTestCreateCourier.register_courier_body_empty_login)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Невозможно создать курьера с незаполненнным полем password')
    def test_impossible_to_create_courier_if_password_field_is_empty(self):
        response = ScooterApi.create_courier(DataTestCreateCourier.register_courier_body_empty_password)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'



