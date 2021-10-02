import time
import os

#Specify a folder path here you've stored the wallpapers
path_of_folder = "/media/neelay/LinuxPart/Wallpapers/"

while(True):

    for file in os.listdir(path_of_folder):
        path_of_file = os.path.join(path_of_folder,file)
		
		#The Linux command to change the wallpaper
        cmd = f'gsettings set org.gnome.desktop.background picture-uri file:////{path_of_file}'
        os.system(cmd)
		
		#Wallpaper refreshes every 10 minutes, 10*60=600 seconds
        time.sleep(600)
