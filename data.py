from faker import Faker

fake = Faker()


class DataTestCreateCourier:
    register_courier_body = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }

    courier_id = 377684

    register_courier_body_empty_login = {
        "login": "",
        "password": "1234",
        "firstName": "saske"
    }

    register_courier_body_empty_password = {"login": "kakashi",
                                            "password": "",
                                            "firstName": "saske"
                                            }


class DataTestLoginCourier:
    login_courier_body = {
        "login": "ninjaTester",
        "password": "1234"
    }

    login_courier_body_empty_login = {
        "login": "",
        "password": "1234"
    }

    login_courier_body_empty_password = {
        "login": "ninjaTester",
        "password": ""
    }

    login_courier_body_wrong_password = {
        "login": "ninjaTester",
        "password": "12345"
    }

    login_courier_body_wrong_login = {
        "login": "ninjaQA",
        "password": "12345"
    }


class DataTestCreateOrder:
    create_order_body = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }

    colors_list = [['BLACK', 'GREY'],  ['BLACK'], ['GREY'], []]


class DataTestOrdersList:

    query_params = {'id': ''}


class ResponseMessages:

    courier_already_exists_message = 'Этот логин уже используется. Попробуйте другой.'
    not_enough_data_to_register_message = 'Недостаточно данных для создания учетной записи'
    not_enough_data_to_login_message = 'Недостаточно данных для входа'
    account_not_found_message = 'Учетная запись не найдена'
