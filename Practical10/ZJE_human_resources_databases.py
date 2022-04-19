class Staff(object):
     def __init__(self,first_name,last_name,location,role):
         self.fn=first_name
         self.ln=last_name
         self.loc=location
         self.ro=role
     def inform (self):
         inf="full name:"+self.fn+self.ln+" location:"+self.loc+" role:"+self.ro
         print(inf)
         return inf
          
a=Staff("Mary","Smith","International_Campus","professor")
a.inform()
