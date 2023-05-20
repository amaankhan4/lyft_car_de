class Spindler:
    def needs_service(last_service_date,current_date):
        if(current_date - last_service_date) > 2:
            return True
        else:
            return False