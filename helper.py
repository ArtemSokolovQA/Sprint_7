from data import DataTestCreateCourier
from faker import Faker


class TestDataHelper:

    @staticmethod
    def modify_create_courier_body(key, value):
        body = DataTestCreateCourier.register_courier_body.copy()
        body[key] = value
        return body

    def generate_create_courier_body(self):
        fake = Faker()
        return self.modify_create_courier_body('login', fake.user_name()[:7])
