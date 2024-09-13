import allure
import pytest
from scooter_api import ScooterApi
from data import DataTestCreateOrder


class TestCreateOrder:

    @allure.step('Возможно заказать самокат различных цветов')
    @pytest.mark.parametrize('color', DataTestCreateOrder.colors_list)
    def test_possible_to_create_order_with_different_colors(self, color):
        order_body = DataTestCreateOrder.create_order_body.copy()
        order_body["color"] = color
        response = ScooterApi.create_order(order_body)
        assert response.status_code == 201
        assert 'track' in response.json()
