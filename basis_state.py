import occupation_state
import creation_operator

class Basis_State(occupation_state.Occupation_State):
    def __init__(self,coefficient,up_spin_list,down_spin_list):
        super().__init__(coefficient,up_spin_list,down_spin_list)
        self.coefficient = 1
        
        
