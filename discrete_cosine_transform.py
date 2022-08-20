import scipy.fftpack as fft_from_scipy
import numpy
import math

class Discrete_Cosine_Transform:
    def __init__(self,start_time,stop_time,number_of_samples):
        self.start_time = start_time 
        self.stop_time = stop_time 
        self.number_of_samples = number_of_samples 
        self.number_of_time_units = self.stop_time - self.start_time
        self.samples_per_time_unit = self.number_of_samples/self.number_of_time_units
    def get_frequency_values(self):
        stop_value = self.samples_per_time_unit/2
        frequency_values = numpy.linspace(start=0,stop=stop_value,num=self.number_of_samples,endpoint=True,retstep=False)
        return frequency_values
    def get_angular_frequency_values(self):
        stop_value = 2 * math.pi * (self.samples_per_time_unit/2)
        angular_frequency_values = numpy.linspace(start=0,stop=stop_value,num=self.number_of_samples,endpoint=True,retstep=False)
        return angular_frequency_values
    def get_dct(self,signal_in_time):
        return fft_from_scipy.dct(signal_in_time)