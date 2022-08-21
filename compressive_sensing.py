import numpy
import math
import scipy 
import random 
import cvxpy as cvx 
import sys
import os

class Compressive_Sensing:
    def __init__(self,start_time,stop_time,number_of_samples,x_values,threshold,type):
        self.start_time = start_time 
        self.stop_time = stop_time 
        self.number_of_samples = number_of_samples 
        self.number_of_time_units = self.stop_time - self.start_time
        self.samples_per_time_unit = self.number_of_samples/self.number_of_time_units
        self.t_values = numpy.linspace(self.start_time,self.stop_time,num=self.number_of_samples,endpoint=True,retstep=False)
        self.x_values = numpy.array(x_values)
        self.threshold = threshold
        self.type = type
    def get_frequency_values(self):
        stop_value = self.samples_per_time_unit/2
        frequency_values = numpy.linspace(start=0,stop=stop_value,num=self.number_of_samples,endpoint=True,retstep=False)
        if self.type == "lesser":
            for index,value in enumerate(frequency_values):
                frequency_values[index] = frequency_values[index] * (-1)
        return frequency_values
    def get_angular_frequency_values(self):
        stop_value = 2 * math.pi * (self.samples_per_time_unit/2)
        angular_frequency_values = numpy.linspace(start=0,stop=stop_value,num=self.number_of_samples,endpoint=True,retstep=False)
        if self.type == "lesser":
            for index,value in enumerate(angular_frequency_values):
                angular_frequency_values[index] = angular_frequency_values[index] * (-1)
        return angular_frequency_values
    def get_transformed_signal(self,number_of_random_samples):
        
        random_indices = numpy.zeros(number_of_random_samples)
        for i,element in enumerate(random_indices):
            random_indices[i] = round( random.uniform(0,1) * (self.number_of_samples-1) )
        random_indices = random_indices.astype(numpy.int32)
        
        y_values = self.x_values[random_indices] # compressed measurement
        t_values_for_y = self.t_values[random_indices]
        
        identity_matrix = numpy.identity(self.number_of_samples) # Identity Matrix
        Psi = scipy.fft.dct(identity_matrix) # Build Psi
        Theta = Psi[random_indices,:] # Measure rows of Psi
        
        # Compressed Sensing with L1 Minimization
        s = cvx.Variable(self.number_of_samples) # Create a variable called s
        objective = cvx.Minimize(cvx.norm(s,1)) # Minimize the L1 norm of s.
        constraint = [Theta@s == y_values] # Define the constraint according to a matrix equation.
        prob = cvx.Problem(objective,constraint) # Define the problem according to the objective and the constraint.
        result = prob.solve(verbose=False) # Solve the problem
        
        # Reconstruct the full signal
        x_reconstructed = scipy.fft.dct(s.value)
        
        edited_result = []
        edited_angular_frequencies = []
        original_angular_frequencies = self.get_angular_frequency_values()
        for index,value in enumerate(s.value):
            if abs(value) > self.threshold:
                edited_result.append(value*2)
                edited_angular_frequencies.append(original_angular_frequencies[index])
            
        
        return edited_result,edited_angular_frequencies