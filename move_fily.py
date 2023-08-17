import os
import shutil

from_dir= "c:/Users/Medhini/Downloads"
to_dir= "c:/Users/Medhini/OneDrive/Desktop/documnet_files"

list_of_files=os.listdir(from_dir)
#print(list_of_files)



for file_name in list_of_files:
    name,ext=os.path.splitext(file_name)

    if ext =='':
        continue
    if ext in['.pdf','.doc','.docx','.txt','.xls']:

        path1 =from_dir + '/' + file_name
        path2= to_dir + '/' + "documnet_files"
        path3 =to_dir + '/' + "documnet_files" + file_name

        if os.path.exists(path2):
            print("Moving" + file_name + "......")


            shutil.move(path1,path3)
        
        else:
            os.makedirs(path2)
            print("Moving" + file_name + ".......")
            shutil.move(path1,path3)

    


            