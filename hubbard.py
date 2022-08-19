import annihilation_operator
import creation_operator
import numpy

class Hubbard:
    def __init__(self,U,t,system):
        self.U = U
        self.t = t
        self.V = system.number_of_sites
        self.hopping_matrix = numpy.zeros((self.V,self.V))
        self.connected_ends = system.connected_ends
        for i in range(self.V):
            for j in range(self.V):
                if abs(i-j)==1:
                    self.hopping_matrix[i][j] = t
                if self.connected_ends == True:
                    if abs(i-j) == self.V-1:
                        self.hopping_matrix[i][j] = t
        self.spin_options = system.spin_options
        self.basis_states = system.get_basis_states()
        self.dimension = len(self.basis_states)
    def apply_kinetic_operator(self,basis_state):
        resulting_states = []
        for i in range(self.V):
            for j in range(self.V):
                for index,spin_option in enumerate(self.spin_options):
                    c_j_sigma = annihilation_operator.Annihilation_Operator(j,spin_option)
                    result_1 = c_j_sigma.apply(basis_state)
                    c_dagger_i_sigma = creation_operator.Creation_Operator(i,spin_option)
                    result_2 = c_dagger_i_sigma.apply(result_1)
                    result_2.coefficient = result_2.coefficient * self.hopping_matrix[i,j] 
                    resulting_states.append(result_2)
        return resulting_states
    def apply_interaction_operator(self,basis_state):
        resulting_states = []
        for i in range(self.V):
            c_i_down = annihilation_operator.Annihilation_Operator(i,"down")
            result_1 = c_i_down.apply(basis_state)
            c_dagger_i_down = creation_operator.Creation_Operator(i,"down")
            result_2 = c_dagger_i_down.apply(result_1)
            c_i_up = annihilation_operator.Annihilation_Operator(i,"up")
            result_3 = c_i_up.apply(result_2)
            c_dagger_i_up = creation_operator.Creation_Operator(i,"up")
            result_4 = c_dagger_i_up.apply(result_3) 
            result_4.coefficient = result_4.coefficient * self.U 
            resulting_states.append(result_4)
        return resulting_states
    def form_kinetic_matrix(self):
        kinetic_matrix = numpy.zeros((self.dimension,self.dimension))
        for row,right_basis_state in enumerate(self.basis_states):
            for col,left_basis_state in enumerate(self.basis_states):
                list_of_states = self.apply_kinetic_operator(right_basis_state)
                kinetic_matrix[row][col] = left_basis_state.scalar_product_with_list_of_states(list_of_states)
        return kinetic_matrix
    def form_interaction_matrix(self):
        interaction_matrix = numpy.zeros((self.dimension,self.dimension))
        for row,right_basis_state in enumerate(self.basis_states):
            for col,left_basis_state in enumerate(self.basis_states):
                list_of_states = self.apply_interaction_operator(right_basis_state)
                interaction_matrix[row][col] = left_basis_state.scalar_product_with_list_of_states(list_of_states)
        return interaction_matrix
    def form_Hamiltonian_matrix(self):
        return numpy.add(self.form_kinetic_matrix(),self.form_interaction_matrix())
    def diagonalize_Hamiltonian_matrix(self):
        # CODE GOES HERE
        pass
    def write_eigenvalues_and_eigenvectors(self):
        # CODE GOES HERE
        pass
    def write_ground_state_eigenvalue_and_eigenvector(self):
        # CODE GOES HERE
        pass