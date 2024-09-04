from data import TestCreateCourier
from faker import Faker


class TestDataHelper:

    @staticmethod
    def modify_create_courier_body(key, value):
        body = TestCreateCourier.register_courier_body.copy()
        body[key] = value
        return body

    @staticmethod
    def generate_create_courier_body():
        fake = Faker()
        return TestDataHelper.modify_create_courier_body('login', fake.user_name()[:7])
