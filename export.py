import os

class Export:
    filepath = "/Users/christinadaniel/Desktop/Christina_Desktop/data/w_interacting/"
    def __init__(self,filename):
        self.filename = filename
    def export(self,angular_frequencies,weights):
        my_path = os.path.join(Export.filepath+self.filename)
        opened_file = open(my_path,"w")
        for index,value in enumerate(angular_frequencies):
            opened_file.write(str(value)+" "+str(weights[index])+"\n")
        opened_file.close()