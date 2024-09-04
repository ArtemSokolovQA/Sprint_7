import allure
import data
from helper import TestDataHelper
import pytest
from scooter_api import ScooterApi
from data import DataTestLoginCourier
from conftest import login_courier
from data import DataTestOrdersList


class TestOrdersList:

    @allure.title('Проверка, что в списке заказов содержатся заказы')
    def test_orders_list_contains_orders(self, login_courier):
        courier_id = login_courier.json()['id']
        orders_list_params = DataTestOrdersList.query_params.copy()
        orders_list_params['id'] = courier_id
        response = ScooterApi.get_orders_list(orders_list_params)
        assert response.status_code == 200
        assert 'orders' in response.json()
        assert response.json()['orders'] != []

