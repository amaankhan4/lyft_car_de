class CapulteEngine implements Engine:
    def needs_service(last_service_milage,current_mileage):
        if(current_mileage - last_service_milage) > 30000:
            return True
        else:
            return False    