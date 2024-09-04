from faker import Faker

fake = Faker()


class DataTestCreateCourier:
    register_courier_body = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }

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
