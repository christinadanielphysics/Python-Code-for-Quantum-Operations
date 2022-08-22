import system
import lesser_green
import greater_green
import numpy
import discrete_cosine_transform
import matplotlib.pyplot as plt
import compressive_sensing
import export
import root_finding
import weights


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
    

# my_latex_file = Latex_File("main.tex")
# my_latex_file.setup_latex_file()

U_value = 1
t_value = 1

connected_ends = True # geometry of molecule
sites = root_finding.V
up_electrons = 1
down_electrons = 1

system_with_n_electrons = system.System(sites,up_electrons,down_electrons,connected_ends)

number_of_samples = 2**8
number_of_random_samples = 2**8
start_time = 0
stop_time = 3
time_values = numpy.linspace(start_time,stop_time,num=number_of_samples,endpoint=True,retstep=False)
threshold = 0

directory = "/Users/christinadaniel/Desktop/Christina_Desktop/data/w_interacting/"


for i in range(sites):
    for j in range(sites):
        my_lesser = lesser_green.Lesser_Green("up",i,j,system_with_n_electrons,U_value,t_value)
        
        lesser_angular_frequencies,lesser_weights = my_lesser.get_angular_frequencies_and_weights()
        lesser_time_version = my_lesser.get_time_version(time_values)
        
        lesser_compressive_object = compressive_sensing.Compressive_Sensing(start_time,stop_time,number_of_samples,lesser_time_version,threshold,"lesser")
        lesser_compressive, lesser_compressive_angular_frequency_values = lesser_compressive_object.get_transformed_signal(number_of_random_samples)
        
        lesser_export_object = export.Export("n_minus_one"+str(i)+"_"+str(j)+".txt",directory)
        lesser_export_object.export(lesser_angular_frequencies,lesser_weights,threshold)
        
        # lesser_dct_object = discrete_cosine_transform.Discrete_Cosine_Transform(start_time,stop_time,number_of_samples,lesser_time_version)
        # lesser_dct = lesser_dct_object.get_dct()
        # lesser_dct_angular_frequencies  = lesser_dct_object.get_angular_frequency_values()
        
        plt.figure(i)
        plt.plot(time_values,lesser_time_version,c='crimson',linewidth=3)
        plt.show()
        
        plt.figure(i)
        plt.scatter(lesser_compressive_angular_frequency_values,lesser_compressive,c='orange',s=500)
        plt.scatter(lesser_angular_frequencies,lesser_weights,c='green',s=100)
        #plt.plot(lesser_dct_angular_frequencies * (-1),lesser_dct,c='black')
        plt.show()



for i in range(sites):
    for j in range(sites):
        my_greater = greater_green.Greater_Green("up",i,j,system_with_n_electrons,U_value,t_value) 
        
        greater_angular_frequencies,greater_weights = my_greater.get_angular_frequencies_and_weights()
        greater_time_version = my_greater.get_time_version(time_values)
        
        greater_compressive_object = compressive_sensing.Compressive_Sensing(start_time,stop_time,number_of_samples,greater_time_version,threshold,"greater")
        greater_compressive, greater_compressive_angular_frequency_values = greater_compressive_object.get_transformed_signal(number_of_random_samples)
        
        greater_export_object = export.Export("n_plus_one"+str(i)+"_"+str(j)+".txt",directory)
        greater_export_object.export(greater_angular_frequencies,greater_weights,threshold)
        
        # greater_dct_object = discrete_cosine_transform.Discrete_Cosine_Transform(start_time,stop_time,number_of_samples,greater_time_version)
        # greater_dct = greater_dct_object.get_dct()
        # greater_dct_angular_frequencies  = greater_dct_object.get_angular_frequency_values()
        
        plt.figure(i)
        plt.plot(time_values,greater_time_version,c='orange',linewidth=3)
        plt.show()
        
        plt.figure(i)
        plt.scatter(greater_compressive_angular_frequency_values,greater_compressive,c='red',s=500)
        plt.scatter(greater_angular_frequencies,greater_weights,c='blue',s=100)
        #plt.plot(greater_dct_angular_frequencies,greater_dct,c='black')
        plt.show()
        

a_value = -7
b_value = 11
step = 3
expected_denominator_roots = root_finding.find_denominator_roots(a_value,b_value,step)
expected_numerator_roots = root_finding.get_numerator_roots()

denominator_filename = "expected_denominator_roots.txt"
denominator_root_file = export.Export(denominator_filename,directory)
denominator_root_file.export_denominator_roots(expected_denominator_roots)

numerator_filename = "expected_numerator_roots.txt"
numerator_root_file = export.Export(numerator_filename,directory)
numerator_root_file.export_numerator_roots(expected_numerator_roots)

object_for_weights = weights.Weights(directory,denominator_filename,numerator_filename)
the_roots, the_weights = object_for_weights.get_roots_and_weights()

plt.figure(1)
plt.scatter(the_roots,the_weights)
plt.show()

print("the roots:\n",the_roots)
print("the weights:\n",the_weights)

# my_latex_file.close_latex_file()

 
 



