import system
import lesser_green
import greater_green
import numpy
import discrete_cosine_transform
import math
import matplotlib.pyplot as plt
import compressive_sensing


class Latex_File:
    directory_to_latex_file = "/Users/christinadaniel/Desktop/Christina_Desktop/latex_files/"
    def __init__(self,filename):
        self.filename = filename
        self.f = open(Latex_File.directory_to_latex_file+self.filename, "w")
    def setup_latex_file(self):
        self.f.write(r"\documentclass{article}")
        self.f.write("\n")
        self.f.write(r"\usepackage[english]{babel}")
        self.f.write("\n")
        self.f.write(r"\usepackage[letterpaper,top=2cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}")
        self.f.write("\n")
        self.f.write(r"\usepackage{amsmath}")
        self.f.write("\n")
        self.f.write(r"\usepackage{physics}")
        self.f.write("\n")
        self.f.write(r"\usepackage{graphicx}")
        self.f.write("\n")
        self.f.write(r"\usepackage[colorlinks=true, allcolors=blue]{hyperref}")
        self.f.write("\n")
        self.f.write(r"\title{Your Paper}")
        self.f.write("\n")
        self.f.write(r"\author{You}")
        self.f.write("\n")
        self.f.write(r"\begin{document}")
        self.f.write("\n")
        self.f.write(r"\maketitle")
        self.f.write("\n")
        self.f.write(r"\section{Output}")
        self.f.write("\n")
    def close_latex_file(self):
        self.f.write("\n")
        self.f.write("\end{document}")
        self.f.close()
    def start_latex_equation(self):
        self.f.write("\n")
        self.f.write(r"\begin{equation*}")
        self.f.write("\n")  
    def end_latex_equation(self):
        self.f.write("\n")
        self.f.write(r"\end{equation*}")
    def write_equal_sign(self):
        self.f.write("=")
    

my_latex_file = Latex_File("main.tex")
my_latex_file.setup_latex_file()

U_value = float(input("Value of U for Hubbard Hamiltonain operator? "))
t_value = float(input("Value of t for Hubbard Hamiltonian operator? "))

connected_ends = True # geometry of molecule
sites = int(input("Number of sites? "))
up_electrons = int(input("Number of up-spin electrons? "))
down_electrons = int(input("Number of down-spin electrons? "))

system_with_n_electrons = system.System(sites,up_electrons,down_electrons,connected_ends)

# i = 0
# j = 0

# my_lesser = lesser_green.Lesser_Green("up",i,j,system_with_n_electrons,U_value,t_value)
# my_greater = greater_green.Greater_Green("up",i,j,system_with_n_electrons,U_value,t_value) 

# lesser_angular_frequencies,lesser_weights = my_lesser.get_angular_frequencies_and_weights()
# greater_angular_frequencies,greater_weights = my_greater.get_angular_frequencies_and_weights()

# lesser_time_version = my_lesser.get_time_version(time_values)
# greater_time_version = my_greater.get_time_version(time_values)

number_of_samples = 2**8
start_time = 0
stop_time = 5
dct_object = discrete_cosine_transform.Discrete_Cosine_Transform(start_time,stop_time,number_of_samples)
time_values,time_step = numpy.linspace(start_time,stop_time,num=number_of_samples,endpoint=False,retstep=True)
sample_signal = numpy.cos(time_values*2*math.pi*3) + numpy.cos(time_values*2*math.pi*7)
frequency_values = dct_object.get_frequency_values()
number_of_random_samples = number_of_samples
compressive_object = compressive_sensing.Compressive_Sensing(start_time,stop_time,number_of_samples,sample_signal)
compressive_frequency_values = compressive_object.get_frequency_values()
plt.figure(1)
plt.plot(frequency_values,dct_object.get_dct(sample_signal),c='black',linewidth=10)
plt.plot(compressive_frequency_values,compressive_object.get_transformed_signal(number_of_random_samples),c='red',linewidth=2)
plt.show()



my_latex_file.close_latex_file()

 
 



