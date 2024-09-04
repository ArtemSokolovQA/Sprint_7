from faker import Faker

fake = Faker()


class TestCreateCourier:
    register_courier_body = {
        "login": "ninja",
        "password": "1234",
        "firstName": "saske"
    }
