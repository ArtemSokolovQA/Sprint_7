import allure
from scooter_api import ScooterApi
from data import DataTestLoginCourier, ResponseMessages


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
        assert response.json()['message'] == ResponseMessages.not_enough_data_to_login_message

    @allure.step('Невозможно авторизоваться курьеру, не заполнив поле password')
    def test_courier_cant_login_with_no_password(self):
        response = ScooterApi.login_courier(DataTestLoginCourier.login_courier_body_empty_password)
        assert response.status_code == 400
        assert response.json()['message'] == ResponseMessages.not_enough_data_to_login_message

    @allure.step('Проверка ошибки при неправильном заполнении поля password')
    def test_login_courier_with_wrong_password_error_expected(self):
        response = ScooterApi.login_courier(DataTestLoginCourier.login_courier_body_wrong_password)
        assert response.status_code == 404
        assert response.json()['message'] == ResponseMessages.account_not_found_message

    @allure.step('Проверка ошибки при неправильном заполнении поля login')
    def test_login_courier_with_wrong_login_error_expected(self):
        response = ScooterApi.login_courier(DataTestLoginCourier.login_courier_body_wrong_login)
        assert response.status_code == 404
        assert response.json()['message'] == ResponseMessages.account_not_found_message
