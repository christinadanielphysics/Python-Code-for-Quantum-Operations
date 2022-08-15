class Creation_Operator:
    def __init__(self,numerical_index,spin_index):
        self.numerical_index = numerical_index
        self.spin_index = spin_index
    def apply(self,simplified_occupation_state):
        return 0