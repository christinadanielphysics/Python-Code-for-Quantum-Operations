import itertools
import basis_state

class System:
    def __init__(self,number_of_sites,number_of_up_electrons,number_of_down_electrons,connected_ends):
        self.number_of_sites = number_of_sites 
        self.number_of_up_electrons = number_of_up_electrons 
        self.number_of_down_electrons = number_of_down_electrons
        self.connected_ends = connected_ends
        self.spin_options = ["up","down"]
    def get_up_spin_lists(self):
        all_lists = []
        objects =  itertools.combinations(range(self.number_of_sites),self.number_of_up_electrons)
        for index,object in enumerate(objects):
            new_list = []
            i = 0
            while i < len(object):
                new_list.append(object[i])
                i = i + 1
            all_lists.append(new_list)
        return all_lists
    def get_down_spin_lists(self):
        all_lists = []
        objects = itertools.combinations(range(self.number_of_sites),self.number_of_down_electrons)
        for index,object in enumerate(objects):
            new_list = []
            i = 0
            while i < len(object):
                new_list.append(object[i])
                i = i + 1
            all_lists.append(new_list)
        return all_lists
    def get_basis_states(self):
        all_basis_states = []
        up_lists = self.get_up_spin_lists()
        down_lists = self.get_down_spin_lists()
        for up_index,up_list in enumerate(up_lists):
            for down_index,down_list in enumerate(down_lists):
                state = basis_state.Basis_State(1,up_list,down_list)
                all_basis_states.append(state)
        return all_basis_states
    def print_basis_states(self,my_latex_file):
        all_basis_states = self.get_basis_states()
        for index,state in enumerate(all_basis_states):
            state.write(my_latex_file)

