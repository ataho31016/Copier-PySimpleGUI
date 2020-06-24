import PySimpleGUI as sg
import os, pathlib
import shutil
 

sg.ChangeLookAndFeel('GreenTan')
progresscount = 1000
layout = [
    [sg.Multiline(default_text='Paste document number to find', size=(100, 10),key='mline')],
    [sg.Text('_' * 102)],
    [sg.Text('Copy From:')],
    [sg.Combo(values=(r'C:\Docs', r'C:\Game'), size=(100, 3), key='copyfrom')],
    [sg.Text('Copy To:')],
    [sg.Combo(values=(r'D:\Docs', r'D:\Game'), size=(100, 3), key='copyto')],
    [sg.Text('_' * 102)],
    [sg.Text('Checking Completion:')],
    [sg.ProgressBar(progresscount, orientation='h', size=(50, 20), key='progressbar')],
    [sg.Button('Copy', key='_BUTTON_KEY_')]]

window = sg.Window('Documents Find & Copier', layout, default_element_size=(40, 1), grab_anywhere=False)
event, values = window.read()
progress_bar = window['progressbar']

ff = values['mline']
mpath = str(values['copyfrom'])
dstdir = str(values['copyto'])
print("from {}, to {}".format(mpath,dstdir))

"""
sg.Popup('Title',
         'The results of the window.',
         'The button clicked was "{}"'.format(event),
         'The values are', values)
"""
#read file in line by line#
numbering = 1
Totalfound = 0

tt = ff.splitlines()
tt = list(filter(None, tt)) #remove empty in list
t3 = len(tt)#check length of list
print(t3)

w = progresscount/t3

for x in tt:
    nn = x.strip()
    progress_bar.UpdateBar(numbering * w)
    print (str(numbering)+". Check For Drawing no : "+nn)
    numbering+=1
    xfound=0
    
    
    for root, dirs, files in os.walk(mpath):
        for file in files:
            #print(file)
            if file.rfind(nn) > -1:
                print(file)
                #print(os.path.join(root, file)+"\t"+file)
                shutil.copy(os.path.join(root, file), dstdir)
                xfound = xfound+1
                Totalfound = Totalfound+1
            else:
                pass
    
    print("Found : "+str(xfound))
    print("===============================================================")
    
print("Total Found : "+str(Totalfound))
if(Totalfound > 0):
    sg.Popup('Searching Result',
         'Searching Completed.\nThe results of the searching.',
         'Total found "{}"'.format(str(Totalfound)))
    window.close()

#window.close()

