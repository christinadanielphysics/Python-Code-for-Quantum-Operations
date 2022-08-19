import quantum_state
import creation_operator

class Occupation_State(quantum_state.Quantum_State):
    def __init__(self,coefficient,up_spin_list,down_spin_list):
        super().__init__(coefficient)
        self.up_spin_list = up_spin_list 
        self.down_spin_list = down_spin_list 
    def write_coefficient_of_state(self,f):
        f.write(str(self.coefficient))
    def write_vacuum_state(self,f):
        f.write("\ket{0}")
    def write_up_operators_of_state(self,f):
        for index,number in enumerate(self.up_spin_list):
            creation_operator.Creation_Operator(number,"up").write_c_dagger(f)
    def write_down_operators_of_state(self,f):
        for index,number in enumerate(self.down_spin_list):
            creation_operator.Creation_Operator(number,"down").write_c_dagger(f)
    def write(self,my_latex_file):
        my_latex_file.start_latex_equation()
        self.write_coefficient_of_state(my_latex_file.f)
        self.write_up_operators_of_state(my_latex_file.f)
        self.write_down_operators_of_state(my_latex_file.f)
        self.write_vacuum_state(my_latex_file.f)
        my_latex_file.end_latex_equation()
    def scalar_product(self,other):
        if self.up_spin_list == other.up_spin_list and self.down_spin_list == other.down_spin_list:
            return self.coefficient * other.coefficient
        else:
            return 0
    def scalar_product_with_list_of_states(self,list_of_states):
        number = 0
        for index,state in enumerate(list_of_states):
            number = number + self.scalar_product(state)
        return number
            
        