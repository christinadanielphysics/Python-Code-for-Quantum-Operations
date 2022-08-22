import system
import lesser_green
import greater_green
import numpy
import discrete_cosine_transform
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

number_of_samples = 2**7
number_of_random_samples = number_of_samples
start_time = 0
stop_time = 50
time_values = numpy.linspace(start_time,stop_time,num=number_of_samples,endpoint=True,retstep=False)

i = 0
j = 0
my_lesser = lesser_green.Lesser_Green("up",i,j,system_with_n_electrons,U_value,t_value)
my_greater = greater_green.Greater_Green("up",i,j,system_with_n_electrons,U_value,t_value) 
lesser_angular_frequencies,lesser_weights = my_lesser.get_angular_frequencies_and_weights()
greater_angular_frequencies,greater_weights = my_greater.get_angular_frequencies_and_weights()
lesser_time_version = my_lesser.get_time_version(time_values)
greater_time_version = my_greater.get_time_version(time_values)




threshold = 0

greater_compressive_object = compressive_sensing.Compressive_Sensing(start_time,stop_time,number_of_samples,greater_time_version,threshold,"greater")
greater_compressive, greater_compressive_angular_frequency_values = greater_compressive_object.get_transformed_signal(number_of_random_samples)

lesser_compressive_object = compressive_sensing.Compressive_Sensing(start_time,stop_time,number_of_samples,lesser_time_version,threshold,"lesser")
lesser_compressive, lesser_compressive_angular_frequency_values = lesser_compressive_object.get_transformed_signal(number_of_random_samples)

greater_dct_object = discrete_cosine_transform.Discrete_Cosine_Transform(start_time,stop_time,number_of_samples,greater_time_version)
greater_dct = greater_dct_object.get_dct()
greater_dct_angular_frequencies  = greater_dct_object.get_angular_frequency_values()

lesser_dct_object = discrete_cosine_transform.Discrete_Cosine_Transform(start_time,stop_time,number_of_samples,lesser_time_version)
lesser_dct = lesser_dct_object.get_dct()
lesser_dct_angular_frequencies  = lesser_dct_object.get_angular_frequency_values()

plt.figure(1)
plt.plot(time_values,greater_time_version,c='orange',linewidth=3)
plt.plot(time_values,lesser_time_version,c='crimson',linewidth=3)
plt.show()


plt.figure(2)
plt.scatter(greater_compressive_angular_frequency_values,greater_compressive,c='red',s=500)
plt.scatter(greater_angular_frequencies,greater_weights,c='blue',s=100)
plt.scatter(lesser_compressive_angular_frequency_values,lesser_compressive,c='orange',s=500)
plt.scatter(lesser_angular_frequencies,lesser_weights,c='green',s=100)
plt.plot(lesser_dct_angular_frequencies * (-1),lesser_dct,c='black')
plt.plot(greater_dct_angular_frequencies,greater_dct,c='black')
plt.show()


my_latex_file.close_latex_file()

 
 



