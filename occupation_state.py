import quantum_state

class Occupation_State(quantum_state.Quantum_State):
    def __init__(self,coefficient,ordered_list):
        super().__init__(coefficient)
        self.ordered_list = ordered_list