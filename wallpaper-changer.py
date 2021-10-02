import time
import os

path_of_folder = "/media/neelay/LinuxPart/Wallpapers/"

while(True):

    for file in os.listdir(path_of_folder):
        path_of_file = os.path.join(path_of_folder,file)

        cmd = f'gsettings set org.gnome.desktop.background picture-uri file:////{path_of_file}'
        os.system(cmd)
        time.sleep(600)

