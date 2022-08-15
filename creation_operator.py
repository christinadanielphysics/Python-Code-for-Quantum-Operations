import occupation_state

class Creation_Operator:
    def __init__(self,numerical_index,spin):
        self.numerical_index = numerical_index
        self.spin = spin
    def apply(self,simplified_occupation_state):
        
        initial_up_spin_list = simplified_occupation_state.up_spin_list
        initial_down_spin_list = simplified_occupation_state.down_spin_list
        initial_coefficient = simplified_occupation_state.coefficient
        
        final_up_spin_list = initial_up_spin_list
        final_down_spin_list = initial_down_spin_list 
        final_coefficient = initial_coefficient
        
        operator_numerical_index = self.numerical_index
        
        if self.spin == "up":
            final_up_spin_list = []
            skips = 0
            for extra_skips,number in enumerate(initial_up_spin_list):
                if number == operator_numerical_index:
                    final_coefficient = 0.0 # annihilation
                # CODE GOES HERE
        else:
            final_down_spin_list = []
            skips = len(initial_up_spin_list)
            for extra_skips,number in enumerate(initial_down_spin_list):
                if number == operator_numerical_index:
                    final_coefficient = 0.0 # annihilation
                # CODE GOES HERE
                
                
        
        final_state = occupation_state.Occupation_State(final_coefficient,final_up_spin_list,final_down_spin_list)
        return final_state