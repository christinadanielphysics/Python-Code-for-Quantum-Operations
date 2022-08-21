import hubbard
import system
import creation_operator 
import annihilation_operator
import occupation_state
import math


class Lesser_Green:
    def __init__(self,spin,i,j,system_n,U_value,t_value):
        self.spin = spin
        self.i = i 
        self.j = j
        self.system_n = system_n
        self.system_n_minus_one = system.System(system_n.number_of_sites, system_n.number_of_up_electrons - 1, system_n.number_of_down_electrons, system_n.connected_ends)
        self.U_value = U_value
        self.t_value = t_value
        self.c_operator = annihilation_operator.Annihilation_Operator(self.i,self.spin)
        self.c_dagger_operator = creation_operator.Creation_Operator(self.j,self.spin)
        
        hubbard_n = hubbard.Hubbard(self.U_value,self.t_value,self.system_n)
        eigenvalues_n,eigenvectors_n = hubbard_n.diagonalize_hamiltonian_matrix()
        
        self.eigenvalues_n = eigenvalues_n 
        self.eigenvectors_n = eigenvectors_n
        
        self.ground_state_energy_n = eigenvalues_n[0]
        self.ground_state_n = eigenvectors_n[:,0]
        
        hubbard_n_minus_one = hubbard.Hubbard(self.U_value,self.t_value,self.system_n_minus_one)
        eigenvalues_n_minus_one,eigenvectors_n_minus_one = hubbard_n_minus_one.diagonalize_hamiltonian_matrix()
        
        self.eigenvalues_n_minus_one = eigenvalues_n_minus_one
        self.eigenvectors_n_minus_one = eigenvectors_n_minus_one
        
        self.basis_n = self.system_n.get_basis_states()
        self.basis_n_minus_one = self.system_n_minus_one.get_basis_states()
        
        left_occupation_states_n = []
        for index,coefficient_from_ground_state in enumerate(self.ground_state_n):
            occupation_state_from_ground_state = occupation_state.Occupation_State(coefficient_from_ground_state,self.basis_n[index].up_spin_list,self.basis_n[index].down_spin_list)
            left_occupation_states_n.append(occupation_state_from_ground_state)
        self.left_occupation_states_n = left_occupation_states_n
        
        right_occupation_states_n = []
        for index,coefficient_from_ground_state in enumerate(self.ground_state_n):
            occupation_state_from_ground_state = occupation_state.Occupation_State(coefficient_from_ground_state,self.basis_n[index].up_spin_list,self.basis_n[index].down_spin_list)
            right_occupation_states_n.append(self.c_operator.apply(occupation_state_from_ground_state))
        self.right_occupation_states_n = right_occupation_states_n
    def c_dagger_bracket(self,a):
        right_occupation_states_n_minus_one = []
        for index,coefficient_from_eigenstate in enumerate(self.eigenvectors_n_minus_one[:,a]):
            occupation_state_from_eigenstate = occupation_state.Occupation_State(coefficient_from_eigenstate,self.basis_n_minus_one[index].up_spin_list,self.basis_n_minus_one[index].down_spin_list)
            result = self.c_dagger_operator.apply(occupation_state_from_eigenstate)
            right_occupation_states_n_minus_one.append(result)
        bracket_2 = 0
        for right_index,right_state in enumerate(right_occupation_states_n_minus_one):
            for left_index,left_state in enumerate(self.left_occupation_states_n):
                bracket_2 = bracket_2 + right_state.scalar_product(left_state)      
        return bracket_2
    def c_bracket(self,a):
        left_occupation_states_n_minus_one = []
        for index,coefficient_from_eigenstate in enumerate(self.eigenvectors_n_minus_one[:,a]):
            occupation_state_from_eigenstate = occupation_state.Occupation_State(coefficient_from_eigenstate,self.basis_n_minus_one[index].up_spin_list,self.basis_n_minus_one[index].down_spin_list)
            left_occupation_states_n_minus_one.append(occupation_state_from_eigenstate)   
        bracket_1 = 0
        for right_index,right_state in enumerate(self.right_occupation_states_n):
            for left_index,left_state in enumerate(left_occupation_states_n_minus_one):
                bracket_1 = bracket_1 + right_state.scalar_product(left_state)
        return bracket_1
    def get_angular_frequencies_and_weights(self):
        angular_frequencies = []
        weights = []
        for a,n_minus_one_eigenvalue_a in enumerate(self.eigenvalues_n_minus_one):
            angular_frequencies.append(self.ground_state_energy_n - n_minus_one_eigenvalue_a)
            bracket_1 = self.c_bracket(a)
            bracket_2 = self.c_dagger_bracket(a)
            weights.append(bracket_1 * bracket_2)  
        return angular_frequencies,weights
    def get_time_version(self,time_values):
        function_values = []
        for time_index,t_value in enumerate(time_values):
            function_value = 0
            for a,n_minus_one_eigenvalue_a in enumerate(self.eigenvalues_n_minus_one):
                bracket_1 = self.c_bracket(a)
                bracket_2 = self.c_dagger_bracket(a)
                function_value = function_value + bracket_1 * bracket_2 * math.cos( (n_minus_one_eigenvalue_a - self.ground_state_energy_n) * t_value )
            function_values.append(function_value)
        return function_values
