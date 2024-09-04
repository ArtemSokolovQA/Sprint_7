import allure
import requests
from data import DataTestCreateCourier
import urls


class ScooterApi:

    @staticmethod
    @allure.step('Создать курьера')
    def create_courier(body):
        return requests.post(f'{urls.BASE_URL}{urls.REGISTER_COURIER_PATH}', json=body)

    @staticmethod
    @allure.step('Удалить курьера')
    def delete_courier(courier_id):
        return requests.delete(f'{urls.BASE_URL}{urls.DELETE_COURIER_PATH}', params=courier_id)

    @staticmethod
    @allure.step('Авторизовать курьера')
    def login_courier(body):
        return requests.post(f'{urls.BASE_URL}{urls.AUTH_COURIER_PATH}', json=body)

    @staticmethod
    @allure.step('Создать заказ')
    def create_order(body):
        return requests.post(f'{urls.BASE_URL}{urls.CREATE_ORDER_PATH}', json=body)

    @staticmethod
    @allure.step('Получить список заказов')
    def get_orders_list(params):
        return requests.get(f'{urls.BASE_URL}{urls.GET_ORDERS_LIST_PATH}', params=params)


