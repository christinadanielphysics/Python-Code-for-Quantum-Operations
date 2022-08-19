import system
import hubbard

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

connected_ends = True # geometry of molecule

sites = int(input("Number of sites? "))
up_electrons = int(input("Number of up-spin electrons? "))
down_electrons = int(input("Number of down-spin electrons? "))
U_value = float(input("Value of U for Hubbard Hamiltonain operator? "))
t_value = float(input("Value of t for Hubbard Hamiltonian operator? "))

my_system = system.System(sites,up_electrons,down_electrons,connected_ends)
my_hubbard = hubbard.Hubbard(U_value,t_value,my_system)

my_hubbard.write_eigenvalues_and_eigenvectors(my_latex_file)

my_latex_file.close_latex_file()

 
 



