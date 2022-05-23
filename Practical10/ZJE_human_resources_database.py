class Staff():
    def __init__(self,first_name,last_name,location,role):
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
        self.role=role
    def information(self):
        print(self.first_name,self.last_name,'is the ',self.role,'in',self.location)
Staff.information(Staff('Emma','Stone','International Campus','faculty'))
