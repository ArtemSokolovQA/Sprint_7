#
from data import DataTestLoginCourier
import pytest
from scooter_api import ScooterApi


@pytest.fixture
def login_courier():
    return ScooterApi.login_courier(DataTestLoginCourier.login_courier_body)

# @pytest.fixture
# def delete_courier(request):
#     def teardown():
#         ScooterApi.delete_courier(courier_id=)
#
#     request.addfinalizer(teardown)
