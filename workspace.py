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
    f.write("\n")
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
        write_c_dagger(creation_operator.Creation_Operator(number,"up"))
            
def write_down_operators_of_state(f,state):
    for index,number in enumerate(state.down_spin_list):
        write_c_dagger(creation_operator.Creation_Operator(number,"down"))
    
def write_equal_sign():
    f.write("=")
    
def write_equation_with_c_applied(f,c_operator,state,result):
    start_latex_equation(f)
    write_coefficient_of_state(f,state)
    write_c(c_operator)
    write_up_operators_of_state(f,state)
    write_down_operators_of_state(f,state)
    write_vacuum_state(f)
    write_equal_sign()
    write_coefficient_of_state(f,result)
    write_up_operators_of_state(f,result)
    write_down_operators_of_state(f,result)
    write_vacuum_state(f)
    end_latex_equation(f)

def write_equation_with_c_dagger_applied(f,c_dagger_operator,state,result):
    start_latex_equation(f)
    write_coefficient_of_state(f,state)
    write_c_dagger(c_dagger_operator)
    write_up_operators_of_state(f,state)
    write_down_operators_of_state(f,state)
    write_vacuum_state(f)
    write_equal_sign()
    write_coefficient_of_state(f,result)
    write_up_operators_of_state(f,result)
    write_down_operators_of_state(f,result)
    write_vacuum_state(f)
    end_latex_equation(f)
    


directory_to_latex_file = "/Users/christinadaniel/Desktop/Christina_Desktop/latex_files/"
latex_filename = "main.tex"
f = open(directory_to_latex_file+latex_filename, "w")
setup_latex_file(f)



# c operator
c_0_up = annihilation_operator.Annihilation_Operator(0,"down")

# state
coefficient_1 = 1
up_spin_list_1 = [0]
down_spin_list_1 = [0]
state_1 = occupation_state.Occupation_State(coefficient_1,up_spin_list_1,down_spin_list_1)

# result
result_1 = c_0_up.apply(state_1)

write_equation_with_c_applied(f,c_0_up,state_1,result_1)

# c-dagger operator
c_dagger_0_up = creation_operator.Creation_Operator(3,"down")

# result
result_2 = c_dagger_0_up.apply(state_1)

#write_equation_with_c_dagger_applied(f,c_dagger_0_up,state_1,result_2)





close_latex_file(f)

 
 



