import allure
import data
from helper import TestDataHelper
import pytest
from scooter_api import ScooterApi
from data import DataTestLoginCourier


class TestLoginCourier:

    def test_courier_can_authorize(self):
        response = ScooterApi.login_courier(DataTestLoginCourier.login_courier_body)
        assert response.status_code == 200
        assert response.json()['id'] != ''



