import occupation_state
import annihilation_operator 
import creation_operator


def setup_latex_file(f):
    f.write(r"\documentclass{article}")
    f.write("\n")
    f.write(r"\usepackage[english]{babel}")
    f.write("\n")
    f.write(r"\usepackage[letterpaper,top=2cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}")
    f.write("\n")
    f.write(r"\usepackage{amsmath}")
    f.write("\n")
    f.write(r"\usepackage{physics}")
    f.write("\n")
    f.write(r"\usepackage{graphicx}")
    f.write("\n")
    f.write(r"\usepackage[colorlinks=true, allcolors=blue]{hyperref}")
    f.write("\n")
    f.write(r"\title{Your Paper}")
    f.write("\n")
    f.write(r"\author{You}")
    f.write("\n")
    f.write(r"\begin{document}")
    f.write("\n")
    f.write(r"\maketitle")
    f.write("\n")
    f.write(r"\section{Output}")
    f.write("\n")

def close_latex_file(f):
    f.write("\n")
    f.write("\end{document}")
    f.close()

def start_latex_equation(f):
    f.write(r"\begin{equation*}")
    f.write("\n")
    
def end_latex_equation(f):
    f.write("\n")
    f.write(r"\end{equation*}")
    
def write_coefficient_of_state(f,state):
    f.write(str(state.coefficient))

def write_vacuum_state(f):
    f.write("\ket{0}")
    
def write_c_dagger(op):
    spin_symbol = 0
    if op.spin == "up":
        spin_symbol = r"\uparrow"
    else:
        spin_symbol = r"\downarrow"
    f.write("\hat{c}^\dag_{"+str(op.numerical_index)+spin_symbol+"}")

def write_c(op):
    spin_symbol = 0
    if op.spin == "up":
        spin_symbol = r"\uparrow"
    else:
        spin_symbol = r"\downarrow"
    f.write("\hat{c}_{"+str(op.numerical_index)+spin_symbol+"}")
    
def write_up_operators_of_state(f,state):
    for index,number in enumerate(state.up_spin_list):
        f.write(creation_operator.Creation_Operator(number,"up"))
        
    
def write_down_operators_of_state(f,state):
    for index,number in enumerate(state.down_spin_list):
        f.write(creation_operator.Creation_Operator(number,"down"))


    
def write_equal_sign():
    f.write("=")


directory_to_latex_file = "/Users/christinadaniel/Desktop/Christina_Desktop/latex_files/"
latex_filename = "main.tex"
f = open(directory_to_latex_file+latex_filename, "w")
setup_latex_file(f)

# operator
c_0_up = annihilation_operator.Annihilation_Operator(0,"up")

# state
coefficient_1 = 1
up_spin_list_1 = []
down_spin_list_1 = []
state_1 = occupation_state.Occupation_State(coefficient_1,up_spin_list_1,down_spin_list_1)

# result
result_1 = c_0_up.apply(state_1)
# print(result_1.coefficient)
# print(result_1.up_spin_list)
# print(result_1.down_spin_list)

start_latex_equation(f)



write_coefficient_of_state(f,state_1)

write_c(c_0_up)

write_up_operators_of_state(f,state_1)
write_down_operators_of_state(f,state_1)

write_vacuum_state(f)

write_equal_sign()

write_coefficient_of_state(f,result_1)

write_up_operators_of_state(f,result_1)
write_down_operators_of_state(f,result_1)
write_vacuum_state(f)

end_latex_equation(f)



close_latex_file(f)

 
 



