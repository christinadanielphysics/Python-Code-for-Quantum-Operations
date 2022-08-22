import os

class Export:
    def __init__(self,filename,filepath):
        self.filename = filename
        self.filepath = filepath
    def export(self,angular_frequencies,weights,threshold):
        my_path = os.path.join(self.filepath+self.filename)
        opened_file = open(my_path,"w")
        for index,value in enumerate(angular_frequencies):
            if abs(weights[index]) > threshold:
                opened_file.write(str(value)+" "+str(weights[index])+"\n")
            else:
                print("small weight!",weights[index])
        opened_file.close()
    def export_denominator_roots(self,root_objects):
        my_path = os.path.join(self.filepath+self.filename)
        opened_file = open(my_path,"w")
        for index,root_object in enumerate(root_objects):
            opened_file.write(str(root_object.root)+" "+str(root_object.multiplicity)+"\n")
        opened_file.close()
    def export_numerator_roots(self,root_list):
        my_path = os.path.join(self.filepath+self.filename)
        opened_file = open(my_path,'w')
        for index,root in enumerate(root_list):
            opened_file.write(str(root)+" "+str(1)+"\n")
        opened_file.close()
           
        
        