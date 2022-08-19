import occupation_state
import creation_operator

class Basis_State(occupation_state.Occupation_State):
    def __init__(self,coefficient,up_spin_list,down_spin_list):
        super().__init__(coefficient,up_spin_list,down_spin_list)
        self.coefficient = 1
    def write_vacuum_state(self,f):
        f.write("\ket{0}")
    def write_up_operators_of_state(self,f):
        for index,number in enumerate(self.up_spin_list):
            creation_operator.Creation_Operator(number,"up").write_c_dagger(f)
    def write_down_operators_of_state(self,f):
        for index,number in enumerate(self.down_spin_list):
            creation_operator.Creation_Operator(number,"down").write_c_dagger(f)
    def write(self,my_latex_file):
        self.write_up_operators_of_state(my_latex_file.f)
        self.write_down_operators_of_state(my_latex_file.f)
        self.write_vacuum_state(my_latex_file.f)
        
        
