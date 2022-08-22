import sympy
import os

class Weights:
    def __init__(self,filepath,denominator_filename,numerator_filename):
        self.filepath = filepath
        self.denominator_filename = denominator_filename
        self.numerator_filename = numerator_filename
    def import_denominator_roots(self):
        joined_file = os.path.join(self.filepath+self.denominator_filename)
        opened_file = open(joined_file,'r')
        data_file = opened_file.readlines()
        roots = []
        multiplicities = []
        for line in data_file:
            contents = line.split()
            root = float(contents[0])
            multiplicity = float(contents[1])
            roots.append(root)
            multiplicities.append(multiplicity)
        return roots,multiplicities
    def import_numerator_roots(self):
        joined_file = os.path.join(self.filepath+self.numerator_filename)
        opened_file = open(joined_file,'r')
        data_file = opened_file.readlines()
        roots = []
        multiplicities = []
        for line in data_file:
            contents = line.split()
            root = float(contents[0])
            multiplicity = float(contents[1])
            roots.append(root)
            multiplicities.append(multiplicity)
        return roots,multiplicities
    def form_factored_denominator(self):
        x = sympy.Symbol('x')
        roots,multiplicities = self.import_denominator_roots()
        denominator = 1
        for index,root in enumerate(roots):
            for multiplicity in range(int(multiplicities[index])):
                denominator = denominator * (x - root)
        return denominator
    def form_factored_numerator(self):
        x = sympy.Symbol('x')
        roots,multiplicities = self.import_numerator_roots()
        numerator = 1 
        for index,root in enumerate(roots):
            for multiplicity in range(int(multiplicities[index])):
                numerator = numerator * (x - root)
        return numerator
    def form_factored_expression(self):
        print(self.form_factored_numerator()/self.form_factored_denominator())
        return self.form_factored_numerator()/self.form_factored_denominator()
    def get_roots_and_weights(self):
        x = sympy.Symbol('x')
        roots,multiplicities = self.import_denominator_roots()
        old_expression = self.form_factored_expression()
        weights = []
        for index,root in enumerate(roots):
            new_expression = old_expression
            for multiplicity in range(int(multiplicities[index])):
                new_expression = new_expression * (x - root)
                new_expression_numerical = sympy.lambdify(x,new_expression)
                weight = new_expression_numerical(root)
                print(weight)
                weights.append(weight)
        return roots,weights
            
        
    





    