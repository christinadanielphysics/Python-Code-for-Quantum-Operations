import system
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




directory_to_latex_file = "/Users/christinadaniel/Desktop/Christina_Desktop/latex_files/"
latex_filename = "main.tex"
f = open(directory_to_latex_file+latex_filename, "w")
setup_latex_file(f)

# DO STUFF
f.write("hiiiiiiii")

close_latex_file(f)

 
 



