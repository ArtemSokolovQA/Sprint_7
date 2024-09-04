import allure
import data
from helper import TestDataHelper
import pytest
from scooter_api import ScooterApi
from data import DataTestLoginCourier


class TestLoginCourier:

    def test_courier_can_login(self):
        response = ScooterApi.login_courier(DataTestLoginCourier.login_courier_body)
        assert response.status_code == 200
        assert response.json()['id'] != ''

    def test_courier_cant_login_with_no_login(self):
        response = ScooterApi.login_courier(DataTestLoginCourier.login_courier_body_empty_login)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'

    def test_courier_cant_login_with_no_password(self):
        response = ScooterApi.login_courier(DataTestLoginCourier.login_courier_body_empty_password)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'
