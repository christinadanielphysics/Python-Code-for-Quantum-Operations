import occupation_state

class Annihilation_Operator:
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
        
        if self.spin == "up":
            skips = 0
            if (self.spin in initial_up_spin_list):
                # CODE GOES HERE
            else:
                final_coefficient = 0.0 # annihilation
        else:
            skips = len(initial_up_spin_list)
            if (self.spin in initial_down_spin_list):
                # CODE GOES HERE
            else:
                final_coefficient  = 0.0 # annihilation
        
        final_state = occupation_state.Occupation_State(final_coefficient,final_up_spin_list,final_down_spin_list) 
        return final_state
