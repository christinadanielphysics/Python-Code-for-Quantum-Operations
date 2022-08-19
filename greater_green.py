import hubbard
import system
import creation_operator
import annihilation_operator

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
        eigenvalues_n_plus_one,eigenvectors_n_plus_one = self.get_eigenstates_for_n_plus_one_electrons()
        # CODE GOES HERE
    def get_time_version(self):
        # CODE GOES HERE
        pass