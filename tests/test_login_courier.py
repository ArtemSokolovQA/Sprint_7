import allure
import data
from helper import TestDataHelper
import pytest
from scooter_api import ScooterApi
from data import DataTestLoginCourier


class TestLoginCourier:

    @allure.title('Проверка возможности залогиниться курьеру')
    def test_courier_can_login(self):
        response = ScooterApi.login_courier(DataTestLoginCourier.login_courier_body)
        assert response.status_code == 200
        assert response.json()['id'] != ''

    @allure.step('Невозможно авторизоваться, не заполнив поле login')
    def test_courier_cant_login_with_no_login(self):
        response = ScooterApi.login_courier(DataTestLoginCourier.login_courier_body_empty_login)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'

    @allure.step('Невозможно авторизоваться курьеру, не заполнив поле password')
    def test_courier_cant_login_with_no_password(self):
        response = ScooterApi.login_courier(DataTestLoginCourier.login_courier_body_empty_password)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'

    @allure.step('Проверка ошибки при неправильном заполнении поля password')
    def test_login_courier_with_wrong_password_error_expected(self):
        response = ScooterApi.login_courier(DataTestLoginCourier.login_courier_body_wrong_password)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'

    @allure.step('Проверка ошибки при неправильном заполнении поля login')
    def test_login_courier_with_wrong_login_error_expected(self):
        response = ScooterApi.login_courier(DataTestLoginCourier.login_courier_body_wrong_login)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'
