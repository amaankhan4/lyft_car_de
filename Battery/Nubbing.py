class Nubbing:
    def needs_service(last_service_date,current_date):
        if(current_date - last_service_date) > 4:
            return True
        else:
            return False
