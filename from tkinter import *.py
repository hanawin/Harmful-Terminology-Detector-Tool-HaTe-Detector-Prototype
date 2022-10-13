from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Harmful Terms Detection and Correction')
root.geometry("500x450")


#class openReplace:
def open_txt():
    text_file = filedialog.askopenfilename(initialdir="stevewinchester", title="Open Text File", filetypes=(("Text Files", "*.txt"),))
    text_file  = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()
    #stuff = text_file.read()
    #stuff3 = stuff
    #return stuff3

#def readStuff():
  #  open_txt()
   # stuff2 = text_file.var
    #stuff2 = text_file.read()
    #stuff = open_txt()
    #stuff.read()
  #  return stuff

#def insertStuff():
  #  my_text.insert(END, stuff)
    #text_file.close()
  #  def returnStuff():
      #  return stuff

def replace_terms():

    text_file = open('sample.txt', 'r')
    stuff = text_file.read()
        
    stuff_split = stuff.split()
    replacements = ['cancel', 'cancel', 'standard', 'opaque box', 'open box', 'ethical attacker', 'unethical attacker', 'blocklist', 'allowlist', 'anonymous', 'dual anonymous', 'anonymous review', 'socket', 'plug', 'they', 'them', 'their', 'they', 'them', 'their', 'main', 'secondary', 'advantage', 'legacy status', 'people', 'person hours', 'confidence check', 'placeholder value', 'Agile lead', 'ensemble', 'ensemble programming', 'separation of network', 'separation of duty','downtime', 'hacktivist', 'built-in', 'built-in feature', 'cyber offense', 'web product owner', 'empty space', 'cyber exercise cell', 'DevSecOps team', 'Tech Talks', 'person-in-the-middle', 'main branch', 'sample']
    harmfulTerms = ['abort', 'terminate', 'average', 'black box', 'white box', 'blackhat', 'whitehat', 'blacklist', 'whitelist', 'blind', 'double blind', 'blind review', 'female connectors', 'male connectors', 'she', 'her', 'hers', 'he', 'him', 'his', 'master', 'slave', 'quantum supremacy', 'grandfather', 'grandfathered', 'guys', 'man hours', 'sanity check', 'dummy value', 'scrum master', 'mob', 'mob programming', 'segregation of network', 'segregation of duty', 'blackout period', 'gray hat', 'native', 'native feature', 'red team', 'web master', 'whitespace', 'white team', 'yellow team', 'aboriginal', 'brown bags', 'cakewalk', 'first-class citizen', 'man-in-the-middle', 'master branch']
    
    array_length = len(stuff_split)
    array_length2 = len(harmfulTerms)
    for i in range(array_length):
        istr = stuff_split[i]
        for j in range(array_length2):
            
            jstr = harmfulTerms[j]
            if istr == jstr:
                stuff_split[i] = replacements[j]
               # stuff_split[i].replace(stuff_split[i], replacements[j])
    my_text.delete("1.0", "end")
    my_text.insert(END, stuff_split)
        
#OR = openReplace()

def save_txt():
    text_file = filedialog.askopenfilename(initialdir="stevewinchester", title="Open Text File", filetypes=(("Text Files", "*.txt"),))
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))

my_text = Text(root, width=40, height=10, font=("Helvetica", 16))
my_text.pack(pady=20)




#open file button
open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=20)

#replace terms button
replace_button = Button(root, text="Replace Terms", command=replace_terms)
replace_button.pack(pady=20)

#save button
save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=20)


root.mainloop()