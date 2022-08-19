import quantum_state
import creation_operator

class Occupation_State(quantum_state.Quantum_State):
    def __init__(self,coefficient,up_spin_list,down_spin_list):
        super().__init__(coefficient)
        self.up_spin_list = up_spin_list 
        self.down_spin_list = down_spin_list 
    def write_coefficient_of_state(self,f):
        f.write(str(self.coefficient))
    def write_vacuum_state(f):
        f.write("\ket{0}")
    def write_up_operators_of_state(f,self):
        for index,number in enumerate(self.up_spin_list):
            creation_operator.Creation_Operator(number,"up").write_c_dagger(f)
    def write_down_operators_of_state(f,self):
        for index,number in enumerate(self.down_spin_list):
            creation_operator.Creation_Operator(number,"down").write_c_dagger(f)
    def write(self,f):
        self.write_coefficient_of_state(f)
        self.write_up_operators_of_state(f)
        self.write_down_operators_of_state(f)
        self.write_vacuum_state(f)

        