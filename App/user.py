class User:
    def __init__(self, name, salary,tax, weeks):
        self.name = name
        self.salary = salary
        self.tax = tax
        self.weeks = weeks
    def displayUser(self):
        print ("Name : ", self.name, ", Salary: ", self.salary,", Tax: ",self.tax,", Weeks: ", self.weeks)
    def getUser(self):
       return (self.name,self.salary,self.tax,self.weeks)