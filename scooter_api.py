import allure
import requests
from data import TestCreateCourier
import urls


class ScooterApi:

    @allure.step('Создать курьера')
    @staticmethod
    def create_courier(body):
        return requests.post(f'{urls.BASE_URL}{urls.REGISTER_COURIER_PATH}', json=body)

    @allure.step('Удалить курьера')
    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f'{urls.BASE_URL}{urls.DELETE_COURIER_PATH}', params=courier_id)

