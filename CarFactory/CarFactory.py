from engine.CapuletEngine import CapuletEngine
from engine.SternmanEngine import SternmanEngine
from engine.WilloughbyEngine import WilloughbyEngine
from Battery.Nubbing import Nubbing
from Battery.Spindler import Spindler
from car import Car
from tire import carrigen_tire,Octoprime_tire
class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine=CapuletEngine(current_mileage, last_service_mileage)
        battery=Spindler(current_date, last_service_date)
        return car(engine,battery)

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine=WillooughbyEngine(current_mileage, last_service_mileage)
        battery=Spindler(current_date, last_service_date)
        return car(engine,battery)

    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine=SternmanEngine(warning_light_on)
        battery=Spindler(current_date, last_service_date)
        return car(engine,battery)

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine=WillooughbyEngine(current_mileage, last_service_mileage)
        battery=Nubbing(current_date, last_service_date)
        return car(engine,battery)
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine=CapuletEngine(current_mileage, last_service_mileage)
        battery=Nubbing(current_date, last_service_date)
        return car(engine,battery)
