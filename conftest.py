from data import DataTestLoginCourier
import pytest
from scooter_api import ScooterApi


@pytest.fixture
def login_courier():
    return ScooterApi.login_courier(DataTestLoginCourier.login_courier_body)

