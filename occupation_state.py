import quantum_state

class Occupation_State(quantum_state.Quantum_State):
    def __init__(self,coefficient,up_spin_list,down_spin_list):
        super().__init__(coefficient)
        self.up_spin_list = up_spin_list 
        self.down_spin_list = down_spin_list 
        