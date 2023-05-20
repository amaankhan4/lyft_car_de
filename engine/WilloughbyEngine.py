class WilloughbyEngine implements Engine:
    def needs_service(last_service_milage,current_mileage):
        if(current_mileage - last_service_milage) > 60000:
            return True
        else:
            return False    