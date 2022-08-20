import hubbard
import system
import creation_operator
import annihilation_operator
import occupation_state

class Greater_Green:
    def __init__(self,spin,i,j,system_n,U_value,t_value):
        self.spin = spin
        self.i = i 
        self.j = j
        self.system_n = system_n
        self.system_n_plus_one = system.System(system_n.number_of_sites, system_n.number_of_up_electrons + 1, system_n.number_of_down_electrons, system_n.connected_ends)
        self.U_value = U_value
        self.t_value = t_value
        self.c_operator = annihilation_operator.Annihilation_Operator(self.i,self.spin)
        self.c_dagger_operator = creation_operator.Creation_Operator(self.j,self.spin)
    def get_eigenstates_for_n_electrons(self):
        hubbard_n = hubbard.Hubbard(self.U_value,self.t_value,self.system_n)
        eigenvalues,eigenvectors = hubbard_n.diagonalize_hamiltonian_matrix()
        return eigenvalues,eigenvectors
    def get_eigenstates_for_n_plus_one_electrons(self):
        hubbard_n_plus_one = hubbard.Hubbard(self.U_value,self.t_value,self.system_n_plus_one)
        eigenvalues,eigenvectors = hubbard_n_plus_one.diagonalize_hamiltonian_matrix()
        return eigenvalues,eigenvectors
    def get_angular_frequencies_and_weights(self):
        eigenvalues_n,eigenvectors_n = self.get_eigenstates_for_n_electrons()
        ground_state_energy_n = eigenvalues_n[0]
        ground_state_n = eigenvectors_n[:,0]
        
        eigenvalues_n_plus_one,eigenvectors_n_plus_one = self.get_eigenstates_for_n_plus_one_electrons()
        basis_n = self.system_n.get_basis_states()
        basis_n_plus_one = self.system_n_plus_one.get_basis_states()
        
        # CODE GOES HERE
        
        right_occupation_states_n = []
        for index,coefficient_from_ground_state in enumerate(ground_state_n):
            occupation_state_from_ground_state = occupation_state.Occupation_State(coefficient_from_ground_state,basis_n[index].up_spin_list,basis_n[index].down_spin_list)
            right_occupation_states_n.append(self.c_dagger_operator.apply(occupation_state_from_ground_state))
        
        left_occupation_states_n = []
        for index,coefficient_from_ground_state in enumerate(ground_state_n):
            occupation_state_from_ground_state = occupation_state.Occupation_State(coefficient_from_ground_state,basis_n[index].up_spin_list,basis_n[index].down_spin_list)
            left_occupation_states_n.append(occupation_state_from_ground_state)
                
        angular_frequencies = []
        weights = []
        for a,n_plus_one_eigenvalue_a in enumerate(eigenvalues_n_plus_one):
            angular_frequencies.append(n_plus_one_eigenvalue_a - ground_state_energy_n)
            
            left_occupation_states_n_plus_one = []
            for index,coefficient_from_eigenstate in enumerate(eigenvectors_n_plus_one[:,a]):
                occupation_state_from_eigenstate = occupation_state.Occupation_State(coefficient_from_eigenstate,basis_n_plus_one[index].up_spin_list,basis_n_plus_one[index].down_spin_list)
                left_occupation_states_n_plus_one.append(occupation_state_from_eigenstate)
                
            right_occupation_states_n_plus_one = []
            for index,coefficient_from_eigenstate in enumerate(eigenvectors_n_plus_one[:,a]):
                occupation_state_from_eigenstate = occupation_state.Occupation_State(coefficient_from_eigenstate,basis_n_plus_one[index].up_spin_list,basis_n_plus_one[index].down_spin_list)
                result = self.c_operator.apply(occupation_state_from_eigenstate)
                right_occupation_states_n_plus_one.append(result)
            
            bracket_1 = 0
            for right_index,right_state in enumerate(right_occupation_states_n):
                for left_index,left_state in enumerate(left_occupation_states_n_plus_one):
                    bracket_1 = bracket_1 + right_state.scalar_product(left_state)
    
            bracket_2 = 0
            for right_index,right_state in enumerate(right_occupation_states_n_plus_one):
                for left_index,left_state in enumerate(left_occupation_states_n):
                    bracket_2 = bracket_2 + right_state.scalar_product(left_state)
                
            weight = bracket_1 * bracket_2 
            weights.append(weight)
            
        return angular_frequencies,weights
    def get_time_version(self):
        # CODE GOES HERE
        pass