import occupation_state

class Annihilation_Operator:
    def __init__(self,numerical_index,spin):
        self.numerical_index = numerical_index 
        self.spin = spin 
    def apply(self,simplified_occupation_state):
        
        initial_up_spin_list = simplified_occupation_state.up_spin_list
        initial_down_spin_list = simplified_occupation_state.down_spin_list
        initial_coefficient = simplified_occupation_state.coefficient
        
        if initial_coefficient == 0:
            final_state = occupation_state.Occupation_State(0.0,[],[])
            return final_state
        
        final_up_spin_list = initial_up_spin_list
        final_down_spin_list = initial_down_spin_list
        final_coefficient = 0 # annihilation

        operator_numerical_index = self.numerical_index
        
        if self.spin == "up":
            final_up_spin_list = []
            skips = 0
            for extra_skips,number in enumerate(initial_up_spin_list):
                if number == operator_numerical_index:
                    skips = skips + extra_skips
                    final_coefficient = initial_coefficient * (-1)**skips
                else:
                    final_up_spin_list.append(number) 
        else:
            final_down_spin_list = []
            skips = len(initial_up_spin_list)
            for extra_skips,number in enumerate(initial_down_spin_list):
                if number == operator_numerical_index:
                    skips = skips + extra_skips
                    final_coefficient = initial_coefficient * (-1)**skips
                else:
                    final_down_spin_list.append(number) 
        
        final_state = occupation_state.Occupation_State(final_coefficient,final_up_spin_list,final_down_spin_list) 
        return final_state
    def write_c(self,f):
        spin_symbol = 0
        if self.spin == "up":
            spin_symbol = r"\uparrow"
        else:
            spin_symbol = r"\downarrow"
        f.write("\hat{c}_{"+str(self.numerical_index)+spin_symbol+"}")