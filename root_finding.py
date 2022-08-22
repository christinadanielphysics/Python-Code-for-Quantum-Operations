import numpy
import sympy
import math
import os
from scipy import optimize
import matplotlib.pyplot as plt


V = 2
K = 0

t = sympy.Symbol('t')

tol_1 = 4*numpy.finfo(float).eps 
tol_2 = 4*numpy.finfo(float).eps 
tol_3 = 4*numpy.finfo(float).eps 
tol_4 = 4*numpy.finfo(float).eps 

class Root_in_t:
    def __init__(self,root,multiplicity):
        self.root = root
        self.multiplicity = multiplicity

class Root_in_z:
    def __init__(self,root,multiplicity):
        self.root = root
        self.multiplicity = multiplicity

def get_Denominator(z):
    # Two of the products do not depend on position indices, so calculate them first
    i = 0
    j = 0
    # Import the N-1 interacting data for each pair of position indices
    filename_Nminus1 = 'n_minus_one' + str(i) + '_' + str(j) + '.txt'
    my_path_Nminus1 = os.path.join('/Users/christinadaniel/Desktop/Christina_Desktop/data/w_interacting/'+filename_Nminus1)
    my_opened_file_Nminus1 = open(my_path_Nminus1,"r")
    my_data_Nminus1 = my_opened_file_Nminus1.readlines()
    # Import the N+1 interacting data for each pair of position indices
    filename_Nplus1 = 'n_plus_one' + str(i) + '_' + str(j) + '.txt'
    my_path_Nplus1 = os.path.join('/Users/christinadaniel/Desktop/Christina_Desktop/data/w_interacting/'+filename_Nplus1)
    my_opened_file_Nplus1 = open(my_path_Nplus1,"r")
    my_data_Nplus1 = my_opened_file_Nplus1.readlines()
    # For N-1
    Product_Over_alpha = 1.0
    # For N+1
    Product_Over_beta = 1.0
    # Parse the N-1 interacting data
    differences_for_a = []
    for line in my_data_Nminus1:
        contents = line.split()
        w_difference_for_Nminus1 = float(contents[0])
        Product_Over_alpha = Product_Over_alpha * (z - w_difference_for_Nminus1)
        differences_for_a.append(w_difference_for_Nminus1)
    # Parse the N+1 interacting data
    differences_for_b = []
    for line in my_data_Nplus1:
        contents = line.split()
        w_difference_for_Nplus1 = float(contents[0])
        Product_Over_beta = Product_Over_beta * (z - w_difference_for_Nplus1)
        differences_for_b.append(w_difference_for_Nplus1)
    number_of_a_eigenstates = len(my_data_Nminus1)
    number_of_b_eigenstates = len(my_data_Nplus1)



    sum_over_b = 0.0
    for b in range(number_of_b_eigenstates):
        product_over_beta_not_b = 1.0
        sum_over_ij_for_X_b = 0.0
        for i in range(V):
            for j in range(V):
                cosine_value = math.cos(K*(i-j))
                # Import the N+1 interacting data for each pair of position indices
                filename_Nplus1 = 'n_plus_one' + str(i) + '_' + str(j) + '.txt'
                my_path_Nplus1 = os.path.join('/Users/christinadaniel/Desktop/Christina_Desktop/data/w_interacting/'+filename_Nplus1)
                my_opened_file_Nplus1 = open(my_path_Nplus1,"r")
                my_data_Nplus1 = my_opened_file_Nplus1.readlines()
                # Collect the N+1 interacting data
                brackets_for_b = []
                for line in my_data_Nplus1:
                    contents = line.split()
                    product_of_Nplus1_brackets = float(contents[1])
                    brackets_for_b.append(product_of_Nplus1_brackets)
                sum_over_ij_for_X_b = sum_over_ij_for_X_b + cosine_value*brackets_for_b[b]
        for beta in range(number_of_b_eigenstates):
            if beta != b:
                product_over_beta_not_b = product_over_beta_not_b * (z - differences_for_b[beta])
        sum_over_b = sum_over_b + sum_over_ij_for_X_b * product_over_beta_not_b
    
    
    sum_over_a = 0.0
    for a in range(number_of_a_eigenstates):
        product_over_alpha_not_a = 1.0
        sum_over_ij_for_X_a = 0.0
        for i in range(V):
            for j in range(V):
                cosine_value = math.cos(K*(i-j))
                # Import the N-1 interacting data for each pair of position indices
                filename_Nminus1 = 'n_minus_one' + str(i) + '_' + str(j) + '.txt'
                my_path_Nminus1 = os.path.join('/Users/christinadaniel/Desktop/Christina_Desktop/data/w_interacting/'+filename_Nminus1)
                my_opened_file_Nminus1 = open(my_path_Nminus1,"r")
                my_data_Nminus1 = my_opened_file_Nminus1.readlines()
                # Collect the N-1 interacting data
                brackets_for_a = []
                for line in my_data_Nminus1:
                    contents = line.split()
                    product_of_Nminus1_brackets = float(contents[1])
                    brackets_for_a.append(product_of_Nminus1_brackets)
                sum_over_ij_for_X_a = sum_over_ij_for_X_a + cosine_value*brackets_for_a[a]
        
                # Collect the N-1 interacting data
                brackets_for_a = []
                differences_for_a = []
                for line in my_data_Nminus1:
                    contents = line.split()
                    w_difference_for_Nminus1 = float(contents[0])  
                    product_of_Nminus1_brackets = float(contents[1])
                    brackets_for_a.append(product_of_Nminus1_brackets)
                    differences_for_a.append(w_difference_for_Nminus1)
                sum_over_ij_for_X_a = sum_over_ij_for_X_a + cosine_value*brackets_for_a[a]
        for alpha in range(number_of_a_eigenstates):
            if alpha != a:
                product_over_alpha_not_a = product_over_alpha_not_a * (z - differences_for_a[alpha])        
        sum_over_a = sum_over_a + sum_over_ij_for_X_a * product_over_alpha_not_a
            

    Denominator = Product_Over_alpha*sum_over_b + Product_Over_beta*sum_over_a
    return sympy.expand(Denominator)

class Cheby_Poly:
    def __init__(self,expression_in_t): # constructor
        self.expression_in_t = expression_in_t # instance attribute
        self.b_vector = self.calculate_b_vector() # instance attribute
        self.degree = sympy.degree(expression_in_t) # instance attribute
    def calculate_b_vector(self): # method
        p_bar = self.expression_in_t
        n = 0
        if p_bar == 0:
            n = 0
        else:
            n = sympy.degree(p_bar)
        p_bar_numerical_evaluation = sympy.lambdify(t,p_bar)
        t_i_values = numpy.linspace(-1,1,num=(n+1),endpoint=True)
        absolute_values = numpy.absolute(p_bar_numerical_evaluation(t_i_values))
        max_value = 0
        if n==0:
            if p_bar == 0:
                max_value = 1
            else:
                max_value = float(self.expression_in_t)
        else:
            max_value = max(absolute_values)
        y_bar_i_values = [] # vector for scaled y_bar_i values
        tau = numpy.zeros( (n+1,n+1) ) # matrix for Chebyshev polynomials
        for i,t_i in enumerate(t_i_values):
            y_bar_i_values.append(p_bar_numerical_evaluation(t_i)/max_value)
            for j in range(n+1):
                tau[i][j] = numpy.cos( j * numpy.arccos(t_i) )
        calculated_b_vector = numpy.linalg.solve(tau,y_bar_i_values)  # Solve tau b = y
        if numpy.allclose(numpy.dot(tau,calculated_b_vector), y_bar_i_values) == False:
             raise Exception("There is an issue with the linear algebra.")
        return calculated_b_vector
    def evaluate_cheby_poly(self,t_value):
        sum = 0
        for j,b_j in enumerate(self.b_vector):
            sum = sum + b_j * numpy.cos( j * numpy.arccos( float(t_value) ) )
        return sum
        
class Poly_in_t:
    def __init__(self,expression,a,b): # constructor
        self.expression = expression
        self.a = a # from change of variables
        self.b = b # from change of variables
        self.degree = sympy.degree(expression)
        if self.degree >= 1:
            self.coeffs = numpy.flip(sympy.Poly(expression).all_coeffs())
        else:
            self.coeffs = expression
        if expression == 0:
            self.degree = 0
        self.root_objects = []
    def compute_symbolic_derivative_in_t(self): # method
        a = self.coeffs
        derivative_expression = 0
        for m in range(self.degree):
            derivative_expression = derivative_expression + a[m+1] * (m+1) * (t**m)
        return derivative_expression
    def convert_root_objects_from_t_to_z(self):
        z_root_objects = []
        for index,object in enumerate(self.root_objects):
            z_root = self.a + ((object.root+1)*(self.b-self.a)/2)
            z_root_object = Root_in_z(z_root,object.multiplicity)
            z_root_objects.append(z_root_object)
        return z_root_objects
        
def Brent(my_cheby_poly):
    t_roots = []
    start = -1.0
    stop = 1.0
    step = 1.0/5
    C = stop - step
    D = stop
    while ( C >= start ):
        if my_cheby_poly.evaluate_cheby_poly(C)*my_cheby_poly.evaluate_cheby_poly(D) < 0:
            sol = optimize.brenth(my_cheby_poly.evaluate_cheby_poly,C,D)
            if abs(my_cheby_poly.evaluate_cheby_poly(sol)) < tol_1:
                t_roots.append(sol)
        C = C - step
        D = D - step
    if abs(my_cheby_poly.evaluate_cheby_poly(start)) < tol_1:
        t_roots.append(start)
    if abs(my_cheby_poly.evaluate_cheby_poly(stop)) < tol_1:
        t_roots.append(stop)
    return t_roots
    
def Brent_for_derivative(my_cheby_poly,my_cheby_poly_derivative):
    t_roots = []
    start = -1.0
    stop = 1.0
    step = 1.0/5
    C = stop - step
    D = stop
    while ( C >= start ):
        if my_cheby_poly_derivative.evaluate_cheby_poly(C)*my_cheby_poly_derivative.evaluate_cheby_poly(D) < 0:
            sol = optimize.brenth(my_cheby_poly_derivative.evaluate_cheby_poly,C,D)
            if abs( my_cheby_poly.evaluate_cheby_poly(sol) ) < tol_2:
                t_roots.append(sol)
        C = C - step
        D = D - step
    return t_roots

class Multiplicity_Computation:
    def __init__(self,f,f_prime,root):
        self.f = f
        self.f_prime = f_prime 
        self.root = root
        self.f_numerical = sympy.lambdify(t,f)
        self.f_prime_numerical = sympy.lambdify(t,f_prime)
    def vertical_value(self,horizontal_value):
        return ( 1.0/self.f_numerical(horizontal_value) ) * self.f_numerical(horizontal_value)
    def plot_limits(self,title):
        for number in range(10):
            left = self.root - (number+1)*tol_3
            right = self.root + (number+1)*tol_3 
            plt.scatter(left,self.vertical_value(left),color='blue')
            plt.scatter(right,self.vertical_value(right),color='red')
        plt.title(title)
        plt.show()
    def left_limit(self):
        far_left = self.root - 10*tol_3
        return self.vertical_value(far_left) 
    def right_limit(self):
        far_right = self.root + 10*tol_3
        return self.vertical_value(far_right)
    def limit(self):
        if abs( self.left_limit() - self.right_limit() ) > tol_4:
            print("LIMITS:",self.left_limit(),self.right_limit())
            raise Exception("The left limit does not equal the right limit.")
        else:
            return self.left_limit()
    
def find_denominator_roots(a_min,b_max,step):
    
    step = (b_max - a_min)/step
    
    a = a_min
    b = a_min + step
    
    all_root_objects = []
    while ( b <= b_max ):
        
        z_in_terms_of_t = a + ((t+1)*(b-a)/2) 
        
        pbar_in_t = Poly_in_t(get_Denominator(z_in_terms_of_t),a,b)
        pbar_prime_in_t = Poly_in_t(pbar_in_t.compute_symbolic_derivative_in_t(),a,b)
        pbar_in_cheby = Cheby_Poly(pbar_in_t.expression)
        
        if pbar_in_t.degree >= 2:
            pbar_double_prime_in_t = Poly_in_t(pbar_prime_in_t.compute_symbolic_derivative_in_t(),a,b)
            
            pbar_prime_in_cheby = Cheby_Poly(pbar_prime_in_t.expression)
        
            # Original Polynomial
            
            t_roots_original = Brent(pbar_in_cheby)
            
            valid_t_roots_original = []
            for index,root in enumerate(t_roots_original):
                multiplicity_object = Multiplicity_Computation(pbar_in_t.expression,pbar_prime_in_t.expression,root)
                multiplicity_value = multiplicity_object.limit()
                if multiplicity_value != 0:
                    root_object = Root_in_t(root,multiplicity_value)
                    valid_t_roots_original.append(root_object) 
            
            pbar_in_t.root_objects = valid_t_roots_original # update instance attribute
            
            # Derivative Polynomial
            
            t_roots_derivative = Brent_for_derivative(pbar_in_cheby,pbar_prime_in_cheby) 
            
            valid_t_roots_derivative = []
            for index,root in enumerate(t_roots_derivative):
                multiplicity_object = Multiplicity_Computation(pbar_prime_in_t.expression,pbar_double_prime_in_t.expression,root)
                multiplicity_value = multiplicity_object.limit() + 1 # need to add 1 for the derivative case
                if multiplicity_value != 0:
                    root_object = Root_in_t(root,multiplicity_value)
                    valid_t_roots_derivative.append(root_object) 
                
            pbar_prime_in_t.root_objects = valid_t_roots_derivative # update instance attribute
            
            # Convert roots to the z-domain
            
            for index,object in enumerate(pbar_in_t.convert_root_objects_from_t_to_z()):
                all_root_objects.append(object)
            
            for index,object in enumerate(pbar_prime_in_t.convert_root_objects_from_t_to_z()):
                all_root_objects.append(object)
            
        else:
            t_roots_original = Brent(pbar_in_cheby)
            
            valid_t_roots_original = []
            for index,root in enumerate(t_roots_original):
                multiplicity_object = Multiplicity_Computation(pbar_in_t.expression,pbar_prime_in_t.expression,root)
                multiplicity_value = multiplicity_object.limit()
                if multiplicity_value != 0:
                    root_object = Root_in_t(root,multiplicity_value)
                    valid_t_roots_original.append(root_object) 
            
            pbar_in_t.root_objects = valid_t_roots_original # update instance attribute
            
            for index,object in enumerate(pbar_in_t.convert_root_objects_from_t_to_z()):
                all_root_objects.append(object)
        
        
        a = a + step
        b = b + step
    
    number_of_roots = 0
    for index,object in enumerate(all_root_objects):
        print("root in z-domain:",object.root)
        print("multiplicity of root:",round(object.multiplicity))
        number_of_roots = number_of_roots + object.multiplicity
    print("total number of roots including multiplicity:",number_of_roots)
    
    return all_root_objects
    

def get_numerator_roots():
    roots = []
    # Two of the products do not depend on position indices, so calculate them first
    i = 0
    j = 0
    # Import the N-1 interacting data for each pair of position indices
    filename_Nminus1 = 'n_minus_one' + str(i) + '_' + str(j) + '.txt'
    my_path_Nminus1 = os.path.join('/Users/christinadaniel/Desktop/Christina_Desktop/data/w_interacting/'+filename_Nminus1)
    my_opened_file_Nminus1 = open(my_path_Nminus1,"r")
    my_data_Nminus1 = my_opened_file_Nminus1.readlines()
    # Import the N+1 interacting data for each pair of position indices
    filename_Nplus1 = 'n_plus_one' + str(i) + '_' + str(j) + '.txt'
    my_path_Nplus1 = os.path.join('/Users/christinadaniel/Desktop/Christina_Desktop/data/w_interacting/'+filename_Nplus1)
    my_opened_file_Nplus1 = open(my_path_Nplus1,"r")
    my_data_Nplus1 = my_opened_file_Nplus1.readlines()
    # Parse the N-1 interacting data
    for line in my_data_Nminus1:
        contents = line.split()
        w_difference_for_Nminus1 = float(contents[0])
        roots.append(w_difference_for_Nminus1)
    # Parse the N+1 interacting data
    for line in my_data_Nplus1:
        contents = line.split()
        w_difference_for_Nplus1 = float(contents[0])
        roots.append(w_difference_for_Nplus1)
    return roots


