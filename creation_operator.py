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
        
        if initial_coefficient == 0:
            final_state = occupation_state.Occupation_State(0,[],[])
            return final_state
            
        if self.spin == "up":
            final_up_spin_list = []
            skips = 0
            right_index = len(initial_up_spin_list)
            for extra_skips,number in enumerate(initial_up_spin_list):
                if number == operator_numerical_index:
                    final_coefficient = 0 # annihilation
                elif operator_numerical_index > number:
                    right_index = extra_skips
                    break
                else:
                    skips = skips + extra_skips
                    final_up_spin_list.append(number)
            if final_coefficient != 0:
                final_coefficient = initial_coefficient * (-1)**skips
                final_up_spin_list.append(operator_numerical_index)
                while right_index < len(initial_up_spin_list):
                    final_up_spin_list.append(initial_up_spin_list[right_index])
                    right_index = right_index + 1
        else:
            final_down_spin_list = []
            skips = len(initial_up_spin_list)
            right_index = len(initial_down_spin_list)
            for extra_skips,number in enumerate(initial_down_spin_list):
                if number == operator_numerical_index:
                    final_coefficient = 0 # annihilation
                elif operator_numerical_index > number:
                    right_index = extra_skips 
                    break
                else:
                    skips = skips + extra_skips 
                    final_down_spin_list.append(number)
            if final_coefficient != 0:
                final_coefficient = initial_coefficient * (-1)**skips
                final_down_spin_list.append(operator_numerical_index)
                while right_index < len(initial_down_spin_list):
                    final_down_spin_list.append(initial_down_spin_list[right_index])
                    right_index = right_index + 1
                
        
        final_state = occupation_state.Occupation_State(final_coefficient,final_up_spin_list,final_down_spin_list)
        return final_state