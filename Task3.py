
#from time import sleep для приостановления действий


accounting = {
    'w_engineer': 10,
    'b_engineer': 5,
    'w_driver': 8,
    'b_driver': 8,
    }



class Worker:
    def __init__(self, us_name, us_surename, us_position):
        self.name = us_name
        self.surname = us_surename
        self.position = us_position
        self._income = accounting['w_'+self.position] + accounting['b_'+self.position]

class Position (Worker):

    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        print(self._income)




class_run_1=Position('alex', 'petrov', 'engineer')
class_run_1.get_full_name()
class_run_1.get_total_income()

class_run_2=Position('Petya', 'Sidorov', 'driver')
class_run_2.get_full_name()
class_run_2.get_total_income()